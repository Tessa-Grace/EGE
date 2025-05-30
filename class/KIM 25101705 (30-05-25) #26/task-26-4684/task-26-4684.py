with open('26_4684.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices)
store = sum(prices) - sum(prices[:N // 6]) / 2

prices = sorted(prices, reverse=True)
cust = sum(prices) - sum(prices[5::6]) / 2

print(cust, store)

# otvet: 46201709 49699604