import itertools
import scipy.stats as stats
import scanpy as sc
import anndata as ad
import matplotlib.pyplot as plt
import pandas as pd


def log2fold_change(merged, metadata_column):
    subset = merged[['variable', 'value', metadata_column]]
    genes = subset.groupby(['variable', metadata_column])['value'].mean()
    genes = genes.reset_index()
    print(genes.head())


    unique_genes = genes['variable'].unique()


    stats_df = pd.DataFrame()
    for gene in unique_genes:
        this_gene = genes[genes['variable'] == gene]
        this_gene = this_gene.reset_index()
        length = len(this_gene['value'])
        combinations = itertools.combinations(range(length), 2)
        for combination in combinations:
            index1 = combination[0]
            index2 = combination[1]
            change = this_gene['value'][index1] - this_gene['value'][index2]
            label = f'{this_gene[metadata_column][index1]} vs {this_gene[metadata_column][index2]}'
            new_row = pd.DataFrame({'gene': gene, 'combination': label, 'log2foldchange': change})
            stats_df = pd.concat([stats_df, new_row])
    return stats_df

def pvalue(merged, metadata_column):
    subset = merged[['variable', 'value', metadata_column]]

    unique_genes = subset['variable'].unique()
    print(len(unique_genes))

    stats_df = pd.DataFrame()
    counter = 0
    for gene in unique_genes:
        this_gene = subset[subset['variable'] == gene]
        this_gene = this_gene.reset_index()

        possible_values = this_gene[metadata_column].unique()
        combinations = itertools.combinations(possible_values, 2)
        for combination in combinations:
            print(combination)
            group1 = this_gene[this_gene[metadata_column] == combination[0]]['value']
            group2 = this_gene[this_gene[metadata_column] == combination[1]]['value']

            t, p = stats.ttest_ind(group1, group2)

            label = f'{combination[0]} vs {combination[1]}'
            new_row = pd.DataFrame({'gene': gene, 'combination': label, 'p-value': p})
            stats_df = pd.concat([stats_df, new_row])
        print(counter)
        counter += 1

    return stats_df