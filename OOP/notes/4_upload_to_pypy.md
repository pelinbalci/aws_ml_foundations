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

Be in the right directory: 

    cd binomial_package_files
    
This command will create 2 new folders: dist & bg_dist.egg-info

    python setup.py sdist
   
In the dist folder there is tar.gz ---> The .tar.gz file is called a source archive.

If you haven't installed twine yet:    

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



# More Info

Ref: https://classroom.udacity.com/courses/ud090/lessons/55951aa6-a28f-4642-a9b4-f9ea92a825ec/concepts/2b79b827-2756-41bb-9b43-fe3430b6d7d8
The new version of upload is: 

    python3 setup.py sdist bdist_wheel
    
The difference is that you will get both a .tar.gz file and a .whl file. 
The .whl file is a built distribution. The .whl file is a newer type of installation file for Python packages. 
When you pip install a package, pip will first look for a whl file (wheel file) and if there isn't one, will then look 
for the tar.gz file. 

A tar.gz file, ie an sdist, contains the files needed to compile and install a Python package. A whl file, 
ie a built distribution, only needs to be copied to the proper place for installation. 
Behind the scenes, pip installing a whl file has fewer steps than a tar.gz file.
