import numpy as np
import pandas as pd
from clean_data import basic_clean_data, normalize_cpm


def test_clean_data():
    '''
    Test basic_clean_data function
    Assert if expected value is matched
    '''

    cleaned_data = basic_clean_data('edited_4x4.csv')

    expected = pd.DataFrame([[0,2669,31],[0,0,0],[3104,3552,992]])
    expected.index = [('ENSG00000000003',), ('ENSG00000000005',), ('ENSG00000000419',)]
    expected.columns = ['ACH-001097', 'ACH-001804', 'ACH-000534']

    assert expected.equals(cleaned_data)

def normalize_cpm_test():
    '''
    Test normalize_cpm function
    Assert if expected value is matched
    '''
    normalized_data = normalize_cpm('edited_4x4.csv')

    expected = pd.DataFrame([[(0/3104)*1000000,(2669/6221)*1000000,
                              (31/1023)*1000000],[(0/3104)*1000000,
                                                    (0/6221)*1000000,
                                                    (0 / 1023) * 1000000],
                             [(3104/3104)*1000000,(3552/6221)*1000000,
                              (992/1023)*1000000]])
    expected.index = [('ENSG00000000003',), ('ENSG00000000005',),
                      ('ENSG00000000419',)]
    expected.columns = ['ACH-001097', 'ACH-001804', 'ACH-000534']

    assert expected.equals(normalized_data)

def main():
    # data = test_clean_data()
    data = normalize_cpm_test()
if __name__ == '__main__':
    main()