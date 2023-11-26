from collections import deque
import random

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i
        return[]
        
        

a = Solution()
z = random.random() * 100
param = 0
if z > 50:
    param = 10
else:
    param = 'gg'
    
    
    
    
b = a.twoSum([1,3,5,7,9], param)
print(b)