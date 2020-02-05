import pandas as pd
import numpy as np
import itertools

demo = pd.read_csv('Demographics.csv')
bmx = pd.read_csv('BodyMeasures.csv')
ocp = pd.read_csv('Occupation.csv')

demo.sort_values('SEQN', inplace=True)
ind = demo['SEQN'].duplicated(keep=False)

print('Duplicated rows: %i' % len(demo.loc[ind,:]))
demo.loc[ind,:].head()

demo.drop_duplicates(inplace=True)
ind = demo['SEQN'].duplicated(keep=False)
print('Duplicated rows: %i' % len(demo.loc[ind,:]))

dup_id = demo.loc[ind, 'SEQN'].unique()
for id in dup_id:
    dup_rows = np.where(demo['SEQN'] == id)[0]
    for (row1, row2) in itertools.product(dup_rows, repeat=2):
        demo.iloc[row1,:] = demo.iloc[row1,:].fillna(demo.iloc[row2,:], axis=0)

demo.drop_duplicates(inplace=True)
ind = demo['SEQN'].duplicated(keep=False)
print('Duplicated rows: %i' % len(demo.loc[ind,:]))

ind = demo['SEQN'].duplicated(keep=False)

demo = demo.loc[~ind,:]

ind = demo['SEQN'].duplicated(keep=False)
print('Duplicate rows: %i' % len(demo.loc[ind,:]))

print(set(demo.columns).intersection(bmx.columns))

bmx.drop('RIDAGEYR', 1, inplace=True)

print(set(demo.columns).intersection(bmx.columns))

dataset = pd.merge(demo, bmx, on='SEQN', how='inner')

