class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        stack  = 0
        for element in A:
            stack = stack ^ element
            
        return stack