## 超级丑数
## 设置一个表示primes系数的list，存放每一位相乘的次数


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        res=[1]
        inx=[]  # 每个primes对应位置的系数
        for i in range(len(primes)):
            inx.append(0)
        for i in range(n-1):
            res.append(min( primes[j]*res[inx[j]] for j in range(len(primes)) ))
            for k in range(len(primes)):
                if res[-1]==primes[k]*res[inx[k]]:
                    inx[k]+=1
        return res[-1]
