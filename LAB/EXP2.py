import numpy as np

sales_data = np.array([
    [10.50, 15.20, 20.00],
    [8.99, 12.49, 15.00],
    [30.00, 45.50, 50.00]
])

average_price = np.mean(sales_data)

print(f"The average price of all products sold is: ${average_price:.2f}")
