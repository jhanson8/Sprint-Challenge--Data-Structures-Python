import time
from collections import Counter
from doubly_linked_list import DoublyLinkedList as dll
from binary_search_tree import BSTNode as bst 


start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#quadratic (On^c) 
'''for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)'''

#set method takes in an iterable list, string tuple, etc. Outputs as object { }
#intersection method takes in a list and compares to another list and returns an object with of all of the common elements between the two lists  

'''d = set(names_1).intersection(names_2)
for i in d: 
    duplicates.append(i)'''

'''for i in [x for x in names_1 if x in names_2]:
    duplicates.append(i)'''

#bst data structure 
bst = bst(names_1[0])
for x in names_1:
    bst.insert(x)
for i in names_2:
    if bst.contains(i):
        duplicates.append(i)
print(len(duplicates))

#doubly
'''
d = dll(names_1[0])
for x in names_1:
    d.add_to_head(x)

for i in names_2:
    if d.contains(i):
        duplicates.append(i)'''



    





end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
