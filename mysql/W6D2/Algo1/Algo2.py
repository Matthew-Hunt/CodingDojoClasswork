# Generate Coin Change
# Change is inevitable (especially when breaking a twenty).
# Make generateCoinChange(cents). Accept a number of American cents,
# compute and print how to represent that amount with the smallest number of coins.
# Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).

# Example output, given (87):

def generateCoinChange(cents):
    coins = [25, 10, 5, 1]
    coin_names = ['quarter', 'dime', 'nickel', 'penny']
    change = []
    for i in range(len(coins)):
        num = cents // coins[i]
        cents -= num * coins[i]
        if num > 0:
            if num == 1:
                change.append(str(num) + ' ' + coin_names[i])
            else:
                change.append(str(num) + ' ' + coin_names[i] + 's')
    return(' '.join(change))

print(generateCoinChange(87))