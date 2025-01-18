with open('26_4660.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)

every_4 = prices[3::4]
client_prices = sum(prices) - sum(every_4) + sum(every_4) /2
shop_price = sum(prices[:3 * N // 4]) + sum(prices[3 * N // 4:]) / 2

print(client_prices, shop_price)

