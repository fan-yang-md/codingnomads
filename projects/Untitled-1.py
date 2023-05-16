#This is a small project to get yourself warmed up and keep training your newly found skills in 
#collecting user input and formatting strings.

#Create a Python script that asks a user questions in the command line. The script should follow 
#the outlined specifications.

#Specifications
#Receive the following arguments from the user:

#Kilometers to drive
#Liters-per-kilometer usage of the car
#Price per liter of fuel
#Calculate the cost of the trip and display it to the user in the console. 
#Apply some of the string formatting tricks that you learned about in this course section.

km = float(input("distance in km: "))
lpk = float(input("fuel efficiency in LPK: "))
price = float(input("fuel price per liter: "))

cost = km/lpk*price 
print(f"total fuel cost of the trip is: {cost}")