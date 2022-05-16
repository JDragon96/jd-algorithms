from typing import List

class Permutation:
    def permute(self, inputs: List[int]) -> List[List[int]]:
        self._inputs = inputs
        self._result = []
        self._BT([])
        return self._result
        
    def _BT(self, crnt_sets):
        if len(crnt_sets) == len(self._inputs):
            print(crnt_sets)
            self._result.append(crnt_sets)
            return
        
        for num in self._inputs:
            if num in crnt_sets:
                continue
            
            crnt_sets.append(num)
            self._BT(crnt_sets)
            crnt_sets.pop()
            
            
per = Permutation()
print(per.permute([1,2,5]))