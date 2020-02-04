# Setup
import os

import pandas as pd

from utils import make_chaos

from tests.helpers import check

pd.options.display.max_rows = 10
users = pd.read_csv(os.path.join('data', 'users.csv'), index_col=0)
# Pay no attention to the person behind the curtain
make_chaos(users, 19, ['first_name'], lambda val: val.lower())
## CHALLENGE - Verified email list ##

# TODO: Narrow list to those that have email verified.
email_list = users[users['email_verified']]
#  The only columns should be first, last and email
email_list = email_list.iloc[:,:3]

# TODO: Remove any rows missing last names
email_list = email_list[~email_list.last_name.isna()]

# TODO: Ensure that the first names are the proper case
email_list.loc[~email_list.first_name.str.istitle() , 'first_name'] = email_list.first_name.str.title()

# Return the new sorted DataFrame..last name then first name ascending
email_list.sort_values(
    ['last_name', 'first_name'],
    ascending=[True, True],
    inplace=True
)
email_list