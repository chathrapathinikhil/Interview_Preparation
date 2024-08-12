class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        
        phonedigits = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        output = []  
        
        def backtrack(combinations, next_digits):
            if len(next_digits)==0:
                output.append(combinations)
            else:
                for i in phonedigits[next_digits[0]]:
                    print(combinations+i)
                    backtrack(combinations + i, next_digits[1:])

        backtrack("", digits)
        return output  