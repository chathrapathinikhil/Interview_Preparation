class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        rtoi = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if i+1<len(s) and rtoi[s[i]]<rtoi[s[i+1]]:
                output = output - rtoi[s[i]]
                # print(output)
            else:
                output = output + rtoi[s[i]]
                # print(output, rtoi[s[i]])
        return output
