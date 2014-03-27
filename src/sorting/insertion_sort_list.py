# implement the insertion sort with list


def insertion_sort(alist):
    
    # pointer starts from the second element
    for i in range(1,len(alist)):
        
        
        key = alist[i]
        
        j = i - 1
        
        while j >= 0 and alist[j] > key:
            alist[j+1] = alist[j]
            j -= 1
            
        alist[j+1] = key
    
    return alist




alist = [2,1,4,5,11,0,9,6]
print insertion_sort(alist)