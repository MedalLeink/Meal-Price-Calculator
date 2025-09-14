"""
Project: Meal Price Calculator
Author: Madeleine Nkiru

Description: A program to calculate the total cost of a meal, including tax and change.
"""

# Ask the user for the child and adult meal
child_meal = float(input("\nWhat is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))

# Ask the user for the number of adults and children 
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))


# Determine and display the subtotal 
subtotal = (number_of_children * child_meal) + (number_of_adults * adult_meal)

print(f"\nSubtotal: ${subtotal:.2f}")

# Ask the user for the sales tax rate as a percentage 
sales_tax_rate = float(input("\nWhat is the sales tax rate?: "))

# Compute and display the sales tax 
sales_tax = (subtotal * sales_tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")


# Compute and display the total 
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")


# Ask for the the payment amount 
payment_amount = float(input("\nWhat is the payment amount? "))

# Compute and display the change 
change = payment_amount - total
print(f"Change: ${change:.2f}")