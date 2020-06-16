### Without using version control system:

What combinations and parameters did I use? 

I saw a better accuracy I'm sure about that! 

Where are they?! =(


### Git

You can work on a project as a team thanks to Git :)

Example:

Commits in a branch called `friend_groups`

    git commit -m "regularization rate: 0.01, 128 - 64 nodes, cv: 0.92"
    git commit -m "regularization rate: 0.03, 128 nodes, cv: 0.85"

Find commits with `git log`

Checkout a commit

    git checkout regularization rate: 0.01, 128 - 64 nodes, cv: 0.92


you’re pretty confident merging this back into the development branch, and pushing the updated recommendation engine.

Switch to develop branch

    git checkout develop

Merge friend_groups branch to develop
    
    git merge --no-ff friend_groups

Push changes to remote repository
    
    git push origin develop

https://algorithmia.com/blog/how-to-version-control-your-production-machine-learning-models

In addition to the often perplexing nature of using the actual protocol, 
its missing a lot of the functionality that you need for machine learning (because it wasn’t created for ML!).

Git itself doesn’t allow you to track data, changes to model files, and model dependencies. 

There are extensions that can help, but those solutions are tough to implement and rarely complete.
    

### Jupyter 

When it comes to deployment and production though, versioning your models in a notebook doesn’t really cut it. 

Jupyter Notebooks are a tool for `exploration` and `visualization, `  NOT for managing dependencies and tracking minute 
changes to hyperparameters.


### DVC

Ref: https://algorithmia.com/blog/how-to-version-control-your-production-machine-learning-models

Data Version Control (DVC) is a Git extension that adds functionality for managing your code and data together. 

It works directly with cloud storage (AWS S3 or Google GCP) to push your data changes. 

For example, according to their tutorial:
 
        “DVC streamlines large data files and binary models into a single Git environment and 
        this approach will not require storing binary files in your Git repository.” 
        
        
It’s a streamlined version of combining Git with machine learning specific functionality for data management.

Useful Links:
- https://github.com/iterative/dvc
- https://becominghuman.ai/how-to-version-control-your-machine-learning-task-ii-d37da60ef570
- https://www.kdnuggets.com/2017/05/data-version-control-iterative-machine-learning.html
    
    
### How to use DVC:
Ref: https://becominghuman.ai/how-to-version-control-your-machine-learning-task-ii-d37da60ef570

" Steps:
- First initialize a git repo and put the downloaded code there.

        $ mkdir numerai_code #create a repo
        $ cd numerai_code
        $ git init # initialize git
        $ git add numerai_code_downloaded # Add downloaded data to git repo
        $ git commit -m 'Numerai code added'
        $ git push
    
- Install and Initialize DVC repository

        $ pip install dvc
        $ dvc init
        
Now, the time is to create a prediction model that predicts the data based on the dataset available and 
then put that file in the same repository (numerai_code) as above. 

Let’s call it ‘prediction.py’

For the prediction model, I used an LSTM (Long Short Term Memory) Recurrent Neural Networks in Python with Keras.

- Run the python code within dvc with the following command:

        $ dvc run python prediction.py

- The model saves the checkpoints in a CSV file with the name assigned and the saved CSV can be submitted on the 
Numerai submission page. "

