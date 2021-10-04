import pandas as pd
import numpy as np

#import metadegs
degs = pd.read_csv('output/metaDEGs/metaDEGs/metaDEGs.txt',sep=',')
degs = degs.rename(columns={'Name': 'metaDEGs', 'Score': 'RRA Score'})
degs['metaDEGs'] = degs['metaDEGs'].astype('str')

#import affinity correlation
affinity = pd.read_csv('output/Affinity/Affinity_Corr.txt',sep=',',usecols=['Genes','Corr'], dtype=str)

affinity = affinity.rename(columns={'Genes': 'metaDEGs', 'Corr': 'Affinity Corr'})
#affinity['metaDEGs'] = affinity['metaDEGs'].astype('str')

#import communities
comm = pd.read_csv('output/Communities/degs_communities.txt',sep=';', names=['metaDEGs','Communities'], dtype=str)
comm.Communities = comm.Communities.replace(np.nan,0)
#comm.Communities = comm.Communities.astype(int)
#comm.Communities = comm.Communities.round()

# Join metadegs, affinity correlation and communities
df = pd.merge(pd.merge(degs,affinity,how='left',on='metaDEGs'),comm,how='left',on='metaDEGs')
df = df.replace(np.nan,0)

# Rounds and order data
df['RRA Score'] = pd.to_numeric(df['RRA Score'])
df['RRA Score'] = df['RRA Score'].round(5)


df['Affinity Corr'] = pd.to_numeric(df['Affinity Corr'])
df = df.sort_values(by='Affinity Corr', ascending=False)
df['Affinity Corr'] = df['Affinity Corr'].round(5)

# export final df
df.to_csv("output/multiAffinity_report.csv",sep = ",", index=None, header=True)