"""
Project: Meal Price Calculator
Author: Madeleine Nkiru

Description: To calculate the price of meal.
"""

# Ask the user for the following info 
child_meal = float(input("What is the price of a child's meal?: "))
adult_meal = float(input("What is the price of an adult's meal?: "))
number_of_children = int(input("What is the number of children?: "))
number_of_adults = int(input("What is the number of adults?: "))


# Determine the meal's subtotal 
children_meal_subtotal = number_of_children * child_meal
adult_meal_subtotal = number_of_adults * adult_meal

# Display the subtotal 
subtotal = children_meal_subtotal +adult_meal_subtotal

# Ask the user for the sales tax rate as a percentage 