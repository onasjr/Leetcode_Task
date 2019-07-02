## 车的可用捕获量
# 首先找到车所在的行和列，然后将空位替换为“”，分别在所在行和列查找Rp和pR数量即为车所能捕获的卒数

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        output = 0
        col = None
        row = None
        for i in range(len(board)):
            if 'R' in board[i]:
                row = i
                break
        col = board[row].index('R')
        s = ''.join(board[row])
        s = s.replace('.', '')
        if 'pR' in s:
            output += 1
        if 'Rp' in s:
            output += 1
        s = ''.join([i[col] for i in board])
        s = s.replace('.', '')
        if 'pR' in s:
            output += 1
        if 'Rp' in s:
            output += 1
        return output
