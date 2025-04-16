import pandas as pd
import numpy as np

import clean_data
import filter_transform_data
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


def pca(df):
    scale = StandardScaler().fit_transform(df)

    pca = PCA(n_components=2)

    pcs = pca.fit_transform(scale)
    pca_df = pd.DataFrame(pcs, columns=['PC1', 'PC2'])

    plt.figure()
    plt.scatter(pca_df['PC1'], pca_df['PC2'])
    plt.title('PCA for Normalized Read Counts')

    plt.grid()
    plt.show()


def boxplots(df):
    plt.figure(figsize=(30, 6))
    df.boxplot()

    plt.title('Boxplots for Samples')
    plt.show()


def main():
    data = clean_data.normalize_cpm('/Users/sangeethavempati/Downloads/CCLE_RNAseq_reads.csv')
    print(data.shape)
    log_transform_df = filter_transform_data.log_transform(data)
    print(log_transform_df.shape)
    print(log_transform_df.head())
    #boxplots(log_transform_df)
    pca(log_transform_df)



if __name__ == '__main__':
    main()



