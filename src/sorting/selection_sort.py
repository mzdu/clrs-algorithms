
def selection_sort(alist):
    ''' @summary: first, find the smallest number and exchange it with the first element, then find the second smallest and exchange with the second element...
        @param key: input is a random number list
        @type key: a list
        @return: returns a list of sorted numbers 
        @rtype: list
    '''
    
    i = 0
    key_idx = 0
    key = alist[0]
    len1 = len(alist)
    
    # first find the smallest of the first loop
    while i<len1:
        
        if alist[i]<key:
            alist[i], key = key, alist[i]
        
        
        
        
        
        
        
        
        
        
        
        
        j = i + 1
        while j<len1:
            
            if alist[j]<key:
                alist[j], key = key, alist[j]
            
            j +=1
        
        i += 1
    
    
    return alist
    
    
list1 = [12,10,9,1,8,3,0,7]
print selection_sort(list1)