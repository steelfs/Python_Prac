# x = 5
# if x % 2 == 0:
#     print('it\'s even')
# else:
#     print('it\'s odd')

# x = -3
# if x < 0:
#     print('less than 0')
# else:
#     print('greater than 0')

# def GetList() -> list[int]:
#     result = []
#     for i in range(1, 11, 1):
#         result.append(i)
    
#     return result

# def Calculator(list : list[int]) -> int:
#     result = 0
#     for i in list:
#         result += i

#     return result

# x = GetList()
# total = Calculator(x)

# print(total)


# '''
# 0 --- 0
# 0 --- 1
# 0 --- 2
# 1 --- 0
# 1 --- 1
# 1 --- 2
# 2 --- 0
# 2 --- 1
# 2 --- 2
# '''

# for i in range(3):
#     for j in range(3):
#         print(f'{i} --- {j}')

'''
0 --- 0 --- 1
0 --- 0 --- 2
0 --- 0 --- 3
0 --- 1 --- 1
0 --- 1 --- 2
0 --- 1 --- 3
1 --- 0 --- 1
1 --- 0 --- 2
1 --- 0 --- 3
1 --- 1 --- 1
1 --- 1 --- 2
1 --- 1 --- 3
'''

# for x in range(2):
#     for y in range(2):
#         for z in range(1, 4, 1):
#             print(f'{x} --- {y} --- {z}')


# 4. inputString="12    1      14        20           56          23 "
# 값을 split, trim, replace, slice, for문 중에 필요한 것만 사용해서
# 모든 숫자의 합을 출력하세요

# 예시

# def Filter(inputString : str):
#     arr = inputString.split(' ')
#     list_ = []
#     for i in arr:
#         if len(i) > 0:
#             list_.append(i)
    
#     total = 0
#     for i in range(len(list_)):
#         str_ = list_[i]
#         element = int(str_)
#         print(f'element_{i} : {element}')
#         total += element
    
#     print(total)

# Filter("12    1      14        20           56          23 ")

# --------------- 출력 -------------
# 12
# 1
# ...
# 23
# 합



# 5." Hello abs Absolutely above cab go bye a boy able "  위 문장에서 소문자로된 "ab"의 갯수를 출력하세요
# 예시
# --------------- 출력 -------------
# abs, above, cab, able
# 합 : 4

# def Collect_word(input : str):
#     token = 'ab'
#     arr = input.split(token)

#     result = len(arr) - 1
#     print(input)

# Collect_word(" Hello abs Absolutely above cab go bye a boy able ")

import time

def Collect_word(ab_str : str) -> int:
    result = 0
   # print(ab_str)

    length = len(ab_str)
    for i in range(length):
        # if i == length - 1: # 100000번 루프 기준 평균 0.8초
        #     break
        char = ab_str[i]
        #next = ab_str[(i + 1)]
        next = ab_str[min((i + 1), length - 1)]# 100000번 루프 기준 평균 1.75초
        if char == 'a' or char == 'A':
            if(next == 'b'):
                result += 1

    return result


count = 0
def TestLoop():
    global count
    for i in range(100000):
        result =  Collect_word(" Hello abs Absolutely above cab go bye a boy able ")
        count = result
        
before = time.time()    
TestLoop()
after = time.time()
elapsed = after - before

print(f'result = {count}')
print(f'time : {elapsed:.2f}')
'''
6 위 문장에서 대소문자 구분하지 말고 "ab"의 갯수를 출력하세요. 
(로직학습을 위한 것이므로  count 함수는 사용하지 마세요!)

예시



--------------- 출력 -------------
abs, Absolutely, above, cab, able
합 : 5
'''




# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         dict = {}
#         for i in len(nums[i]):
#             diff = target - nums


# question = Solution()
# question.twoSum([1, 3, 6, 7, 9, 11], 14)
