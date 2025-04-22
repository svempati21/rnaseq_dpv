import pandas as pd

def clean_data(df):

    counts = pd.read_csv(df, index_col=[0])
    # Take counts greater than 0
    counts = counts[counts.sum(axis=1)>0]
    counts = counts.dropna()
    # Convert all counts to integers
    counts_float = counts.select_dtypes(include=['float64']).columns
    counts[counts_float] = counts[counts_float].astype(int)

    # Transpose counts
    counts = counts.T

    counts.index = counts.index.str.extract(r'\((.*?)\)')

    return counts

'''
def ensemble_ids(df):
    df_cleaned = clean_data(df)

    # counts.index = counts.index.str.extract(r'ENS')
    counts.index = counts.index.str.replace(r'ENS[A-Z]+[0-9]{11}', regex=True)
    print(counts.index)
'''

def normalize_cpm(df):
    df_cleaned = clean_data(df)
    df_normalized = (df_cleaned / df_cleaned.sum()) * 1000000
    return df_normalized


def main():
    data = clean_data('CCLE_RNAseq_reads.csv')
    print(data.head())
if __name__ == '__main__':
    main()




