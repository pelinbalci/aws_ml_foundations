# # Optimizing Code: Common Books
# Here's the code your coworker wrote to find the common book ids in `books_published_last_two_years.txt` and
# `all_coding_books.txt` to obtain a list of recent coding books.

import time
import pandas as pd
import numpy as np

with open('books_published_last_two_years.txt') as f:
    recent_books = f.read().split('\n')
    
with open('all_coding_books.txt') as f:
    coding_books = f.read().split('\n')

start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# "96\n",
# "Duration: 17.357314348220825 seconds\n"


# new_list = [value for value in list1 if value in list2]
start = time.time()
recent_coding_books = [value for value in recent_books if value in coding_books] 
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# "96\n",
# "Duration: 17.27001690864563 seconds\n"

# In[12]:


# new_list = [value for value in set(list1) if value in set(list2)]
start = time.time()
recent_coding_books = [value for value in set(recent_books) if value in set(coding_books)] 
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# "96\n",
# "Duration: 46.82951021194458 seconds\n"


# new_list = list(set(list1) & set(list2))
start = time.time()
recent_coding_books = list(set(recent_books) & set(coding_books)) # TODO: compute intersection of lists
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# "96\n"
# "Duration: 0.014384746551513672 seconds\n"


# new_list = set(lst1).intersection(lst2)
start = time.time()
recent_coding_books = set(recent_books).intersection(set(coding_books)) # TODO: compute intersection of lists
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# "96\n",
# "Duration: 0.012008905410766602 seconds\n"


# ### Tip #1: Use vector operations over loops when possible
# Use numpy's `intersect1d` method to get the intersection of the `recent_books` and `coding_books` arrays.

start = time.time()
recent_coding_books = np.intersect1d(recent_books, coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# "96\n",
# "Duration: 0.0385744571685791 seconds\n"


# ### Tip #2: Know your data structures and which methods are faster
# Use the set's `intersection` method to get the common elements in `recent_books` and `coding_books`.

start = time.time()
recent_coding_books = set(recent_books).intersection(coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
# "96\n",
# "Duration: 0.009184837341308594 seconds\n"

