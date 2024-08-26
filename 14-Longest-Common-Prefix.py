class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        strs.sort()
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i]!=strs[-1][i]:
                return output
            output += strs[0][i]
        return output
                    