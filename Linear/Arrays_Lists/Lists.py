#For Theory Refer To The Wiki.

#Different Ways to create Lists in Python

# Using [] brackets

import array as arr

my_list1 = []

print(my_list) #Output is []

#Using list() constructor

my_list2 = list()

print(my_list) #Output is []

#Using array module - imported the module on line 7.

my_list3 = arr.array('i', [2, 3, 4, 5]) '''The array method takes two parameters - Here 'i' means Integer and similarly 
                                       other primitive data types like double ('d') can be used to initialize the list/array.'''

#We can initialize lists/arrays with some predefined values also.

my_list4 = [10, 20, 30, 40, 50] #List of Integers. Same can be created with other types such as - Strings, Double, Char etc.

my_list5 = [10, '20', 30.0] #Lists are flexible enough to store values with different data types.

#We can access the elements of a list either by mentioning the index number or using a for-loop

#Using index

print(my_list4[0]) #Output is 10. Similarly we can use indexs upto (length of the list - 1) within the brackets. Exceeding that will throw index error.

#Using For-Loop

for i in range(len(my_list4)):
  print(my_list4[i])           '''Output is 10
                                            20
                                            30
                                            40
                                            50'''

#We can also use a for-each loop
for ele in my_list5:
  print(ele)                    '''Output is 10
                                             '20'
                                             30.0'''


                                             





