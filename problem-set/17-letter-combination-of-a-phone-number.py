from typing import List, Dict

class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    dict: Dict[str, List[str]] = {
      "1": [],
      "2": ["a", "b", "c"],
      "3": ["d", "e", "f"],
      "4": ["g", "h", "i"],
      "5": ["j", "k", "l"],
      "6": ["m", "n", "o"],
      "7": ["p", "q", "r", "s"],
      "8": ["t", "u", "v"],
      "9": ["w", "x", "y", "z"]
    }
    
    filtered_digits = ""
    for digit in digits:
      if digit != "1":
        filtered_digits += digit
    digits = filtered_digits
    if digits == "": return []
    
    digits_len = len(digits)
    result_len = 1
    for digit in digits:
      result_len = result_len * len(dict[digit])
    
    limit_list = [1] * digits_len
    i = digits_len - 1
    while i >= 1:
      limit_list[i-1] = limit_list[i] * len(dict[digits[i]])
      i -= 1
      
    result = [""] * result_len
    for i, digit in enumerate(digits):
      j = 0
      k = 0
      while j < result_len:
        result[j] += dict[digit][k]
        j += 1
        if j % limit_list[i] == 0:
          k += 1
        if k == len(dict[digit]):
          k = 0
        
    return result
s = Solution()
print("solution",s.letterCombinations("67"))