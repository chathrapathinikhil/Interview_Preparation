class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def splitexpression(expression):
            if expression.isdigit():
                return [int(expression)]
            output = []
            for i in range(len(expression)):
                if expression[i] in '+-*':
                    leftside = splitexpression(expression[:i])
                    rightside = splitexpression(expression[i+1:])
                    for left in leftside:
                        for right in rightside:
                            if expression[i] == '+':
                                output.append(left + right)
                            elif expression[i] == '-':
                                output.append(left - right)
                            else:
                                output.append(left * right)
            return output
        return (splitexpression(expression))            
            