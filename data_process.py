import pandas as pd
import os
from cmapPy.pandasGEXpress.parse import parse

def read_data(gct_file_path):
    # Parse the data
    data = parse(gct_file_path)
    return data

def gct_to_csv(gct_file_path, csv_file_path):
    data = read_data(gct_file_path)
    # Store the data_df attribute
    df = data.data_df

    # Convert this to a csv
    csv_file = csv_file_path
    df.to_csv(csv_file, index=True)

def metadata_to_csv(txt_file_path, csv_file_path):
    metadata = pd.read_csv(txt_file_path, sep='\t')
    metadata.to_csv(csv_file_path, index=False)



def main():
    file = "/Users/sangeethavempati/Downloads/CCLE_RNAseq_genes_counts_20180929.gct"
    metadata_file = "/Users/sangeethavempati/Downloads/Cell_lines_annotations_20181226.txt"
    gct_to_csv(file, "rnaseq.csv")
    metadata_to_csv(metadata_file, 'metadata.csv')


if __name__ == "__main__":
    main()
