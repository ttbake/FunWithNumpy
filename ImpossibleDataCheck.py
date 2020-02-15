import pandas as pd
import numpy as np
import itertools

demo = pd.read_csv('Demographics.csv')
bmx = pd.read_csv('BodyMeasures.csv')
ocp = pd.read_csv('Occupation.csv')

print(bmx['BMXWT'].describe())
ind = bmx['BMXWT'] < 0
bmx.loc[ind, 'BMXWT'] = np.nan
ind = bmx['BMXWT'] > 635
bmx.loc[ind, 'BMXWT'] = np.nan
print(bmx['BMXWT'].describe())

ind = bmx['BMIWT'] > 4
bmx.loc[ind, 'BMIWT'] = np.nan
print(bmx['BMIWT'].unique())

mean_wt = np.nanmean(bmx['BMXWT'])
std_wt = np.nanstd(bmx['BMXWT'])
min_wt = np.nanmin(bmx['BMXWT'])
max_wt = np.nanmax(bmx['BMXWT'])

low_wt_zscore = (min_wt - mean_wt)/std_wt
high_wt_zscore = (max_wt - mean_wt)/std_wt

print('Max weight z score: %d' % high_wt_zscore)
print('Min weight z score: %d' % low_wt_zscore)

print(np.nanmax(demo['RIDAGEYR']))
ind = demo['RIDAGEYR'] > 85
demo.loc[ind, 'RIDAGEYR'] = 85

demo.to_csv('Demographics.csv')
bmx.to_csv('BodyMeasures.csv')
ocp.to_csv('Occupation.csv')