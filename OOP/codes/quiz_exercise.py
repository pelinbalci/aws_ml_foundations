"""
Write a Pants class with the following characteristics:

the class name should be Pants
the class attributes should include
color
waist_size
length
price
the class should have an init function that initializes all of the attributes
the class should have two methods
change_price() a method to change the price attribute
discount() to calculate a discount

Write a SalesPerson class with the following characteristics:

the class name should be SalesPerson
the class attributes should include:
first_name
last_name
employee_id
salary
pants_sold
total_sales

the class should have an init function that initializes all of the attributes

the class should have four methods:
sell_pants() a method to change the price attribute
calculate_sales() a method to calculate the sales
display_sales() a method to print out all the pants sold with nice formatting
calculate_commission() a method to calculate the salesperson commission based on total sales and a percentage
"""


class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount_ratio):
        return self.price * (1-discount_ratio)


def check_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12

    pants.change_price(10) == 10
    assert pants.price == 10

    assert pants.discount(.1) == 9

    print('You made it to the end of the check. Nice job!')


check_results()


class SalesPerson:

    def __init__(self, first_name, last_name, employee_id, salary, pants_sold=[], total_sales=0):

        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = pants_sold
        self.total_sales = total_sales

    def sell_pants(self, pants_object):
        """The sell_pants method appends a pants object to the pants_sold attribute

        Args: pants_object (obj): a pants object that was sold

        Returns: None
        """
        return self.pants_sold.append(pants_object)

    def display_sales(self):
        """The display_sales method prints out all pants that have been sold

        Args: None

        Returns: None
        """
        for pants in self.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}' \
                  .format(pants.color, pants.waist_size, pants.length, pants.price))

    def calculate_sales(self):
        """
        The method should iterate through the pants_sold attribute list and sum the prices of the pants sold.
        The sum should be stored in the total_sales attribute.

        Args: None

        Returns: total_sales
        """
        total_sales = 0
        for pants in self.pants_sold:
            total_sales += pants.price
        return total_sales

    def calculate_commission(self, commision_percentage):

        '''
        sales_total = self.pants_sold()
        return sales_total * percentage
        The calculate_commission method outputs the commission based on sales

        Args:
            commision_percentage : a decimal representing th amount of commission

        Returns: commission
        '''

        commission = 0
        for pants in self.pants_sold:
            commission += pants.price*commision_percentage
        return commission


pants_obj_1 = Pants('red', 'M', 10, 100)
pants_obj_2 = Pants('red', 'S', 10, 130)
pants_obj_3 = Pants('blue', 'S', 10, 120)
employee_1 = SalesPerson('pelin', 'balci', '465', '1000', [], 0)

employee_1.sell_pants(pants_obj_1)
employee_1.sell_pants(pants_obj_2)
employee_1.display_sales()

total_sales = employee_1.calculate_sales()
print('total sales is ', total_sales)
print('employee_1 comission', employee_1.calculate_commission(0.1))


def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)

    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0

    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color

    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)

    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(), 2) == 47.36
    assert round(salesperson.calculate_commission(.1), 2) == 4.74

    print('Great job, you made it to the end of the code checks!')


check_results()
