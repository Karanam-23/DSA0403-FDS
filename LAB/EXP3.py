import numpy as np

# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1500, 250000],
    [5, 2200, 450000],
    [4, 1800, 320000],
    [6, 2800, 550000],
    [5, 2400, 480000]
])

# Select houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price
average_price = np.mean(filtered_houses[:, 2])

print("Average Sale Price:", average_price)
