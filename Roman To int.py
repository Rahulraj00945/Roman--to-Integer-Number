class Solution(object):
   def romanToInt(self, s):
      roman = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000,'R':5000}
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            num+=roman[s[i]]
            i+=1
      return num
ob1 = Solution()
x = input("Roman number is: ")
print("Converted value into integer is: ",ob1.romanToInt(x))
