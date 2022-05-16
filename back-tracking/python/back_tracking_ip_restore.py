"""
[200523132] 리스트가 존재할 때
위 요소를 이용해 IP를 만들 수 있는 조건은 몇가지가 있을까?

생각할 수 있는 조건
1. 각 항목의 값은 255 이하여야 한다.
2. 각 항목은 0으로 시작할 수 없다.
"""
from typing import List

BLOCK_SIZE = 3
NUM_OF_BLOCK = 4

class IPRestore:
    def solution(self, inputs:List[int]) -> List[List[int]]:
        self._inputs = inputs
        self._result = []
        self._length = len(inputs)
        self._BP(0, 0, [])
        
        return self._result
    
    def _BP(self, start_index, prev_block, ip):
        if len(ip) == NUM_OF_BLOCK:
            for block in ip:
                if len(block) <= 0:
                    return
            
                if block[0] == 0 and len(block) > 1:
                    return
    
        if start_index == self._length and len(ip) == NUM_OF_BLOCK:
            save_ip = ''
            for block in ip:
                temp_block = ''
                for num in block:
                    temp_block += str(num)
                save_ip += (str(temp_block) + '.')
            self._result.append(save_ip[:-1])
            return
        
        # STEP 1. BLOCK SIZE
        for block in range(prev_block, NUM_OF_BLOCK):
        
            # STEP 2. start index ~ += 3
            for index in range(start_index, start_index + BLOCK_SIZE):
                target_index = index + 1
                selected_block = self._inputs[start_index: target_index]
                ip.append(selected_block)
                self._BP(target_index, prev_block + 1, ip)
                ip.pop()
                
ip = IPRestore()
print(ip.solution([2,5,2,0,4]))