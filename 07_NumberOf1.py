# 作者：wangchuang
# 日期：2019/5/21 4:18 PM
# 工具：PyCharm
# Python版本：3.6.3
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n & 0xffffffff).count('1')

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n & 0xffffffff:
            count += 1
            n = (n - 1) & n
        return count