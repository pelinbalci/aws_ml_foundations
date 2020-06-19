# https://www.python-course.eu/python3_properties.php
# I've changed the variable names.


class Property:
    def __init__(self, build_year_value, potential):
        # initializing the attribute
        self.build_year = build_year_value
        self.potential = potential

    @property
    def calculate_condition(self):
        condition = self.potential
        if condition <= -1:
            return "I feel miserable!"
        elif condition <= 0:
            return "I feel bad!"
        elif condition <= 0.5:
            return "Could be worse!"
        elif condition <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"

    @property
    def build_year(self):
        return self.__build_year

    # the attribute name and the method name must be same
    @build_year.setter
    def build_year(self, build_year_value):
        if build_year_value < 0:
            self.__build_year = 2000
        else:
            self.__build_year = 2020


new_object = Property(-1300, 0.2)

print(new_object.calculate_condition)
print(new_object.build_year)

# Output:
# Could be worse!
# 2000
