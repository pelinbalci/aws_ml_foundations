#https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556

import logging


class LoggerMixin(object):
    @property
    def logger(self):
        name = '.'.join([
            self.__module__,
            self.__class__.__name__
        ])
        logging.getLogger().setLevel(logging.DEBUG)
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        return logging.getLogger(name)


class Shipping(LoggerMixin):

    def __init__(self, sales_price, variable_cost, quantity):
        self.logger.info('Shipping initializing')

        self.sales_price = sales_price
        self.variable_cost = variable_cost
        self.quantity = quantity

    def calculate_profit(self):
        profit = self.quantity * (self.sales_price - self.variable_cost)
        return profit


class Production(Shipping, LoggerMixin):

    def __init__(self, sales_price, variable_cost, quantity, type):

        Shipping.__init__(self, sales_price, variable_cost, quantity)

        self.type = type
        self.logger.info('production initializing')

    def calculate_comission(self, comission):
        self.logger.info('Calculating commissions')
        return self.calculate_profit() * comission


shipping_object = Shipping(100, 5, 1000)
print(shipping_object.calculate_profit())

production_object = Production(100, 5, 1000, 'truck')
comission = production_object.calculate_comission(0.3)
print(comission)
