import numpy as np
import clean_data


def mean_counts(df):
    row_averages = df.mean(axis=1)
    return row_averages

def filter(df):
    means = mean_counts(df)
    drop_indices = []
    for index, mean in enumerate(means):
        if mean < 1:
            drop_indices.append(index)
    new_df = df.drop(df.index[drop_indices])

    return new_df

def log_transform(df):
    filtered_df = filter(df)
    print(filtered_df.head())
    log_transform_df = filtered_df.apply(lambda x: np.log2(x + 1))
    return log_transform_df

def main():
    data = clean_data.normalize_cpm('/Users/sangeethavempati/Downloads/CCLE_RNAseq_reads.csv')
    print(data.shape)
    log_transform_df = log_transform(data)
    print(log_transform_df.shape)
    print(log_transform_df.head())


if __name__ == '__main__':
    main()



