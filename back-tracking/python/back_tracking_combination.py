from typing import List

class Combination:
    def solution(self, inputs: List[int], expected_result: int):
        self._inputs = inputs
        self._result = []
        self._label = expected_result
        self._length = len(inputs) - 1
        
        if self._label == 0:
            return []
        
        self._BP(inputs[0], [])
        
        return self._result
        
    def _BP(self, prev_value, crnt_sets):
        if sum(crnt_sets) > self._label:
            return
        
        if sum(crnt_sets) == self._label:
            self._result.append(crnt_sets.copy())
            return
        
        for num in self._inputs:
            if prev_value > num:
                continue
            
            crnt_sets.append(num)
            self._BP(num, crnt_sets)
            crnt_sets.pop()
            
com = Combination()
print(com.solution([1,2,3], 5))