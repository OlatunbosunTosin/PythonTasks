years = int(input("Enter number of years: "))

current_population = 312032486
birth_rate = (60 * 60 * 24 * 365) // 7
death_rate = (60 * 60 * 24 * 365) // 13
new_immigrant = (60 * 60 * 24 * 365) // 45
additional_population = birth_rate + new_immigrant - death_rate
new_population_year_one = current_population + additional_population
new_population_year_two = new_population_year_one + additional_population
new_population_year_three = new_population_year_two + additional_population
new_population_year_four = new_population_year_three + additional_population
new_population_year_five = new_population_year_four + additional_population

print(f"The popultion for the next {years} years are  {new_population_year_one}, {new_population_year_two}, {new_population_year_three}, {new_population_year_four}, {new_population_year_five}")

