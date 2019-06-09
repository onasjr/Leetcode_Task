## 括号生成
## 迭代左括号右括号剩余的个数
class Solution:
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(left, right, tmp, res):
            if left == 0 and right == 0:
                res.append(tmp)
                return res
            if left>0:
                backtrack(left-1,right,tmp+'(',res)
            if right>left:
                backtrack(left,right-1,tmp+')',res)
            
        backtrack(n, n, "", res)
        return res
        
    
