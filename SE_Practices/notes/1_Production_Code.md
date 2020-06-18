#### Production Code

Ref: https://classroom.udacity.com/courses/ud090/lessons/ac47b924-72d3-4bf9-971c-bfccfa368b02/concepts/ca9168f7-0405-41f8-b392-db1e77201880

Production code == Code run on production servers

It should be Clean and Modular. 

⭐Clean: 

Readable, simple, concise

⭐Modular: 

Logically broken up into functions and modules. It allows you to collaborate, write less code, read the code, reuse it. 
Modular code is organized and efficient. 

Modules allow code to be reused by ENCAPSULATING them into files.

⭐MODULAR CODE:
- Functions: 

        def my_func(x,y): 
            result = do_sth(x,y)
            return result

- Modules:

      my_module.py
      
      
#### Refactoring

After you've achieved a working model, go back and do refactoring. 

⭐️Refactoring : Improve its internal structure w/o changing its external functionality.

- reduce workload in long run
- easier to maintain your code
- reuse
- become a better developer =)

⭐DRY PRINCIPLE : DON'T REPEAT YOURSELF.


#### Two important Factor

-Reduce the run time
-Reduce the space in memory

If you run the code once in every week, it is ok that it takes a minute to run. 
But it is inefficient time for Twitter. It should be fed instantaneously.


#### Lists & Sets

*******************

https://stackoverflow.com/questions/8929284/what-makes-sets-faster-than-lists/8929445#8929445

list: 

Imagine you are looking for your socks in your closet, 
but you don't know in which drawer your socks are, 
so you have to search drawer by drawer until you find them (or maybe you never do). 

That's what we call O(n), because in the worst scenario, you will look in all your drawers 
(where n is the number of drawers).

set: 

Now, imagine you're still looking for your socks in your closet, 
but now you know in which drawer your socks are, say in the 3rd drawer. 

So, you will just search in the 3rd drawer, instead of searching in all drawers. 

That's what we call O(1), because in the worst scenario you will look in just one drawer.

*******************