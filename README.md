# RNA Seq Data Processing and Visualization
**RNA Seq DPV** is a package that cleans, processes, and filters RNA seq read counts. It provides some plots for exploratory data analysis. RNA Seq DPV then takes in metadata and produces more accurate plots. Development has started on producing volcano plots but is still in progress.


## Description
RNA Seq DPV is intended to demonstrate ability to take a large file of RNA seq raw counts as well as associated metadata and perform beginning analyses on this data. It performs data cleaning, normalizing, and filtering including log2 transformation. This package then allows for exploratory data analysis in the form of PCA, box plots, and sample-sample correlation. The pipeline then provides a module for reading in metadata and incorporating this with both PCA and box plots. This projected was tested with and is intended to be used with the CCLE DepMap Public 20Q1 Dataset or similarly structured datasets.

## Setup

Dependencies can all be found in `requirements.txt`. To install, please clone repo from GitHub.


## Executing Program

The program can be started from any point if the user would like to normalize independently. This is the recommended sequence:

**Step One**
In the eda file, run `filter_transform_data.log_transform(data)`, swapping in an absolute path to the read counts file for data. Plots will automatically save to the project directory, please adjust file names and locations to save according to user preference.

**Step Two**
In the metadata_plots file, run `filter_transform_data.log_transform(data)`, swapping in an absolute path to the read counts file for data. Run `merge_metadata.merge_metadata_long(log_transform_df, metadata)`, swapping in the log transformed data from the previous step, as well as a string value for the absolute path to the metadata file. These plots will also save automatically but please adjust as needed.
 

## Authors
Sangeetha Vempati  @svempati21


## Acknowledgements:
This project was tested with the CCLE DepMap Public 20Q1 Dataset:
For this DepMap release:
DepMap, Broad (2020): DepMap 20Q1 Public. figshare. Dataset doi:10.6084/m9.figshare.11791698.v2.
For CRISPR datasets:
Robin M. Meyers, Jordan G. Bryan, James M. McFarland, Barbara A. Weir, ... David E. Root, William C. Hahn, Aviad Tsherniak. Computational correction of copy number effect improves specificity of CRISPR-Cas9 essentiality screens in cancer cells. Nature Genetics 2017 October 49:1779–1784. doi:10.1038/ng.3984
Dempster, J. M., Rossen, J., Kazachkova, M., Pan, J., Kugener, G., Root, D. E., & Tsherniak, A. (2019). Extracting Biological Insights from the Project Achilles Genome-Scale CRISPR Screens in Cancer Cell Lines. BioRxiv, 720243.
For omics datasets:
Mahmoud Ghandi, Franklin W. Huang, Judit Jané-Valbuena, Gregory V. Kryukov, ... Todd R. Golub, Levi A. Garraway & William R. Sellers. 2019. Next-generation characterization of the Cancer Cell Line Encyclopedia. Nature 569, 503–508 (2019).
