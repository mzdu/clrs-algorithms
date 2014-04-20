# pay attention on infinity 'inf'  +infinity = float('inf'), -infinity = float('-inf')
# In Java, Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY

def peak_finding(alist):
    """ a brute force method """
    i = 0
    length = len(alist)
    while i < length:
        
        if i ==0 and alist[i]>alist[i+1]:
            print 'find a peak', alist[i]
            return alist[i]
            
        elif i==length-1 and alist[i]>alist[i-2]:
            print 'find a peak', alist[i]
            return alist[i]
        
        else:
            if alist[i]>=alist[i-1] and alist[i]>=alist[i+1]:
                print 'find peak', alist[i]
                return alist[i]
                
            else:
                print 'keep moving forward'
                i += 1
            
        
def peak_finding2(alist):
    """ divide and conquer method """
    
    # first reconstruct this list
    
    blist = []
    blist.append(float('-inf'))
    blist = [x for x in alist]
    
    import random
    
    length = len(alist)
    
    pivot = random.randint(0, length-1)
    print 'pivot', pivot
    
    if pivot == 0 and alist[pivot] > alist[pivot+1]:
        return alist[pivot]
    
    elif pivot = length-1 and alist[pivot]>
    
        
        
alistt = [12,23,1,8,9,11,32,45,0,7,6,4,31]

peak_finding(alistt)