import clean_data
import filter_transform_data
import eda

import pandas as pd

def read_metadata(filename):
    metadata = pd.read_csv(filename)
    return metadata

def merge_metadata_pca(metadata, data):
    '''
    Merge metadata and data
    Parameters:
    metadata: string value for path to metadata
    data: adjusted read counts
    Returns: merged metadata and data
    '''
    metadata = read_metadata(metadata)
    data = data.T
    print(data.head())
    data = data.reset_index(names='DepMap_ID')
    merged = pd.merge(metadata, data, on='DepMap_ID')
    print(merged.head())
    return merged

def merge_metadata_long(metadata, data):

    # long form combined df for other plots to access by sample
    metadata = read_metadata(metadata)
    data = data.T
    # Make customizable if different column names?
    data = data.reset_index(names='DepMap_ID')
    long_data = pd.melt(data, id_vars='DepMap_ID')
    merged = pd.merge(long_data, metadata, on='DepMap_ID')
    return merged



def main():
    data = clean_data.normalize_cpm('CCLE_RNAseq_reads.csv')
    metadata = 'sample_info.csv'
    log_transform_df = filter_transform_data.log_transform(data)
    print(merge_metadata_pca(metadata, log_transform_df).head())





if __name__ == '__main__':
    main()