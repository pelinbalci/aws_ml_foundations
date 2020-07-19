# https://www.python-course.eu/python3_properties.php
# I've changed the variable names.


class Property:
    def __init__(self, build_year_value, potential):
        # initializing the attribute
        self.build_year = build_year_value
        self.potential = potential

    @property
    def calculate_condition(self):
        if self.potential <= -1:
            return "I feel miserable!"
        elif self.potential <= 0:
            return "I feel bad!"
        elif self.potential <= 0.5:
            return "Could be worse!"
        elif self.potential <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"

    @property
    def change_build_year(self):
        if self.build_year < 0:
            self.build_year = 2000
        else:
            self.build_year = 2020
        return self.build_year


new_object = Property(-1300, 0.2)

print(new_object.calculate_condition)
print(new_object.change_build_year)

# Output:
# Could be worse!
# 2000
