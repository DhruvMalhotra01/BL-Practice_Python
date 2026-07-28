import numpy as np

daily_max_temperatures = [31.2, 31.5, 30.9, 31.3, 31.7, 31.9, 32.2]

mean_temperature = np.mean(daily_max_temperatures)
std_deviation = np.std(daily_max_temperatures)

print(f"Mean temperature (numpy): {mean_temperature:.2f}")
print(f"Standard deviation (numpy): {std_deviation:.2f}")