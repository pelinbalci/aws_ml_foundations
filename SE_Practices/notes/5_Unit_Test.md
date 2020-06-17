# Testing
Testing your code is essential before deployment. 
It helps you catch errors and faulty conclusions before they make any major impact. 

Today, employers are looking for data scientists with the skills to properly prepare their code for an industry setting, 
which includes testing their code.

Problems that could occur in data science aren’t always easily detectable:
- bad encoding
- features being used inappropriately
- unexpected features

To catch these errors, you have to check:
- the quality and accuracy of your analysis
- the quality of your code

Solution: Test Driven Development =)

UNIT TEST: a type of test that covers a “unit” of code, usually a single function, 
independently from the rest of the program.

We will learn:
- write unit tests
- tools to imrpve unit tests
- tests specifically for data science

Passing unit tests isn’t always enough to prove that our program is working successfully. 
To show that all the parts of our program work with each other properly, communicating and transferring 
data between them correctly, we use `integration` tests.


# Test Driven Implementation

Write test before you write the code being tested. 

First decide the function and its parameters:

    def email_validator(email):
        pass

Write the test function, our expectations from the function:

    def test_email_validator():
        assert email_validator('pelin@email.com') == True
        assert email_validator('pelin@email@.com') == False
        assert email_validator('pelin.com') == False
        
Start implementing your function:

    def email_validator(email):
        if email.count('@') == 1 and email.count('.') == 1:
            return True
        else:
            return False
            
If test passes, our implementation is done =)


TDD in DS: 
Ref: https://engineering.pivotal.io/post/test-driven-development-for-data-science/
'Test driving all the features and algorithms stringently during the exploratory phase is an overkill. 
We felt we were investing a lot of time in throw-away work. TDD made the exploration phase quite intensive and slowed us
 considerably. Eventually we found a fine balance between TDD and DS.

After the exploratory phase, once we have figured out which model and features suits the use case the best, we actually 
start test driving feature generation, model development and integration bits. Our model evaluation from the exploratory
 phase helps us set expectations around the model’s performance. We leverage this information in our TDD to make sure 
 the model is behaving as expected in production.'


