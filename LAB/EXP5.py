import numpy as np

# Fuel efficiency (miles per gallon)
fuel_efficiency = np.array([25, 30, 28, 35])

# Average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Percentage improvement between first and second car
percentage_improvement = ((fuel_efficiency[1] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100

print("Average Fuel Efficiency:", average_efficiency)
print("Percentage Improvement:", percentage_improvement, "%")
