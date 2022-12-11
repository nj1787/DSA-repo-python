#Refer wiki for theory.

#Linear search can be implemented in two ways : Recursive and Iterative.

#Iterative
def Linear_Search_Iterative(arr, ele):
    for i in range(len(arr)):   #Loop till last index of the array/list.
        if arr[i] == ele:       #If current element is equal to element we are searching for, return that index.
            return i            
    return -1                   #-1 means  element we are searching for is not present in the array/list.

#Recursive
def Linear_Search_Recursive(arr, ele):
    if len(arr) == 0:           #Base Case
        return -1
    small_output = Linear_Search_Recursive(arr[1:], ele) #Recursive Call. small output will have index of element 1 less than actual index.
    if small_output == -1:                               #Condition for element not found in smaller list.
        if arr[0] == ele:                                #Check whether the first element of original array/list is equal to element to be searched.
            return 0                                     #If True, return 0 
        else:
            return -1                                    #-1 means  element we are searching for is not present in the array/list.
    else:
        return 1 + small_output                          #We add 1 to the small output so that we get actual index of the element as size of the list was reduced.    

array = [90, 12, 16, 71, 82, 24, 88, 67, 52, 49]
print(array)
result1 = Linear_Search_Iterative(array, 52)
print(result1)
print()
result2 = Linear_Search_Iterative(array, 50)
print(result2)


-------------------------------------------------------------Sample I/O-----------------------------------------------------------------------------------
[90, 12, 16, 71, 82, 24, 88, 67, 52, 49]
8             #Output for Iterative.

-1            #Output for Iterative.
  
5             #Output for Recursive.

-1            #Output for Recursive.
