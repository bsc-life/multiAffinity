import os
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import spearmanr

#Load expression matrices and join
# load all table files
path_to_files = '1-Obtaining-DEGs-for-HB/Matrices_HB/Normalized_HB/'
lst_expmat = []
for filen in [x for x in os.listdir(path_to_files) if '.txt' in x]:
    lst_expmat.append(pd.read_csv(path_to_files+filen, delimiter= "\t"))
expression_mats = pd.concat(lst_expmat, ignore_index=True)
expression_mats = expression_mats.groupby(['Unnamed: 0']).mean().reset_index()

expression_mats = expression_mats.set_index(['Unnamed: 0'])
expression_mats = expression_mats.loc[:, ~expression_mats.columns.str.startswith('Normal')]
expression_genes = expression_mats.mean(axis=1)
expression_genes = pd.DataFrame(expression_genes, columns=['expression'])
expression_genes.index.names = ['genes']
expression_genes.drop(expression_genes.loc[expression_genes['expression']==0].index, inplace=True)

#Load degs
degs_path = '1-Obtaining-DEGs-for-HB/DEGs_HB/HB_db_DEG.csv'
degs = pd.read_csv(degs_path, index_col=0)
degs_names = degs.index.tolist()

#Load rwr matrice
mat_path = '2-HB-DEGs-on-Liver-Communities/4_NodeAffinity/PTmatrix_tmp_PPI.txt'
mat = pd.read_csv(mat_path, sep='\t', index_col=0)

#Find gene matches 
mat_names = mat.index.tolist()
matches = list(set(degs_names).intersection(set(mat_names)))

# create joined matrice
mat_degs = mat.filter(matches, axis=1) # filter only DEGs in column
mat_degs.index.names = ['genes']

result = expression_genes.merge(mat_degs, left_index=True, right_index=True)

# Find larger correlations (top 10)
genes = (result.columns[1:])

corr_list = []
for i in genes:
    corr_df = result[['expression',i]]
    corr_df.corr(method='spearman')
    if spearmanr(corr_df)[1] <= 0.05:
        corr_list.append(spearmanr(corr_df)[0])

top_list = sorted(corr_list, key=abs, reverse=True)[:10]

for i in genes:
    corr_df = result[['expression',i]]
    corr_df.corr(method='spearman')
    corr = spearmanr(corr_df)[0]
    if corr in top_list:
        print(i,'\t',spearmanr(corr_df)[0],'\t',spearmanr(corr_df)[1])