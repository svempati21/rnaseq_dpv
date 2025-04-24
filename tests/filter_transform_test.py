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

    expected = pd.Series([153111.244254,0.000000,846888.755746])
    expected.index = [('ENSG00000000003',), ('ENSG00000000005',), ('ENSG00000000419',)]
    print(expected)
    print(type(expected))

    print(expected.compare(cleaned_data))

    assert expected.equals(cleaned_data)

def test_filter():
    '''
    Test filter function
    Assert if expected value is matched
    '''
    filtered_data = ft.filter('edited_4x4.csv')

    expected = pd.DataFrame([[0.0,429030.702459,30303.030303],[1000000.0,570969.297541,969696.969697]])
    expected.index = [('ENSG00000000003',), ('ENSG00000000419',)]
    expected.columns = ['ACH-001097', 'ACH-001804', 'ACH-000534']
    print(expected.compare(filtered_data))

    assert expected.equals(filtered_data)



def main():
    #data = test_mean_counts()
    data = test_filter()
if __name__ == '__main__':
    main()