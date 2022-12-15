def merge_two_sorted_lists(list1, list2, org_list):             #This is a helper function which would help us formulate the final result. 

    i = j = k = 0                                               #Index Variables for list1, list2 and org_list respectively.

    while i < len(list1) and j < len(list2):                    #This loop is the place where actual merging of two arrays happen inside another list/array.
        if list1[i] < list2[j]:                                 #If element in list1 is less than element in list2, that element gets appended to the org_list.
            org_list[k] = list1[i]
            i = i + 1
            k = k + 1
        elif list1[i] > list2[j]:                               #Else if element in list2 is less than element in list1, that element gets appended to the org_list.
            org_list[k] = list2[j]
            j = j + 1
            k = k + 1
                                                                
    while i < len(list1):                                       #If some elements are left in any of the arrays/lists due to unequal sizes, the next two loops
                                                                #would perform the same operations for both the lists/arrays.
        org_list[k] = list1[i]
        i = i + 1
        k = k + 1

    while j < len(list2):
        org_list[k] = list2[j]
        j = j + 1
        k = k + 1


def merge_sort(my_list):
    if len(my_list) <= 1:                                         #Base Case.
        return                                                    #Do Nothing.
    mid = len(my_list) // 2                                       #Finding middle element index. At the start of each recursive call, mid will be updated
    left_sublist = my_list[:mid]                                  #Sub-problem 1.
    right_sublist = my_list[mid:]                                 #Sub-problem 2.
    merge_sort(left_sublist)                                      #Recursive Call using sub-problem 1. 
    merge_sort(right_sublist)                                     #Recursive Call using sub-problem 2.
    merge_two_sorted_lists(left_sublist, right_sublist, my_list)  #Kind of a helper function to make the code look cleaner.


#Main
a = [91, 62, 66, 87, 95, 53, 45]
print(a)
merge_sort(a)
print()
print(a)

---------------------------------------------------------------------SAMPLE I/O----------------------------------------------------------------
[91, 62, 66, 87, 95, 53, 45]            #Input

[45, 53, 62, 66, 87, 91, 95]            #Output

#Extra test cases

[91]                                    #Input

[91]                                    #Output
