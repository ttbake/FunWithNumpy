import numpy as np
import pandas as pd

from utils import render

test_balance_data = {
    'pasan': 20.00,
    'treasure': 20.18,
    'ashley': 1.05,
    'craig': 42.42,
}

balances = pd.Series(test_balance_data)

unlabeled_balances = pd.Series([20.00, 20.18, 1.05, 42.42])

labeled_balances = pd.Series(
    [20.00, 20.18, 1.05, 42.42],
    index=['pasan', 'treasure', 'ashley', 'craig']
)

ndbalances = np.array([20.00, 20.18, 1.05, 42.42])
pd.Series(ndbalances)

pd.Series(20.00, index=["guil", "jay", "james", "ben", "nick"])

for label, value in balances.items():
    render("The label {} has a value of {}".format(label, value))

