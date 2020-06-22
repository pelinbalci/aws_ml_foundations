Ref: https://classroom.udacity.com/courses/ud090/lessons/55951aa6-a28f-4642-a9b4-f9ea92a825ec/concepts/0f6e02e6-13bd-498c-9297-1afdef89e909

# Making a package

Example package is [here]()

There are distribution package and setup.py file. 

### Distribution package

In distribution python package; there are general distribution, gaussian distribution and an init file. 
We added this line to init file: 

    from .Gaussiandistribution import Gaussian

Why?

- If we DIDN'T include any CODE in the `init ` file the package would still WORK.
- But any program that uses this package should import Gaussian class indirectly.


    from distributions import Gaussian 

Now; by adding a line to init file, we're making a shortcut.

### Setup.py

It is necessary for pip installing.

- pip will look this file.  
- it contains info and metadata about the package.
    - name, version, description, packages, zip_safe etc. 


### Install the package

- Make sure that you are in the same directory with setup.py file.
- Terminal :

``
    pip install .
``

- " . " tells pip to look for setup file. 
- Then package is installed. 

- Open terminal. Your directory can be different than setup file. Or open a new .py file anywhere under this env.
- type: 
`
    from distributions import Gaussian
`    

- You can use it now :)

### Where is this package installed?

In python console:

    import distributions
    distributions.__file__
    
Mine is here: '/Users/pelin.balci/.conda/envs/aws_ml_foundations/lib/python3.7/site-packages/distributions_example/__init__.py'
    
### What if you update the code?

You should reinstall the package:

    pip install --upgrade .

# What is pip?

Pip is a Python package manager that helps with installing and uninstalling Python packages.


# More info

A Python package does not need to use object-oriented programming. 

You could simply have a Python module with a set of functions. 

- Object-oriented programs are relatively easy to expand especially because of inheritance
- Object-oriented programs obscure functionality from the user. Consider scipy packages. 
You don't need to know how the actual code works in order to use its classes and methods.
