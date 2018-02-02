mylist1 = [1,2,3,4]
print mylist1 #[1, 2, 3, 4]
print id(mylist1) # 87172960
mylist1 = mylist1 + [5,6]
print mylist1 #[1, 2, 3, 4, 5, 6]
print id(mylist1) # 87172440


mylist2 = [1,2,3,4]
print mylist2 #[1,2,3,4]
print id(mylist2) # 87172960
mylist2.append([5,6]) 
print  mylist2 # [1, 2, 3, 4, [5, 6]]
print id(mylist2) # 87172960

mylist3 = [1,2,3,4]
print  mylist3 #[1, 2, 3, 4]
print id(mylist3) # 87152280
mylist3 += [5,6]
print mylist3 #[1, 2, 3, 4, 5, 6]
print id(mylist3) # 87152280

'''
from L13F2 import daysBetweenDates
print (daysBetweenDates(2012,1,1,2012,2,28))

import L13F2
print L13F2.daysBetweenDates(2012,1,1,2012,2,28)
L13F2.test()
'''
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
   random_list.append(random.randint(0,10))

print random_list

random_list2 = []
count = 0
while count < list_length:
   random_list2.append(random.randint(0,10))
   count += 1

print random_list2

