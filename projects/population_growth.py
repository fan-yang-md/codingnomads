#The current population is 380,123,456
#One person is born every 6 seconds
#One person dies every 12 seconds
#One person immigrates every 40 seconds
#Write the necessary code to display the total population count for the next 3 years (without a leap year).

current_population = 380123456
three_years_in_seconds = 365*24*60*60
growth = three_years_in_seconds/6 - three_years_in_seconds/12 + three_years_in_seconds/40
year_1 = current_population + growth
year_2 = year_1 + growth
year_3 = year_2 + growth
print("year 1 population: " + str(year_1))
print("year 2 population: " + str(year_2))
print("year 3 population: " + str(year_3))
