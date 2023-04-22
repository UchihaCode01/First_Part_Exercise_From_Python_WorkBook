
total_sum = 0  # I am creating a variable for the total sum
cash_sum = 0  # I am creating a variable for the amount that needs to be paid in cash

while True:  # Here I am creating an infinite loop

    # Here I am asking the user for the price
    message = input("Enter the price : ")

    if not message:  # Here I am saying that if the input is empty, then the infinite loop should be stopped
        break

    # Here I am saying that the variable is equal to the input converted to a float
    price = float(message)
    # Here I am saying that the variable for the total sum is equal to the variable with the float
    total_sum += price
    # Here I am saying that the variable is equal to the sum * 100, in order to convert the entire sum into cents
    cash_sum += round(price * 100)

# Here I am asking to print the value of the total sum to the screen
print("The total sum in the shop is : ", total_sum)

# Here I divide the total sum in cents by 5, then multiply by 5, and round the result
cash_rounded = round(cash_sum / 5) * 5
# Here I declare a new variable in which I divide the rounded result by 100
cash = cash_rounded / 100

# Here I ask to display the value of cash payment on the screen
print("The cash sum in the shop is : ", cash)
