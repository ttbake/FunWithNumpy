import pandas as pd
import numpy as np

demo = pd.read_csv('Demographics.csv')
bmx = pd.read_csv('BodyMeasures.csv')
ocq = pd.read_csv('Occupation.csv')

np.testing.assert_array_equal(demo.shape, (9761,144))
np.testing.assert_array_equal(bmx.shape, (9278,38))
np.testing.assert_array_equal(ocq.shape, (7212,36))

dataset = pd.merge(demo, bmx, on='SEQN', how='inner')
dataset = pd.merge(dataset, ocq, on='SEQN', how='inner')

total_cols = demo.shape[1] + bmx.shape[1] + ocq.shape[1] - 2
np.testing.assert_equal(dataset.shape[1], total_cols)
np.testing.assert_array_less(dataset.shape[0], demo.shape[0])

for col in demo.columns:
    try:
        demo.loc[:,col] = demo.loc[:,col].str.strip()
    except AttributeError:
        pass

valid_codes = {'DMDBORN' : [1,2,3,7,9],
               'DMDCITZN' : [1,2,7,9]}

for col in valid_codes.keys():
    goodInd = demo[col].isin(valid_codes[col])
    demo.loc[~goodInd,col] = np.nan

valid_range = {'BMXWT' : [0,635],
               'BMXHT' : [81.8,201.3]}

for col in valid_range.keys():
    goodInd = (bmx[col] >= valid_range[col][0]) & (bmx[col] <= valid_range[col][1])
    bmx.loc[~goodInd,col] = np.nan

max_missing_perc = 30

valid_entries = demo.count()
total_rows = len(demo.index)
missing_percentage = (total_rows - valid_entries) / total_rows * 100
missing_bool = missing_percentage > max_missing_perc
print(demo.columns[missing_bool])