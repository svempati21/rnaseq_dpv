import pandas as pd

counts = pd.read_csv('/Users/sangeethavempati/Downloads/CCLE_RNAseq_reads.csv')
counts = counts.set_index('Unnamed: 0')
# Take counts greater than 0
counts = counts[counts.sum(axis = 1) > 0]
# Convert all counts to integers
counts_float = counts.select_dtypes(include=['float64']).columns
counts[counts_float] = counts[counts_float].astype(int)

# Read in the metadata
metadata = pd.read_csv('/Users/sangeethavempati/Downloads/sample_info.csv')
# Make sure only metadata that matches IDs from counts
metadata1 = metadata[metadata['DepMap_ID'].isin(counts.index)]
metadata1 = metadata1.set_index('DepMap_ID')

# Make sure only counts that are accounted for in metadata
counts = counts[counts.index.isin(metadata1.index)]
# Transpose counts
counts = counts.T
