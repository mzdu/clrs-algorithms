class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, source, target):
        if source == None or target == None:
            return -1
        if target == '':
            return 0
        
        searchLength = len(source) - len(target) + 1
        
        # 2. searching starts from index 0, for source
        i = 0
        
        while i < searchLength:
            # j is the index for target
            j = 0            
            while j < len(target):
                if source[i + j] != target[j]:
                    break
                j += 1
            
            if j == len(target):
                return i
            i += 1
        
        return -1