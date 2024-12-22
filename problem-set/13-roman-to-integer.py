class Solution(object):
    def romanToInt(self,s):
      dic1 = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
      }
      dic2 = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
      }
      total = 0
      i = 0
      while i <= len(s) - 1:
        if i == len(s) - 1:
          return total + dic1[s[i]]
        two = s[i] + s[i+1]
        val = dic2.get(two, 0)
        if val != 0:
          total += val
          i += 2
        else:
          total += dic1[s[i]]
          i += 1 
      return total    
        
        
s = Solution()
print("solution ", s.romanToInt("III"))