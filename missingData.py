import pandas as pd
import numpy as np

demo = pd.read_csv('Demographics.csv')
bmx = pd.read_csv('BodyMeasures.csv')
ocp = pd.read_csv('Occupation.csv')

valid_entries = demo.count()
total_rows = len(demo.index)
missing_data = total_rows - valid_entries

print(missing_data.head())

missing_percentage = missing_data/total_rows * 100
print(missing_percentage.head())

missing_data = np.sum(demo.isnull(), axis=1)
num_cols = len(demo.columns)
missing_percentage = missing_data/num_cols * 100
print(missing_data)

num_refused = sum(demo['DMDSCHOL'] == 7)
num_dontknow = sum(demo['DMDSCHOL'] == 9)
print('Number refused: %d' % num_refused)
print('Number unknown: %d' % num_dontknow)

unknown_ind = demo.loc[:, 'DMDSCHOL'] > 3
demo.loc[unknown_ind, 'DMDSCHOL'] = np.nan
print(demo['DMDSCHOL'].unique())

perc = (len(demo.index) - demo['DMDSCHOL'].count())/len(demo.index)*100
print('Percent missing: %d' % perc)

print('Demographics')
print(demo.dtypes.head())

print('\nBody Measures')
print(bmx.dtypes.head())

bmx.loc[:, 'SEQN'] = pd.to_numeric(bmx['SEQN'], errors='coerce', downcast='integer')

print('Demographics')
print(demo.dtypes.head())

print('\nBody Measures')
print(bmx.dtypes.head())

ind = np.isnan(bmx['SEQN'])
bmx = bmx.loc[~ind,:]
bmx.loc[:,'SEQN'] = pd.to_numeric(bmx['SEQN'], errors='coerce', downcast='integer')

print('Demographics')
print(demo.dtypes.head())

print('\nBody Measures')
print(bmx.dtypes.head())

minor_id = demo.loc[:, 'RIDAGEYR'] < 18
print(demo.loc[minor_id, 'DMDMARTL'].count())

demo.loc[minor_id, 'DMDMARTL'] = np.nan
print(demo.loc[minor_id, 'DMDMARTL'].count())
demo.loc[minor_id, 'RIDEXPRG'] = np.nan
print(demo.loc[minor_id, 'RIDEXPRG'].count())

demo.to_csv('Demographics.csv', index=False)
bmx.to_csv('BodyMeasures.csv', index=False)

