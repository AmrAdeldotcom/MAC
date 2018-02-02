# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1210],
             ['Romania', 'Bucharest', 21],
             ['United States', 'Washington', 307]]


def findcountry(search):
    result =''
    for sublist in countries:
        if sublist[0] == search:
            result = sublist[1]
            break
        else:
            result = "No Country Found to Get Capital "
    return result

# Write code to print out the capital of India
# by accessing the list
print (findcountry('India'))

s= 1
print(s)
print(id(s))
s=2
print(s)
print(id(s))
p = [1,2,3]
print(p)
print(id(p))
p[0]=100
print(p)
print(id(p))

p =[1,2]
q = [3,4]
p.append(q)
print (len(p))
print (p)
# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.
'''
def find_element(list,svalue):
    if list.index(svalue):
        return list.index(svalue)
    else:
        return -1
'''
def find_element(list,svalue):
    i = 0
    while i < len(list):
        for item in list:
            if item == svalue :
                return i
                break
            else:
                i+=1
    if i == len(list):
        i = -1
    return i


print (find_element([1,2,3],3))
#>>> 2

print (find_element(['alpha','beta'],'gamma'))
#>>> -1

def find_element(list,svalue):
         if svalue in list :
            return list.index(svalue)
         else:
             return -1
print (find_element([1,2,3],3))
#>>> 2

print (find_element(['alpha','beta'],'gamma'))
#>>> -1