from random import *

wives = ["Emma Watson", "Scarlet Johansson", "Rihanna"]
country = ["Russia", "Japan", "Spain"]
house = ["mansion", "trailer", "boathouse"]
car = ["ferrari", "bentley", "maserati"]

WifeInput = raw_input("Who is your wife?")
CountryInput = raw_input("Where do you live?")
HouseInput = raw_input("What do you live in?")

print("You will marry", choice(wives))
print("You will live in the country of", choice(country))
print("You will live in a", choice(house))
print("Your car will be a", choice(car))
print("congratulations")