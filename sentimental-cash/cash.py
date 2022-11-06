# TODO

from cs50 import get_float


def get_change():
    while True:
        n = get_float("Change owed: ")
        if n > 0:
            break
    return n


def main():
    cash = get_change() * 100

# Calculate the number of quarters to give the customer
    quarters = cash / 25
    cash = cash - int(quarters) * 25

#   // Calculate the number of dimes to give the customer
    dimes = cash / 10
    cash = cash - int(dimes) * 10

#   // Calculate the number of nickels to give the customer
    nickels = cash / 5
    cash = cash - int(nickels) * 5

#   // Calculate the number of pennies to give the customer
    pennies = cash / 1
    cash = cash - int(pennies) * 1

#   // Sum coins
    coins = int(quarters) + int(dimes) + int(nickels) + int(pennies)

#   // Print total number of coins to give the customer
    print(coins)


main()

