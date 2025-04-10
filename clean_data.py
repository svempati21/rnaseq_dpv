import pandas as pd

def clean_data(df):

    counts = pd.read_csv(df)
    counts = counts.set_index('Unnamed: 0')
    # Take counts greater than 0
    counts = counts[counts.sum(axis = 1) > 0]
    counts = counts.dropna()
    # Convert all counts to integers
    counts_float = counts.select_dtypes(include=['float64']).columns
    counts[counts_float] = counts[counts_float].astype(int)

    # Transpose counts
    counts = counts.T

    return counts

def main():
    data = clean_data('/Users/sangeethavempati/Downloads/CCLE_RNAseq_reads.csv')
    print(data.head())
if __name__ == '__main__':
    main()




