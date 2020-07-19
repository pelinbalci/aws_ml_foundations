class Shirt:

    def __init__(self, color='defualt', size='default', price=0, cost=0):

        self.color = color
        self.size = size
        self.price = price
        self.cost = cost

    def calculate_profit(self):
        profit = self.price - self.cost
        return profit

    def __repr__(self):
        return '{} color, {} size shirt, the price of the shirt {}, cost of the shirt {}'.format(self.color, self.size, self.price, self.cost)

    def __add__(self, other):

        total = Shirt()
        total.price = self.price + other.price
        total.cost = self.cost + other.cost
        return total

    def __sub__(self, other):
        subtract = Shirt()
        subtract.price = self.price - other.price
        subtract.cost = self.cost - other.cost
        return subtract


shirt_1 = Shirt('red', 'L', 1, 3)
shirt_2 = Shirt('blue', 'M', 30, 10)

shirt_sum = shirt_1 + shirt_2
subtract = shirt_1 - shirt_2


print(str(shirt_1))
print(str(shirt_2))

print(str(shirt_sum))
print(str(subtract))

