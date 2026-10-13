import numpy as np

# Item prices and quantities
prices = np.array([50, 80, 100])
quantities = np.array([2, 1, 3])

discount_rate = 10
tax_rate = 5

# Total amount
total = np.sum(prices * quantities)

# Apply discount
discounted_total = total - (total * discount_rate / 100)

# Add tax
final_total = discounted_total + (discounted_total * tax_rate / 100)

print("Total Amount:", total)
print("Final Amount:", final_total)
