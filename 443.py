## 压缩字符串
## 设置记录不同字符比较到的位置  和  替换后的起始位置


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        final_index = 0  # 记录不同字符比较到的位置
        i = 0   # 记录替换后起始位置

        while i < len(chars):
            num = 1  # 记录相同字符个数
            # pdb.set_trace()
            while final_index < len(chars)-1 and chars[final_index] == chars[final_index + 1]:
                final_index += 1
                num += 1
            if num != 1:
                chars[i:final_index+1] = [str(chars[i]), str(num)]
                i += 2
                final_index = i
            else:
                i += 1
                final_index = i
        return chars
