import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.stats.multitest as multi
from tqdm import tqdm
from tabulate import tabulate

metadata_dict = {}
metadata = pd.read_csv('/home/mar/Documents/TFM/June/Task1_v4/Metadata_HB/metadata_joined.csv')
lst = []
for i in metadata['type']:
    if str(i).startswith('Hepatoblastoma'):
        lst.append('case')
    elif str(i).startswith('Normal'):
        lst.append('control')
    else:
        lst.append('other')
metadata['class'] = lst
metadata_dict = pd.Series(metadata['class'].values,index=metadata['sample']).to_dict()

data = pd.read_csv('/home/mar/Documents/TFM/June/Task1_v4/Matrices_HB/Joint_matrix.txt', sep=';', index_col=0)
data.columns = data.columns.map(metadata_dict)
data = data.rename_axis('gene')

# Independent Unequal Variance T-Test per gene
tstatistic = []
pvalue = []
effsize = []
mean_case = []
mean_control = []
std_case = []
std_control = []
for idx in tqdm(data.index):

    case = data['case'].loc[idx].tolist()
    control = data['control'].loc[idx].tolist()

    t = stats.ttest_ind(case, control, equal_var = False)
    tstatistic.append(t[0])
    pvalue.append(t[1])

    # Cohen's d effect size (i.e., standardized mean difference)
    # d=0.2 small; d=0.5 medium; d=0.8 large

    es = (np.mean(case) - np.mean(control)) / np.std(case+control)
    effsize.append(es)
    mean_case.append(np.mean(case))
    mean_control.append(np.mean(control))
    std_case.append(np.std(case))
    std_control.append(np.std(control))

data['mean_case'] = mean_case
data['mean_control'] = mean_case
data['std_case'] = std_case
data['std_control'] = std_control
data['t-statistic'] = tstatistic
data['p-value'] = pvalue
data['effect size'] = effsize
data['adj_p-value'] = np.nan


# debug adj-pvalue
for idx in tqdm(data.index):
    pvalue = data.at[idx,'p-value']
    adj_pvalue = float((multi.multipletests(pvalue, method='fdr_bh')[1]))
    data.loc[idx,'adj_p-value'] = adj_pvalue
    

# export obtained stats 
#data.to_csv("Outputs_HB/HB_db_stats.csv", index=True)

# create df with only stats
data_stats = data[["adj_p-value","effect size"]]
data_stats = data_stats.dropna(axis=0, subset=["effect size"])


print('Filter DEG by adj p-value < 0.05 and Cohens effect size d > 1.2 (large)')

# Select desregulated genes
DEGS = data_stats[data_stats['adj_p-value'] < 0.05]
DEGS = DEGS[abs(DEGS["effect size"]) > 1.2]

DEGS = DEGS.sort_values(by="effect size", ascending=False)

print('higher effect-size:\n',
      DEGS.head(10),
      '\n\nlower effect-size:\n',
      DEGS.tail(10))


print('\ntotal num. of genes:',len(data_stats))
print('num. of DEG:',len(DEGS))

# export obtained stats 
DEGS.to_csv('/home/mar/Documents/TFM/June/Task1_v4/HB_db_DEG.csv', index=True)