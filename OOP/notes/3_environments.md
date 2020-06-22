
# Conda, Venv, Pip

- Conda does two things: manages packages and manages environments.

- Venv is an environment manager

- Pip can only manage Python packages

- Conda was invented because pip could not handle data science packages that depended on libraries outside of Python.

Read this: https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/#Myth-#5:-conda-doesn't-work-with-virtualenv,-so-it's-useless-for-my-workflow


# Which to choose?

- Conda is very helpful for data science projects, but conda can make generic Python software development a bit more confusing

- If you CREATE a CONDA ENVIRONMENT, ACTIVATE the ENVIRONMENT, and THEN INSTALL INSTALL the distributions package, 
you'll find that the system installs your package globally rather than in your LOCAL CONDA ENVIRONMENT.

-  if you CREATE the CONDA ENVIRONMENT and INSTALL INSTALL SIMULTANEOUSLY, you'll find that 
pip behaves as expected installing packages into your LOCAL ENVIRONMENT.

- using pip with venv works as expected. 

