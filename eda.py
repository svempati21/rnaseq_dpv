from sklearn.decomposition import PCA

import clean_data
import clean_data as cd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def mean_counts(df):
    row_averages = df.mean(axis=1)
    return row_averages

def pca(df):
    pca = PCA(n_components=2)


def main():
    data = clean_data.clean_data('/Users/sangeethavempati/Downloads/CCLE_RNAseq_reads.csv')
    means = mean_counts(data)
    print(means)



