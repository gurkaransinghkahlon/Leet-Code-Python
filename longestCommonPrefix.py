class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        longestPrefix = ""
        index = 0
        chArray = strs[0]
        for ch in chArray:
            for i in range(1,len(strs)):
                if index >= len(strs[i]) or ch != strs[i][index]:
                    return longestPrefix
                
            longestPrefix += ch
            index += 1
            
        return longestPrefix