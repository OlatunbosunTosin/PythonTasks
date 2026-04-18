import statistics
values = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]

mean_value = statistics.mean(values)
median_value = statistics.median(values)
most_frequent = statistics.mode(values)

print(f"mean = {mean_value}\nmedian = {median_value}\nmode = {most_frequent}")

#mode returns the lowest number out of the two modes
