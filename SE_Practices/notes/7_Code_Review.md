# Code Review

- Catch errors
- Ensure readability
- Check standarts are met
- Share knowledge

Ideally, a ds code reviewed by another ds. 

************* 
Ref: https://github.com/lyst/MakingLyst/tree/master/code-reviews
- PR description: It should explain both why you are making this change and what you changed.
- You shouldn't put off code review for more than a few hours. Never more than a day.
- you should expect to spend some time every day doing reviews and that you will probably need to spend 2-3 sessions per day replying to PRs and reading other people's code.

Things to look for: 

`Clarity`
Things should be named well and should be easy to follow when reading. The code should attempt to be self documenting.

`Correctness`
There must be unit tests. They should test the edge cases. The code should behave as the submitter described. The code should use other APIs correctly.

`Security`
The design should not introduce any security problems such as potential denial of service attacks or unintended information disclosures. In particular we should be aware of potential CSRF and XSS attacks.

`Performance`
The code should perform within our targets for a particular area. It should not use obviously suboptimal algorithms. However optimisation is usually best left to later. Except when it can also improve other areas at the same time. Simpler code is often faster.

************* 

Another ref: https://www.kevinlondon.com/2015/05/05/code-review-best-practices.html

# Tips

Use pylint in terminal: `pylint path_of_py`

Rather than commanding people to change their code a specific way because it's better, it will go a long way to explain 
to them the consequences of the current code and suggest changes to improve it

    BAD: Make model evaluation code its own module - too repetitive.
    BETTER: Make the model evaluation code its own module. This will simplify models.py to be less repetitive and focus 
    primarily on building models.
    GOOD: How about we consider making the model evaluation code its own module? This would simplify models.py to only 
    include code for building models. Organizing these evaluations methods into separate functions would also allow us to reuse them with different models without repeating code.



Is the code clean and modular?

    Can I understand the code easily?
    Does it use meaningful names and whitespace?
    Is there duplicated code?
    Can you provide another layer of abstraction?
    Is each function and module necessary?
    Is each function or module too long?
    
Is the code efficient?

    Are there loops or other steps we can vectorize?
    Can we use better data structures to optimize any steps?
    Can we shorten the number of calculations needed for any steps?
    Can we use generators or multiprocessing to optimize any steps?
    Is documentation effective?
    Are in-line comments concise and meaningful?
    
Is there complex code that's missing documentation?

    Do function use effective docstrings?
    Is the necessary project documentation provided?
    
Is the code well tested?

    Does the code high test coverage?
    Do tests check for interesting cases?
    Are the tests readable?
    Can the tests be made more efficient?
    
Is the logging effective?

    Are log messages clear, concise, and professional?
    Do they include all relevant and useful information?
    Do they use the appropriate logging level?

