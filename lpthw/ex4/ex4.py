cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# cars_not_driven = cars = 100 - drivers = 30
cars_not_driven = cars - drivers
# cars_driven = drivers = 30
cars_driven = drivers
# carpool_capacity = 30 * 4.0 = 120.0 (floating number)
carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = 90 / 30
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
