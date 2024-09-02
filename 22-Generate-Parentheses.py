class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # open and close means the number of open and close paranthesis
        def paranthesiscombinations(open, close, s):
            if len(s)==n*2:
                res.append(s)
            if open<n:
                paranthesiscombinations(open+1, close, s+'(')
            if close<open:
                paranthesiscombinations(open, close+1, s+')')
        paranthesiscombinations(0, 0, '')
        return res