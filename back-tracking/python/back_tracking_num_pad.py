from typing import List   

class LetterCombinations:
  def solutions(self, digits: str) -> List[str]:
    self._keypad = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    
    if len(digits) == 0 :
      return []   
    
    self._digits = digits
    self._comb = []    
    self._BT(index=0,crntStr=[])
    return self._comb
    
  def _BT(self, index:int, crntStr: List[str]):
    if index == len(self._digits):
      comb = ''.join(crntStr)
      self._comb.append(comb)
      return
    
    num = int(self._digits[index])
    chars = self._keypad[num]
    for char in chars:
      crntStr.append(char)
      self._BT(index+1, crntStr)      
      crntStr.pop()
      
letterComb = LetterCombinations()
print(letterComb.solutions(digits='257'))