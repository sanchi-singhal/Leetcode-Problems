258. Add Digits
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        if(len(s)<=1):
            return num
        else:
            while(len(s)>1):
                m=0
                for i in s:
                    m=m+int(i)
                s=str(m)
            return m
