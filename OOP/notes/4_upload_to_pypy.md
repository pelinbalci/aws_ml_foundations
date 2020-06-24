# Upload to pypy

Register to: https://test.pypi.org/

Create the package toy would like to upload. 

It should include these files: 

    Package
        |___ package_name <bg_distributions>
            |___  __init__.py
            |___  README.md
            |___  licence.txt
            |___  setup.gcf
            |___  binomial_distribution.py
            |___  generaldistribution.py
            
        |___ __init__.py
        
        |___ setup.py
        
## Licence

You can use the licence here: https://opensource.org/licenses/MIT

## README.md

It can include: Summary, Files, Installation

## Setup.py

    from setuptools import setup
    
    setup(name='bg_distributions',
          version='0.1.0',
          description='Gaussian and Binomial distributions',
          packages=['bg_distributions'],
          author='Pelin Balci',
          zip_safe=False)


Initialize version: https://stackoverflow.com/questions/3728626/what-to-use-as-an-initial-version

Why is zip_safe false?

Because it means that the package can't ve run directly from a zip file. 

name is the same as the folder name. 


## Terminal Commands

    cd binomial_package_files
    python setup.py sdist
    pip install twine


commands to upload to the pypi test repository

    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    
Now it is published :)

how to install your package ? 

    pip install --index-url https://test.pypi.org/simple/ bg-dist

command to upload to the pypi repository

    twine upload dist/*
    pip install bg-dist
    

While pip installing use -, but in python console you need to use _.

⭐⭐️⭐

You can find the uploaded package [here](https://github.com/pelinbalci/aws_ml_foundations/blob/master/OOP/binomial_package_files/)
I've tried to use it, you can find just a small example [here](https://github.com/pelinbalci/aws_ml_foundations/blob/master/OOP/try_binomial_package/)

⭐⭐️⭐️ ️And here is my first package =) https://pypi.org/project/bg-dist/ ⭐️⭐️⭐️

