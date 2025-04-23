import pandas as pd

def basic_clean_data(df):
    '''
    Perform basic data cleaning and formatting
    Parameters: string value that is absolute path to CSV data file
    Returns: cleaned pandas dataframe
    '''
    # Read in dataframe and set first column as index
    counts = pd.read_csv(df, index_col=[0])
    # Remove instances of all zero counts
    counts = counts[counts.sum(axis=1)>0]
    # Drop NA rows
    counts = counts.dropna()
    # Convert all counts to integers
    counts_float = counts.select_dtypes(include=['float64']).columns
    counts[counts_float] = counts[counts_float].astype(int)

    # Transpose counts
    counts = counts.T

    # Separate ENSEMBL ID
    counts.index = counts.index.str.extract(r'\((.*?)\)')

    return counts

def normalize_cpm(df):
    '''
    Perform CPM normalization
    Parameters: string value that is absolute path to CSV data file
    Returns: normalized pandas dataframe
    '''
    # Perform data cleaning and formatting
    df_cleaned = basic_clean_data(df)
    # Perform CPM normalization for samples
    df_normalized = (df_cleaned / df_cleaned.sum()) * 1000000
    return df_normalized


def main():
    data = basic_clean_data('CCLE_RNAseq_reads.csv')
    print(data.head())
if __name__ == '__main__':
    main()




