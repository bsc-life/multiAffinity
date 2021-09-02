import pandas as pd
import numpy as np
import os

# Load dictionary
gene_dict = pd.read_csv('MultiAffinity/tmp/gene_dict.txt',sep='\t')
gene_dict = gene_dict.set_index('Genes')['ids'].to_dict()

df = pd.read_csv('MultiAffinity/tmp/degs_names.txt', header=None)
df[0] = df[0].apply(lambda x: gene_dict.get(x, x))
df = df[pd.to_numeric(df[0], errors='coerce').notnull()]

df.to_csv('MultiAffinity/tmp/degs_ids.txt', sep='\t',index=False, header=None)