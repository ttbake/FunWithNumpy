import pandas as pd

demo = pd.read_csv('Demographics.csv')
bmx = pd.read_csv('BodyMeasures.csv')
ocp = pd.read_csv('Occupation.csv')

print(demo.describe())

# print(demo.head())
print(demo.loc[:,:].dtypes)
print(demo.columns.to_series().groupby(demo.dtypes).groups)
print(demo.loc[:,['SEQN','RIDAGEYR','RIAGENDR','DMQMILIT']].dtypes)

# Military status DMQMILIT replacement
print(len(demo['DMQMILIT'].unique()))
print(demo['DMQMILIT'].unique())
demo.loc[:,'DMQMILIT'] = demo.loc[:,'DMQMILIT'].str.strip()
replace_dict = {'DMQMILIT' : {
    'Y' : 'Yes',
    'N' : 'No'
}}
demo.replace(replace_dict, inplace=True)
print(len(demo['DMQMILIT'].unique()))
print(demo['DMQMILIT'].unique())
#print(demo.iloc[0:4,0:5])

# Citizen status DMDCITZN replacement
print(len(demo['DMDCITZN'].unique()))
print(demo['DMDCITZN'].unique())
demo.loc[:,'DMDCITZN'] = demo.loc[:,'DMDCITZN'].str.strip()
replace_dict = {'DMDCITZN' : {
    "Dont know" : "Don't know",
    "Don't Know" : "Don't know",
    "Unknown" : "Don't know"
}}
demo.replace(replace_dict, inplace=True)
print(len(demo['DMDCITZN'].unique()))
print(demo['DMDCITZN'].unique())

# Interview/examination status RIDSTATR replacement
print(len(demo['RIDSTATR'].unique()))
print(demo['RIDSTATR'].unique())
demo.loc[:,'RIDSTATR'] = demo.loc[:,'RIDSTATR'].str.strip()
replace_dict = {'RIDSTATR' : {
    "Exam" : "Both Interviewed and MEC examined",
    "Both" : "Both Interviewed and MEC examined",
    "exam" : "Both Interviewed and MEC examined",
    "interview" : "Interviewed Only",
    "Interview" : "Interviewed Only",
    "Interview Only" : "Interviewed Only",
    "Both Interviewed and MCE examined" : "Both Interviewed and MEC examined"
}}
demo.replace(replace_dict, inplace=True)
print(len(demo['RIDSTATR'].unique()))
print(demo['RIDSTATR'].unique())

# Gender RIAGENDR replacement
print(len(demo['RIAGENDR'].unique()))
print(demo['RIAGENDR'].unique())
demo.loc[:,'RIAGENDR'] = demo.loc[:,'RIAGENDR'].str.strip()
replace_dict = {'RIAGENDR' : {
    "F" : "Female",
    "M" : "Male"
}}
demo.replace(replace_dict, inplace=True)
print(len(demo['RIAGENDR'].unique()))
print(demo['RIAGENDR'].unique())

# Race/ethnicity RIDRETH1 replacement
print(len(demo['RIDRETH1'].unique()))
print(demo['RIDRETH1'].unique())
demo.loc[:,'RIDRETH1'] = demo.loc[:,'RIDRETH1'].str.strip()
print(len(demo['RIDRETH1'].unique()))
print(demo['RIDRETH1'].unique())

# Country of birth DMDBORN replacement
print(len(demo['DMDBORN'].unique()))
print(demo['DMDBORN'].unique())
demo.loc[:,'DMDBORN'] = demo.loc[:,'DMDBORN'].str.strip()
print(len(demo['DMDBORN'].unique()))
print(demo['DMDBORN'].unique())

# Length of time in US DMDYRSUS replacement
print(len(demo['DMDYRSUS'].unique()))
print(demo['DMDYRSUS'].unique())
demo.loc[:,'DMDYRSUS'] = demo.loc[:,'DMDYRSUS'].str.strip()
print(len(demo['DMDYRSUS'].unique()))
print(demo['DMDYRSUS'].unique())

# Education level children/youth 6-19 DMDEDUC3 replacement
print(len(demo['DMDEDUC3'].unique()))
print(demo['DMDEDUC3'].unique())
demo.loc[:,'DMDEDUC3'] = demo.loc[:,'DMDEDUC3'].str.strip()
print(len(demo['DMDEDUC3'].unique()))
print(demo['DMDEDUC3'].unique())

# Education level adults 20+ DMDEDUC2 replacement
print(len(demo['DMDEDUC2'].unique()))
print(demo['DMDEDUC2'].unique())
demo.loc[:,'DMDEDUC2'] = demo.loc[:,'DMDEDUC2'].str.strip()
print(len(demo['DMDEDUC2'].unique()))
print(demo['DMDEDUC2'].unique())

# Now attending school DMDSCHOL replacement
print(len(demo['DMDSCHOL'].unique()))
print(demo['DMDSCHOL'].unique())
demo.loc[:,'DMDSCHOL'] = demo.loc[:,'DMDSCHOL'].str.strip()
replace_dict = {'DMDSCHOL' : {
    "Neither" : "Neither in school or on vacation from school (between grades)",
    "Neither in school or on vacation frm school (between grades)" : "Neither in school or on vacation from school (between grades)"
}}
demo.replace(replace_dict, inplace=True)
print(len(demo['DMDSCHOL'].unique()))
print(demo['DMDSCHOL'].unique())

# Marital status DMDMARTL replacement
print(len(demo['DMDMARTL'].unique()))
print(demo['DMDMARTL'].unique())
demo.loc[:,'DMDMARTL'] = demo.loc[:,'DMDMARTL'].str.strip()
print(len(demo['DMDMARTL'].unique()))
print(demo['DMDMARTL'].unique())

dataset = pd.merge(demo, bmx, on='SEQN', how='inner')
dataset.to_csv('Demographics.csv', index=False)