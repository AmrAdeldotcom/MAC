# Great! We now want to create a new list that contains the counts
# of all occurrances of every number seen in the randomly generated 
# list. That means we want counts of all occurrences of all numbers
# from 0 through 10 in our randomly generated list.

# Let's store our counts in a list of length 11 
# with zeros filled in.

# We can multiply a list construct to create a list with the same
# elements n number of times.
count_list = [0] * 11

# Check that we have a list of length 11 with all 0 elements
print count_list

# We use this list to store our count of numbers 0 to 10 - take note 
# that total numbers 0 to 10 is 11. We can use the index number of
# each element to refer to the count of our target
# number. Our target number is actually the index of the list.
# For example, assume count_list looks like this:

count_list = [1,2,3,2,2,1,1,2,3,1,2]

# Let's print out the occurrences for the numbers 0, 4, 5, and 6
print count_list[0]
print count_list[4]
print count_list[5]
print count_list[6]

# Therefore, for our output, we want a count_list that looks like:
# [1,2,3,2,2,1,1,2,3,1,2]

# Here's our code that we coded before

import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))
# --------------------------------------------------------------------

# Initialize count_list for every integer between 0 and 10. 
# A number will correspond to an index of this count_list
# Therefore if we see that there are 3 occurrences of the number 4, 
# we assign count_list[4] = 3, if there are 5 occurrences of the 
# number 6, we assign count_list[6] = 5

count_list = [0] * 11
index = 0

# Write code here to loop through every number in random_list and
# update count_list appropriately
i=0
while i < 11:
    c=0
    for n in random_list:
        if n == i:
            c +=1
    count_list[i] = c
    i += 1

'''
#This answer by instructor
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0
count = 0

while index < len(random_list):
  number = random_list[index]
  count_list[number] = count_list[number] + 1
  index = index + 1
'''
# Check the list we created
print count_list
# If we coded everything correctly, the sum of all of the numbers 
# in count_list should be 20
print sum(count_list)
