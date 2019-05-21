# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # 用递归
        if n == 0:
            return 0
        elif n== 1:
            return 1
        elif:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # 用循环
        a,b = 0,1
        for _ in range(n):
            a,b = b, a+b
        return a
