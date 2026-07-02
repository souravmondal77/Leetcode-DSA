class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0
        
        for ch in s:
            if ch == '(':
                # Add only if not outermost opening
                if balance > 0:
                    result.append(ch)
                balance += 1
            
            else:  # ch == ')'
                balance -= 1
                # Add only if not outermost closing
                if balance > 0:
                    result.append(ch)
        
        return "".join(result)