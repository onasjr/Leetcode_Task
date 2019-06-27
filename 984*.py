## 不含AAA或BBB的字符串
## 分情况讨论，大于等于2倍时先写aab/bba；之后追加a/b；
## 二倍以内时先写aab或bba，之后追加ab/ba


class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        # 分情况讨论，大于等于2倍时先写aab/bba；之后追加a/b；
        # 二倍以内时先写aab或bba，之后追加ab/ba
        if A >= B*2:
            return "aab" * B + "a" * (A-2*B)
        elif B >= A*2:
            return "bba" * A + "b" * (B-2*A)
        elif A >= B:
            return "aab" * (A-B) + "ab" * (2*B-A)
        else:
            return "bba" * (B-A) + "ba" * (2*A-B)
