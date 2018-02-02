# We now would like to summarize this data and make it more visually appealing
# We want to go through count_list and print a table that shows the number and its 
# corresponding count.

# The output should look like this neatly formatted table:
"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""
# Here is our code we have written so far:

import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

# Aggregate the data -------------------------------------------------
count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1
    
# Write code here to summarize count_list and print a neatly formatted table that looks
# like this:

"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""

# Hint: To print 10 blank spaces in a row, we can multiply a string by a number "n"
# to print this string n number of times:
print "Udacity! "*10

# BONUS!
# From your summarize code you just wrote, can you make the table even more visual by 
# replacing the count with a string of asterisks that represent the count of a number?
# The table should look like

"""
number | occurrence
     0 | *
     1 | **
     2 | ***
     3 | **
     4 | **
     5 | *
     6 | *
     7 | **
     8 | ***
     9 | *
    10 | **
"""
index = 0
print "number " + "| " + "occurrence"
while index < len(count_list)-1:
    print " "*5 + str(index) +" | " + str(count_list[index])
    index +=1
print " "*4 + "10" +" | " + str(count_list[10])

print "number | occurrence"
index = 0
num_len = len("number")

while index < len(count_list):
  num_spaces = num_len - len(str(index))
  print " " * num_spaces + str(index) + " | " + str(count_list[index])
  index = index + 1

  # Congratulations! You just created a distribution table of a list of numbers! 
# This is also known as a histogram


def greatest(list_of_numbers):
    index = 0
    lenth = len(list_of_numbers)
    if lenth == 0:
        return 0
    else:
        number = 0
        while index < lenth:
            if list_of_numbers[index] > number:
                number = list_of_numbers[index]
            index += 1
        return number


print greatest([])
print greatest([4,23,1])

'''
def word_in_pos(word, parts_of_speech):
    # your code here
    s = ''.join(e for e in word if e.isalnum())
    if s in parts_of_speech:
        return s
    else:
        return "None"
'''
parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]
test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""     
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
#parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]
'''
print word_in_pos(test_cases[0], parts_of_speech)
print word_in_pos(test_cases[1], parts_of_speech)
print word_in_pos(test_cases[2], parts_of_speech)
print word_in_pos(test_cases[3], parts_of_speech)
'''

def play_game(ml_string, parts_of_speech):    
    replaced = []
    # your code here
    ml = ml_string.split()
    for w in ml:
        r = (word_in_pos(w, parts_of_speech))
        if r != None:
            w = w.replace(r,"corgi")
            replaced.append(w)
        else:
            replaced.append(w)
    replaced = ' '.join(replaced)
    return replaced
    
print play_game(test_string, parts_of_speech)