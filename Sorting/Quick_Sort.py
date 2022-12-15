#The following is the implementation of the Quick Sort Algorithm used for sorting an array/list.
#For Theory Refer The Wiki.

def partition(my_list, si, ei):                                        #I have named this function as partition since the array will be divided into two parts based upon the pivot element.
    pivot = my_list[0]                                                 #For simplicity, I have assumed the first element i.e. index 0 of the array/list as pivot element.
    count = 0                                                          #This variable is actually used to count the number of elements which are less than the pivot element.
    for i in range(si, ei + 1):  
        if pivot > my_list[i]:                                         #Increment count if current element is greater than pivot element.
            count += 1
    my_list[si + count], my_list[si] = my_list[si], my_list[si + count]#si + count will bring current pivot(my_list[si]) to the new postition after the swapping happens.
    pivot_index = si + count                                           #Actual pivot element index that we will return at the end of this function. This will be used for partitioning the array/list.
    i = si                      
    j = ei

    while i < j:                                                       #The pivot element is at it's correct position. Now, this loop will make sure all 
        if my_list[i] < my_list[pivot_index]:                          #elements at the left of the pivot are smaller and elements at right are bigger.
            i = i + 1
        elif my_list[j] > my_list[pivot_index]:                       
            j = j - 1
        else:
            my_list[i], my_list[j] = my_list[j], my_list[i]            #This swapping will help in acheiving our target.
            i = i + 1
            j = j - 1

    return pivot_index                                                 #Actual pivot index


def quick_sort(my_list, si, ei):
    if si > ei:                                                       #Base case
        return my_list
    index = partition(my_list, si, ei)                                #Index of the pivot element
    quick_sort(my_list, si, index - 1)                                #Recursive Call - Problem gets sub divided into two parts
    quick_sort(my_list, index + 1, ei)                                #First Part -> mylist[:index] Second Part -> [index + 1:]  
                                                                        

#Main
a = [12, 31, 44, 45, 22, 78, 62]
print(a)
quick_sort(a, 0, len(a) - 1)
print()
print(a)

------------------------------------------------------------------Sample I/O------------------------------------------------------------------------

[12, 31, 44, 45, 22, 78, 62]              #Input

[12, 22, 31, 44, 45, 62, 78]              #Output
