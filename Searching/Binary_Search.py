#For Theory Refer To The Wiki.
#The following consists of a two kinds of implementations of Binary Search Algorithm -> Iterative and Recursive.

#Iterative Approach
def binary_search_iterative(a, low, high, num):
    while low <= high:             #Entry Condition otherwise will return -1.
        mid = (low + high) // 2    #Start by Finding the Middle Index as the loop proceeds.This is how size of problem gets reduced to half.
        if a[mid] == num:          #Possible that the element you are searching for is present at the middle.
            return mid
        elif a[mid] < num:         
            low = mid + 1          #If middle element is less than the number you are searching for, then high remains same and we increment mid by 1
                                   #and assign to low.
        else:
            high = mid - 1         #If middle element is greater than the number you are searching for, then low remains same and we decrement mid by 1
                                   #and assign to high.
    
    return -1                      #-1 means element is not found in the given array/list.

def binary_search_recursive(a, low, high, num):
    if low > high:                #Base Case 
        return -1                 #-1 means element is not found in the given array/list.
    mid = (low + high) // 2       #Mid Calculation Happens At Each Recursive Call.This is how the size of problem gets reduced to half.
    if a[mid] == num:             #Possible that the element you are searching for is present at the middle.
        return mid
    elif a[mid] > num:            #If middle element is greater than the number you are searching for, then low remains same and we decrement mid by 1
                                  #and assign to high.
        return binary_search_recursive(a, low, mid - 1, num) #Tail Recursion.
    else:                         #If middle element is less than the number you are searching for, then high remains same and we increment mid by 1
                                  #and assign to low.
        return binary_search_recursive(a, mid + 1, high, num) #Tail Recursion.



#Main
arr = [12, 15, 16, 20, 23, 45, 57, 62]      #The only prerequisite for Binary Search is the array/list should be sorted(Ascending/Descending).
print(arr)
result1 = binary_search_iterative(arr, 0, len(arr) - 1, 45)
print(result1)
print()
result2 = binary_search_recursive(arr, 0, len(arr) - 1, 16)
print(result2)

-----------------------------------------------------------------Sample I/O-----------------------------------------------------------------------------------
[12, 15, 16, 20, 23, 45, 57, 62]
5       #Output for Iterative Approach

2       #Output for Recursive Approach
