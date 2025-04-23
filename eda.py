import pandas as pd
import numpy as np

import clean_data
import filter_transform_data
import merge_metadata
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


def pca(df):
    '''
    Generate PCA with principal components
    Parameters: string value that is absolute path to CSV data file
    Returns: Nothing, but generates plot and saves as png file
    '''

    # Preprocess the data so it is transformed onto unit scale
    scale = StandardScaler().fit_transform(df.T)

    # Perform PCA with two principal components for plotting
    pca = PCA(n_components=2)

    # Fit the PCA onto the scale
    pcs = pca.fit_transform(scale)
    pca_df = pd.DataFrame(pcs, columns=['PC1', 'PC2'])

    # Show PCA scatter plot
    plt.figure()
    plt.scatter(pca_df['PC1'], pca_df['PC2'])
    plt.title('PCA for Normalized Read Counts')

    plt.grid()
    plt.savefig('PCA_eda_final.png')
    plt.show()

def boxplots(df):
    '''
        Generate boxplot
        Parameters: string value that is absolute path to CSV data file
        Returns: Nothing, but generates plot and saves as png file
    '''
    plt.figure(figsize=(30, 6))
    # Generate box plot
    df.boxplot()

    plt.title('Boxplots for Samples')
    plt.savefig('box_eda_final.png')
    plt.show()

def sample_correlation(df):
    '''
    Generate correlation matrix and heatmap
    Parameters: string value that is absolute path to CSV data file
    Returns: Nothing, but generates plot and saves as png file
    '''
    # Generate correlation matrix
    correlation = df.corr()
    plt.figure()

    # Show heat map
    sns.heatmap(correlation)
    plt.title('Correlation Matrix')
    plt.savefig('corr_eda_final.png')
    plt.show()


def main():
    data = 'CCLE_RNAseq_reads.csv'
    log_transform_df = filter_transform_data.log_transform(data)
    print(log_transform_df.shape)
    print(log_transform_df.head())
    pca(log_transform_df)
    boxplots(log_transform_df)
    sample_correlation(log_transform_df)



if __name__ == '__main__':
    main()



