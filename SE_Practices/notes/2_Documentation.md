#### Documentation


Additional text or illustrated information that comes with or is embedded in the code of software.

Helpful for clarifying complex parts of code, making your code easier to navigate, and quickly conveying how and 
why different components of your program are used.

Several types of documentation can be added at different levels of your program:
- In-line Comments - line level
- Docstrings - module and function level
- Project Documentation - project level
    
#### In-line comments:

In-line comments are text following hash symbols throughout your code. 

They are used to explain parts of your code, and really help future contributors understand your work.
 
Comments are valuable for explaining where code cannot. For example, the history behind why a certain method was 
implemented a specific way.

#### Docstrings

Docstrings and inline comments are NOT interchangeble!

Docstring, or documentation strings, are valuable pieces of documentation that explain the functionality of any FUNCTION
or MODULE in your code. 

Ideally, each of your functions should always have a docstring.⭐️

Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose.

Ex: 

    def population_density(population, land_area):
        """Calculate the population density of an area."""
        return population / land_area

   
    def population_density(population, land_area):
        """Calculate the population density of an area.
    
        Args:
        population: int. The population of the area
        land_area: int or float. This function is unit-agnostic, if you pass in values in terms of square km or square miles the function will return a density in those units.
    
        Returns:
        population_density: population/land_area. The population density of a 
        particular area.
        """
        return population / land_area

   
    def foo():
        """A multi-line
        docstring.
        """

    def bar():
        """
        A multi-line
        docstring.
        """
        
#### Project Documentation

Whether it's an application or a package, your project should absolutely come with a README file. 

At a minimum, this should explain what it does, list its dependencies, 
and provide sufficiently detailed instructions on how to use it. 
    
#### Read Me

https://classroom.udacity.com/courses/ud777/lessons/5338568539/concepts/53317786070923

- Start with a header of the project and description. You can add a logo here.

- Installation  instructions, initial setups. 

- Common usages 

- Known bugs.

Ask the questions yourself: 

1. what steps need to be taken?
2. What should the user already have installed or configured?
3. What might they have hard time understanding right away?


Including a COPYRIGHT or licencing information or a link to it is ALWAYS a GOOD IDEA. 

If you want others to contribute your project, you can add the licence in readme file. 
And you can add a Contribution Section in order to give details.
