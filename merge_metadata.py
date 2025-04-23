import clean_data
import filter_transform_data
import eda

import pandas as pd

def read_metadata(df, filename):
    '''
    This function reads in metadata and matches it up with the data
    Parameters: a dataframe with the log transformed data, the filename for
    the metadata file
    Returns: edited metadata and df files
    '''

    # Read in metadata file
    metadata = pd.read_csv(filename)
    # Set first column to index
    metadata.set_index(metadata.columns[0], inplace=True)

    # Set samples back to index
    df = df.T
    # Drop samples not in df from metadata
    drop = metadata.index.difference(df.index)
    metadata = metadata.drop(drop)

    # Drop samples not in metadata from df
    drop = df.index.difference(metadata.index)
    df = df.drop(drop)

    # Make sure to transpose df back
    df = df.T

    return df, metadata

def merge_metadata_long(data, metadata):
    '''
    This function creates a long version of the merged data and metadata
    Parameters: a dataframe with the log transformed data, the filename for
    the metadata file
    Returns: a long version of the merged data and metadata
    '''

    # Read in both data and metadata, adjusted by each other
    data, metadata = read_metadata(data, metadata)

    # Transpose data
    data = data.T
    print(data.head())

    # Set index of data to DepMap_ID
    data = data.reset_index(names='DepMap_ID')
    long_data = pd.melt(data, id_vars='DepMap_ID')
    merged = pd.merge(long_data, metadata, on='DepMap_ID')
    return merged



def main():
    data = clean_data.normalize_cpm('CCLE_RNAseq_reads.csv')
    metadata = 'sample_info.csv'
    log_transform_df = filter_transform_data.log_transform(data)
    print(log_transform_df)
    pd.set_option('display.max_columns', None)
    #metadata_read = read_metadata(log_transform_df, metadata)
    metadata_read = merge_metadata_long(log_transform_df, metadata)
    #print(metadata_read.head())



if __name__ == '__main__':
    main()