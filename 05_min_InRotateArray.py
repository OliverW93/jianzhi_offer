# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        low = 0
        high  = len(rotateArray) -1
        while low < high:
            mid = (low + high) // 2
            if rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            else:
                high = mid
        return rotateArray[low]