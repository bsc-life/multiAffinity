import pandas as pd
import numpy as np

#import metadegs
degs = pd.read_csv('output/metaDEGs/metaDEGs.txt',sep=',')
degs = degs.groupby(['Name'],as_index=False).Score.mean()
degs = degs.rename(columns={'Name': 'metaDEGs', 'Score': 'Aggregate Rank'})
degs.to_csv("output/metaDEGs/metaDEGs.txt",sep = ",", index=None, header=True)
degs['metaDEGs'] = degs['metaDEGs'].astype('str')

#import affinity correlation
affinity = pd.read_csv('output/Affinity/Affinity_Corr.txt',sep=',',usecols=['Genes','Corr','Adj. p-val'], dtype=str)
affinity = affinity.rename(columns={'Genes': 'metaDEGs', 'Corr': 'difexp-Aff Corr', 'Adj. p-val':'Corr adj-p.val'})

#import communities
comm = pd.read_csv('output/Communities/degs_communities.txt',sep=';', names=['metaDEGs','Communities'], dtype=str)
comm.Communities = comm.Communities.replace(np.nan,0)
comm = comm.rename(columns={'Communities': 'Community ID'})

# import multiplex metrics
metrics = pd.read_csv('output/Affinity/part_coef.txt',sep=',', dtype=str)

#import differential expression values
difexp = pd.read_csv('output/Affinity/difexp.txt',sep=',', dtype=str)
difexp.log2FoldChange = difexp.log2FoldChange.replace(np.nan,0)
difexp = difexp.rename(columns={'genes': 'metaDEGs', 'log2FoldChange': 'log2FC'})

#import size communities
size_comm = pd.read_csv('output/Communities/size_communities.txt',sep='\t', usecols=['Size'], dtype=str)
size_comm.reset_index(inplace=True)
size_comm = size_comm.rename(columns = {'index':'Community ID','Size': 'Comm Size'})
size_comm['Community ID'] = size_comm['Community ID'] + 1
size_comm['Comm Size']=  size_comm['Comm Size'].astype(int)
size_comm['Community ID'] = size_comm['Community ID'].astype(str)


# Join metadegs, affinity correlation,communities and metrics
df = pd.merge(affinity,degs,how='inner',on='metaDEGs')
df = pd.merge(df,difexp,how='inner',on='metaDEGs')
df = pd.merge(df,comm,how='inner',on='metaDEGs')
df = pd.merge(df,size_comm,how='inner',on='Community ID')
df = pd.merge(df,metrics,how='inner',on='metaDEGs')
df = df.replace(np.nan,0)

# Rounds data
df['Aggregate Rank'] = pd.to_numeric(df['Aggregate Rank'])
df['Aggregate Rank'] = df['Aggregate Rank'].round(5)
df['difexp-Aff Corr'] = pd.to_numeric(df['difexp-Aff Corr'])
df['Corr adj-p.val'] = pd.to_numeric(df['Corr adj-p.val'])
df['log2FC'] = pd.to_numeric(df['log2FC'])
df['log2FC'] = df['log2FC'].round(5)
df['log2FC'] = pd.to_numeric(df['log2FC'])
df['log2FC'] = df['log2FC'].round(5)
df['part_coef'] = pd.to_numeric(df['part_coef'])
df['part_coef'] = df['part_coef'].round(5)

#remove duplicates
df = df.set_index(['metaDEGs']) 
df = df.groupby(level=0).first()

#filter results
#df = df[df['Corr adj-p.val'] < 0.05]
#df = df[df['Comm Size'] > 1]

# sort results
df = df.reindex(df['difexp-Aff Corr'].abs().sort_values(ascending=False).index)

# export final df
df.to_csv("output/multiAffinity_report.csv",sep = ",", index=True, header=True)