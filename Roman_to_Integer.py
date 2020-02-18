class Solution(object):
    # https://leetcode.com/problems/roman-to-integer/
    def __init__(self):
      self.roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
          return self.roman[s]

        convert_num = 0
        temp = 0
        roman_length = len(s)
        for iteration in range(roman_length):
          if temp == 1:
            temp = 0
            continue
          try:
            cal, temp = self.calculate(self.roman[s[iteration]], self.roman[s[iteration+1]])
            convert_num += cal 
          except:
            convert_num += self.roman[s[iteration]] 

        return convert_num

    def calculate(self, num1, num2):
      if num1 < num2:
        return num2 - num1, 1
      else:
        return num1, 0 
'''
best solution

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        for i in range(n-1):
            v1 = r[s[i]]
            v2 = r[s[i+1]]
            if v1 >= v2:
                sum += v1
            else:
                sum -= v1
        
        return sum + r[s[-1]]

'''



if __name__ == '__main__':
  s = Solution()
  print(s.romanToInt("I"))

  print(s.romanToInt("III"))

  print(s.romanToInt("IV"))

  print(s.romanToInt("LVIII"))

  print(s.romanToInt("MCMXCIV"))
