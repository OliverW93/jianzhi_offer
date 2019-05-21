# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows, columns = len(array)-1, len(array[0])-1
        i = 0
        j = columns
        while j>=0 and i<=rows:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
        return
