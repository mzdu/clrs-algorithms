# implement a merge sort

# 1. if n = 1 T(n) = 1
# 2. Recursive Sort T(n) = 2T(n/2)
# 3. Merge 2 sorted lists

def merge_leaf(node):
    pass


def merge_sort(alist):
    
    len1 = len(alist)
    
    if len(alist) == 1:
        return alist[0]
    
    else:
        num1 = merge_sort(alist[:(len1/2)])
        
        num2 = merge_sort(alist[(len1/2):])
        
        if num1 < num2:
            print num1
        else:
            print num2
            
alist = [2,1,4,5,11,0,9,6]
merge_sort(alist)

