import pandas as pd

import clean_data
import filter_transform_data
import merge_metadata
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def pca_metadata(df, metadata, metadata_column):
    '''
    This function creates a PCA scatter plot colored by the metadata column.
    Parameters: the log transformed data, a string value for the
    metdata file location, and a string value for the metadata column name.
    Returns: nothing but creates and saves a PCA scatter plot.
    '''
    labels = df.columns
    scale = StandardScaler().fit_transform(df.T)

    pca = PCA(n_components=2)

    pcs = pca.fit_transform(scale)
    pca_df = pd.DataFrame(pcs, columns=['PC1', 'PC2'])
    pca_df.index = labels

    df, metadata = merge_metadata.read_metadata(df, metadata)

    merged = pd.concat([metadata, pca_df], axis=1)
    pd.set_option('display.max_columns', None)


    plt.figure(figsize=(14, 10))
    plot = sns.scatterplot(merged, x='PC1', y='PC2', hue=metadata_column)
    # sns docs
    sns.move_legend(plot, "upper left", bbox_to_anchor=(1, 1))
    plt.title('PCA for Normalized Read Counts')

    plt.grid()
    plt.savefig(f'PCA-{metadata_column}.png')
    plt.show()



def boxplots_metadata(df, metadata_column):
    '''
    This function creates a boxplots scatter plot for the specified
    metadata column.
    Parameters: merged dataframe, a string value for the metadata column name.
    Returns: nothing but creates and saves a boxplot scatter plot.
    '''
    plt.figure(figsize=(20, 20))
    sns.boxplot(x=metadata_column, y='value', data=df)

    plt.title('Boxplots for Samples')
    plt.savefig(f'Box-{metadata_column}.png')
    plt.show()

'''
def sample_correlation_metadata(df, metadata, metadata_column):
    df.set_index(df.columns[0], inplace=True)
    print(df.head())
    correlation = df.corr()

    df, metadata = merge_metadata.read_metadata(df, metadata)

    merged = pd.concat([metadata, correlation], axis=1)
    pd.set_option('display.max_columns', None)
    print(merged.head)

    plt.figure()
    sns.heatmap(correlation, hue=metadata_column)
    plt.title('Correlation Matrix')
    plt.show()
'''

def main():
    data = 'CCLE_RNAseq_reads.csv'
    log_transform_df = filter_transform_data.log_transform(data)
    metadata = 'sample_info.csv'
    merged = merge_metadata.merge_metadata_long(log_transform_df, metadata)
    '''
    pca_metadata(log_transform_df, metadata, 'sex')
    pca_metadata(log_transform_df, metadata, 'lineage')
    pca_metadata(log_transform_df, metadata, 'lineage_subtype')
    pca_metadata(log_transform_df, metadata, 'culture_type')
    pca_metadata(log_transform_df, metadata, 'sample_collection_site')
    pca_metadata(log_transform_df, metadata, 'primary_or_metastasis')
    pca_metadata(log_transform_df, metadata, 'disease')
    pca_metadata(log_transform_df, metadata, 'disease_subtype')
    pca_metadata(log_transform_df, metadata, 'age')

    '''
    '''
    boxplots_metadata(merged, 'sex')
    boxplots_metadata(merged, 'lineage')
    boxplots_metadata(merged, 'culture_type')
    boxplots_metadata(merged, 'sample_collection_site')
    boxplots_metadata(merged, 'primary_or_metastasis')
    boxplots_metadata(merged, 'lineage_subtype')
    boxplots_metadata(merged, 'disease')
    boxplots_metadata(merged, 'disease_subtype')
    boxplots_metadata(merged, 'age')
    '''

if __name__ == '__main__':
    main()
