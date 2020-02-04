import numpy as np

orders = np.array([
    [2, 0, 0, 0],
    [4, 1, 2, 2],
    [0, 1, 0, 1],
    [6, 0, 1, 2]
])

totals = np.array([3, 20.50, 10, 14.25])

prices = np.linalg.solve(orders, totals)

inner_product = orders.dot(prices)
a, b = np.split(np.arange(1, 11), 2)
sum = a + b

print(prices)

print(inner_product)

print(sum)