# Object Oriented Programming - OOP

Ref: https://classroom.udacity.com/courses/ud090/lessons/55951aa6-a28f-4642-a9b4-f9ea92a825ec/concepts/9a937f8b-efd3-4381-ada2-1ffd5382ec93

- class - a blueprint consisting of methods and attributes
- object - an instance of a class. ex: a yellow pencil, a small dog
- attribute - a descriptor or characteristic. ex: blue, 3 inches 
- method - an action that a class or object could take
- encapsulation - you can combine functions and data all into a single entity. In object-oriented programming, 
this single entity is called a class.  


Example: 

    Object: Stephen Hawking, Brad Pitt
    Class: Scientist, Actor
    Attribute: Color, Size, Shape 
    Method: To rain, To sing
    Value: Gray, Large
    
Example2:

    A shirt has its own color (yellow) and size (S)
    A shirt (magically :)) can change its price. 
    
    Shirt is an object.
    
    It has attributes (color and size) and method-action (change price)
    It has values for attributes. 
    
    If you describe the requirements of shirt with attributes and methods;
    this is your class. 
    
    
# Writing Class:

[code](https://github.com/pelinbalci/aws_ml_foundations/blob/master/OOP/codes/shirt_example.py)

- Capitalize the first letter in class name. use () or not.
- 'self' stores your attributes, colors, size etc. --> makes those attributes available throughout your class.
- 'self' is a dictionary that holds your attributes and attributes values.
- if you want to access these attributes, self will be the first input to the functions.
- change price doesn't return anything. It only changes the value of price attribute.
- discount method returns discounted price.
- you can't reach object name ; for example shirt_1.
- you can change the attributes directly: shirt_1.color = 'black' Try not to use this way.
- Read more: https://www.python-course.eu/python3_properties.php

    
# Right way of using docstrings:

    class Pants:
        """The Pants class represents an article of clothing sold in a store
        """
    
        def __init__(self, color, waist_size, length, price):
            """Method for initializing a Pants object
    
            Args: 
                color (str)
                waist_size (int)
                length (int)
                price (float)
    
            Attributes:
                color (str): color of a pants object
                waist_size (str): waist size of a pants object
                length (str): length of a pants object
                price (float): price of a pants object
            """
    
            self.color = color
            self.waist_size = waist_size
            self.length = length
            self.price = price
    
        def change_price(self, new_price):
            """The change_price method changes the price attribute of a pants object
    
            Args: 
                new_price (float): the new price of the pants object
    
            Returns: None
    
            """
            self.price = new_price
            
        def discount(self, discount_rate):
            """ This method uses discount rate to calculate discounted price of a pants object
            
            Args:
                discount_rate (float): a decimal representing the amount to discount
                
            Returns: discounted_price
            """   
            return self.price * (1 - percentage)
        