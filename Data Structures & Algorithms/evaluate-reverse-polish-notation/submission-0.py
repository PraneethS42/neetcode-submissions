class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for tkn in tokens:
            if tkn in ('+','-','*','/'):
                first = int(stk.pop())
                second = int(stk.pop())
                if tkn == '+':
                    res = second + first
                elif tkn == '-':
                    res = second - first
                elif tkn == "*":
                    res = second * first
                else:
                    res = second / first
                stk.append(res)
            else:
                stk.append(tkn)
        
        return int(stk[0])
     