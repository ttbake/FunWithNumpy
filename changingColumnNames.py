import pandas as pd

demo = pd.read_csv('Demographics.csv')
bmx = pd.read_csv('BodyMeasures.csv')
ocp = pd.read_csv('Occupation.csv')

# Value replacement from string to float64
replace_dict = {'DMQMILIT' : {
    'Yes' : 1,
    'No' : 2,
    'Refused' : 7,
    "Don't know" : 9},
                'DMDCITZN' : {
    'Citizen by birth or naturalization' : 1,
    'Not a citizen of the US' : 2,
    'Refused' : 7,
    "Don't know" : 9
    }
}
demo.replace(replace_dict, inplace=True)

# Column rename
column_dict = {'DMQMILIT' : 'Veteran/Military Status',
               'DMDCITZN' : 'Citizenship Status'}
demo.rename(columns=column_dict, inplace=True)

dataset = pd.merge(demo, bmx, on='SEQN', how='inner')
dataset.to_csv('Demographics.csv', index=False)