import numpy as np
import clean_data


def mean_counts(df):
    '''
    Compute mean counts of each row.
    Parameters: string value that is absolute path to CSV data file
    Return: Averages for each row
    '''
    # Clean and normalize data
    df = clean_data.normalize_cpm(df)

    # Calculate row averages
    row_averages = df.mean(axis=1)
    return row_averages

def filter(df):
    '''
    Filter dataframe by
    Parameters: string value that is absolute path to CSV data file
    Return: cleaned and normalized df filtered by mean counts
    '''
    # Obtain mean counts for each row
    means = mean_counts(df)

    # Read in cleaned and normalized data
    df = clean_data.normalize_cpm(df)

    # Drop rows with means less than 1
    drop_indices = []
    for index, mean in enumerate(means):
        if mean < 1:
            drop_indices.append(index)
    new_df = df.drop(df.index[drop_indices])

    return new_df

def log_transform(df):
    '''
    Log transform read counts
    Parameters: string value that is absolute path to CSV data file
    Return: log transformed filtered df
    '''
    # Obtain filtered df
    filtered_df = filter(df)

    # Transform read counts by log base 2
    log_transform_df = filtered_df.apply(lambda x: np.log2(x + 1))
    return log_transform_df

def main():
    data = 'CCLE_RNAseq_reads.csv'
    log_transform_df = log_transform(data)
    print(log_transform_df.shape)
    print(log_transform_df.head())


if __name__ == '__main__':
    main()



