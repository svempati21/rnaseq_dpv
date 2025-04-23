import numpy as np
import pandas as pd
import filter_transform_data as ft


def test_mean_counts():
    '''
    Test mean_counts function
    Assert if expected value is matched
    '''

    cleaned_data = ft.mean_counts('edited_4x4.csv')
    print(cleaned_data)
    print(type(cleaned_data))

    expected = pd.Series([(429030.702459+30303.030303)/3,0.000000,(1000000.0+570969.297541+969696.969697)/3])
    expected.index = [('ENSG00000000003',), ('ENSG00000000005',), ('ENSG00000000419',)]
    print(expected)
    print()

    assert expected.equals(cleaned_data)


def main():
    data = test_mean_counts()
if __name__ == '__main__':
    main()