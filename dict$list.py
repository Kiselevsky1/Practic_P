# #LIST
# L = [1,2,3,4] #Create list
# print(L)
#
# L.append(5) #add element
# print(L)
#
# L.extend([6,7,8]) #add  elements
# print(L)
#
# L.insert(8 , 8) #add 9 on index 8
# print(L)
#
# print(L.index(8)) #index elemnt ( list.index(x , [start , stop])  )
#
# print(L.count(8)) # Count element
#
# L.reverse() # sort list 1 < 0
# print(L)
#
# L.sort() # sort list 0 > 1
# print(L)
#
# L.pop(8) # delete elemnt on index
# print(L)
#
# L.remove(1) # delite on value
# print(L)
#
#
#
# del L[1]
# print(L)
# del L[5:8]
# print(L)
#
#
#
# L = [x**2 for x in range(5)]
# print(L)
#
# print(list(map(ord, "spam")))


#DICT

D = {} # Empty dict
print(D)

D2 = {'spam' : 2, 'eggs' : 3} #dict , two elemets
print(D2)
print(D2['eggs'])
print('eggs' in D2)

D3 = {'food' : {'ham' : 1, 'egg' : 2}}
print(D3)
print(D3['food']['ham'])

D4 = dict(name = 'Bob', age=40)
print(D4)

D5 = dict(zip(keyslist , valuelist))
print(D5)































