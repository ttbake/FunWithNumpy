import pandas as pd
import numpy as np

demo = pd.read_csv('Demographics.csv')
bmx = pd.read_csv('BodyMeasures.csv')

demo.loc[:,'Education'] = np.nan
index = (demo['DMDEDUC3'] < 13 | demo['DMDEDUC3'] == 55 | demo['DMDEDUC3'] == 66)
demo.loc[index, 'Education'] = 1

index = (demo['DMDEDUC3'] == 13 | demo['DMDEDUC3'] == 14)
demo.loc[index, 'Education'] = 2

index = (demo['DMDEDUC3'] == 15)
demo.loc[index, 'Education'] = 3

index = (demo['DMDEDUC3'] == 77)
demo.loc[index, 'Education'] = 7

index = (demo['DMDEDUC3'] == 99)
demo.loc[index, 'Education'] = 9

index = demo['DMDEDUC2'] <= 2
demo.loc[index, 'Education'] = 1

index = demo['DMDEDUC2'] == 3
demo.loc[index, 'Education'] = 2

index = (demo['DMDEDUC2'] == 4 | demo['DMDEDUC2'] == 5)
demo.loc[index, 'Education'] = 3

index = demo['DMDEDUC2'] == 7
demo.loc[index, 'Education'] = 7

index = demo['DMDEDUC2'] == 9
demo.loc[index, 'Education'] = 9

demo.drop('DMDEDUC2', axis=1, inplace=True)
demo.drop('DMDEDUC3', axis=1, inplace=True)

print(bmx[['BMXWT', 'BMXHT', 'BMXARMC']].corr())

demo.to_csv('Demographics.csv', index=False)