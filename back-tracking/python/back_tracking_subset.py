from typing import List

class Subset:
    def solutions(self, inputs:List)->List[List[int]]:
        self._input = inputs
        self.subset = []
        self._BT(0, [])
        return self.subset
        
    def _BT(self, index:int, crnt_set: List[int]):
        if index == len(self._input):
            self.subset.append(crnt_set.copy())
            return
        
        # STEP1. []
        num = self._input[index]
        self._BT(index + 1, crnt_set)
        
        # STEP2. [a]
        crnt_set.append(num)
        self._BT(index + 1, crnt_set)
        crnt_set.pop()

obj = Subset()
print(obj.solutions([1,2,5]))