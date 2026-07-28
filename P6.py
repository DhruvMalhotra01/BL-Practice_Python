import statistics

daily_max_temperatures = [31.2, 31.5, 30.9, 31.3, 31.7, 31.9, 32.2]

mean_temperature = statistics.mean(daily_max_temperatures)
std_deviation = statistics.stdev(daily_max_temperatures)

print(f"Mean temperature: {mean_temperature:.2f}")
print(f"Standard deviation: {std_deviation:.2f}")