with open('26_4660.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)

cust = sum(prices) - sum(prices[::4]) / 2
store = sum(prices) - sum(prices[-N // 4:]) / 2

print(cust, store)

# otvet: 44097776 48825239