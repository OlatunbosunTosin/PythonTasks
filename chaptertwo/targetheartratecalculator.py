age = int(input("How old are you? "))
maximum_heart_rate = 220 - age
lower_heart_rate = 0.5 * maximum_heart_rate
higher_heart_rate = 0.85 * maximum_heart_rate
print("Maximum heart rate is", maximum_heart_rate, "and Range of your target heart rate is", lower_heart_rate, "-", higher_heart_rate)
