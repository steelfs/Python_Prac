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

# import time

# def Collect_word(ab_str : str) -> int:
#     result = 0
#    # print(ab_str)

#     length = len(ab_str)
#     for i in range(length):
#         # if i == length - 1: # 100000번 루프 기준 평균 0.8초
#         #     break
#         char = ab_str[i]
#         #next = ab_str[(i + 1)]
#         next = ab_str[min((i + 1), length - 1)]# 100000번 루프 기준 평균 1.75초
#         if char == 'a' or char == 'A':
#             if(next == 'b'):
#                 result += 1

#     return result


# count = 0
# def TestLoop():
#     global count
#     for i in range(100000):
#         result =  Collect_word(" Hello abs Absolutely above cab go bye a boy able ")
#         count = result
        
# before = time.time()    
# TestLoop()
# after = time.time()
# elapsed = after - before

# print(f'result = {count}')
# print(f'time : {elapsed:.2f}')
'''
6 위 문장에서 대소문자 구분하지 말고 "ab"의 갯수를 출력하세요. 
(로직학습을 위한 것이므로  count 함수는 사용하지 마세요!)

예시



--------------- 출력 -------------
abs, Absolutely, above, cab, able
합 : 5
'''


# 7 성적을 List로 입력하면 수 우 미 양 가를 출력하세요. 출력은 한줄에 공백을 하나씩 띄우고 하세요.
# 입력 및 출력 예시



# 수는 90보다 크거나 같을때
# 우는 80보다 크거나 같고 90보다 작을때
# 미는 70보다 크거나 같고 80보다 작을떄
# 양은 60보다 크거나 같고 70보다 작을때
# 가는 60보다 작을때
# [입력]
# score = [25, 99, 80, 69, 77]   

# [출력]
# 가 수 우 양 미 

# def Grade(score : list[int]):
#     result = ''
#     for i in score:
#         if i >= 90:
#             result += '수 '
#         elif i >= 80:
#             result += '우 '
#         elif i >= 70:
#             result += '미 '
#         elif i >= 60:
#             result += '양 '
#         else:
#             result += '가 '
        
#     print(result)


# Grade([25, 99, 80, 69, 77])



'''
8.  짝수면 출력하고 홀수면 출력하지 마세요

입력 및 출력 예시



입력
numbers = [4, 7, 8, 11, 13, 16, 18, 19, 21, 24]

출력
4 8 16 18 24
'''

# def Print_Even(numbers : list[int]):
#     for i in numbers:
#         if i % 2 == 0:
#             print(i)

# Print_Even([4, 7, 8, 11, 13, 16, 18, 19, 21, 24])





'''
9.  5의 배수가 나올때 까지 List의 숫자를 출력하세요

입력 및 출력 예시



입력
numbers = [4, 7, 8, 11, 13, 16, 18, 20, 21, 24, 26]

출력
4 7 8 11 13 16 18 
'''

# def Keep_Print(numbers : [list]):
#     for i in numbers:
#         if (i % 5) != 0:
#             print(i)
#         else:
#             print(f'End Loop value = {i}')
#             break


# Keep_Print([4, 7, 8, 11, 13, 16, 18, 20, 21, 24, 26])





'''
10. List에서 홀수의 합과 짝수의 합과 전체 합을 출력하세요

입력 및 출력 예시



입력
numbers = [4, 7, 8, 11, 13, 16, 18, 20, 21, 24, 26]

출력
홀수의합: 52
짝수의합: 116
총합계: 168

'''
# def Edit_Numbers(numbers : [list]):
#     even = 0
#     odd = 0
#     for i in numbers:
#         if (i % 2) == 0:
#             even += i
#         else:
#             odd += i
        
#     print(f'홀수의 합: {odd}')
#     print(f'짝수의 합: {even}')
#     print(f'총 합계: {odd + even}')

# Edit_Numbers( [4, 7, 8, 11, 13, 16, 18, 20, 21, 24, 26])





'''
11.  List에 들어있는 수 가운데 가장 큰 숫자를 출력하세요

입력 및 출력 예시



입력
numbers = [4, 7, 8, 11, 13, 16, 18, 20, 21, 24, 26, 10, 5, 22]

출력
가장큰수: 26 
'''

# def print_Greatest(numbers : [list]):
#     greatest = 0
#     for i in numbers:
#         if i > greatest:
#             greatest = i

#     print(greatest)

# print_Greatest([4, 7, 8, 11, 13, 16, 18, 20, 21, 24, 26, 10, 5, 22])


# a = 2
# b = 50
# c = 2

# answer = (a or b) == c
# if answer:
#     print('yes')


'''
12.  숫자가 몇자리 인지 출력하세요

입력 및 출력 예시



입력
number = 129934

출력
이 숫자는 6자리 입니다
'''

# def count_digits(number : int):
#     converted = str(number)
#     print(len(converted))

# count_digits(129934)





'''
13. 숫자를 거꾸로 만들어서 출력하세요. 

입력 및 출력 예시



입력
number = 129934

출력
439921
# '''
# def Reverse_Number(number : int):
#     converted = str(number)
#     firstElemant = converted[0]
#     sliced = converted[-1: 0: -1]
#     sliced += firstElemant
#     print(sliced)

# Reverse_Number(129934)



'''
14.  입력한 숫자의 팩토리얼 값을 구하세요 
중학교 수학책 나왔던거 까먹었던분을 위해….   n! = n x (n-1) x …. x 2 x 1   이걸 팩토리얼 이라고 합니다. 
5! = 5×4×3×2×1 = 120

입력 및 출력 예시



입력
number = 5

출력
120
# '''

# def Print_Factorial(number : int):
#     factorial = 1
#     i = 1
#     while i < number:
#         i += 1
#         factorial *= i

#     print(factorial)

# Print_Factorial(5)



'''
15.  X의 Y승을 계산하세요

입력 및 출력 예시



입력
x = 2
y = 3
(2의 3승을 구하는 문제:  2x2x2)
출력
8
'''

# def Multiplier(x : int, y : int):
#     i = 1
#     z = x
#     while i < y:
#         x *= z
#         i += 1

#     print(x)


# Multiplier(2, 3)






'''
16.  숫자에서 0을 모두 1로 바꾼 숫자를 출력하세요

입력 및 출력 예시



입력
number = 1020970

출력
1121971

# '''

# def Zero_to_One(number : int):
#     converted = str(number)
#     edited = converted.replace('0', '1')

#     print(edited)

# Zero_to_One(1020970)



'''
17.  입력된 2진수를 십진수 값으로 출력하세요

입력 및 출력 예시



입력
number = 10101

출력
21
'''

# def Binary_To_Decimal(number : int):
#     decimalized = 0
#     converted = str(number)
#     length = len(converted)
    

#     for i in range(length):
#         if converted[i] == '1':
#             if (i < length - 1):
#                 decimalized += Multiplier(2, ((len(converted) - i) - 1)) # 자릿수만큼 2를 제곱해서 결과값에 저장
#             else:
#                 decimalized += 1 # 첫번째 자리가 1일 경우는 제곱할 필요 없이 1만 더하기
#         else:
#             continue

#     print(decimalized)



# def Multiplier(x : int, y : int) -> int:
#     i = 1
#     z = x
#     while i < y:
#         x *= z
#         i += 1

#     return x

# Binary_To_Decimal(110111)




'''
18. 입력된 십진수를 2진수로 출력하세요

입력 및 출력 예시



입력
number = 20

출력
10100
'''


# def Decimal_To_Binary(number : int):
#     #맨 뒷쪽 비트부터 셋팅하면서 2로 계속 나눠나간다.
#     result = ''
#     while number > 1:
#         if number % 2 == 0:
#             result += '0'
#             number /= 2
#         else:
#             result += '1'
#             number -= 1
#             number /= 2

#     result += '1' # 맨 앞쪽 비트

#     result = result[::-1]

#     print(result)
    
# Decimal_To_Binary(119)


'''
19.  0부터 입력된 정수까지 3이 몇번 나올까요? 
예를 들어 33은 3이 두번 나오는 겁니다. 

입력 및 출력 예시

입력
number = 35

출력
10  
'''

# def CountOfThree(number : int):
#     count = 0
#     for i in range(number + 1):
#         converted = str(i)
#         for j in converted:
#             if j == '3':
#                 count += 1
    
#     print(count)

# CountOfThree(39)




'''
20.  dictionary를 이용하여 성적을 아래 출력값과 같이 출력하세요

입력 및 출력 예시

입력값

scores = {
  "김동현" : {
    "국어" : 89,
    "영어" : 77,
    "수학" : 95
  },
  "김민혁" : {
    "국어" : 80,
    "영어" : 85,
    "수학" : 100
  },
  "홍길동" : {
    "국어" : 90,
    "영어" : 80,
    "수학" : 85
  }
}
출력값
(출력시 정렬은 알아볼 정도만 하면 되니 너무 신경쓰지 마세요)
-------------------------------
텍스토리반 성적표 집계
-------------------------------
이름     국어    영어    수학    평균
김동현    89      77     95     87.0
김민혁    80      85     100    88.3 
홍길동    90      80     85     85
-------------------------------
평균     86.3    80.7   93.3
'''

# scores = {
#   "김동현" : {
#     "국어" : 89,
#     "영어" : 77,
#     "수학" : 95
#   },
#   "김민혁" : {
#     "국어" : 80,
#     "영어" : 85,
#     "수학" : 100
#   },
#   "홍길동" : {
#     "국어" : 90,
#     "영어" : 80,
#     "수학" : 85
#   }
# }

# from io import StringIO
# builder = StringIO()

# def Print_Scores(scores : [dict]):
#     line_x = '-----------------------------------------'
#     builder.writelines(f'{line_x}\n')
#     builder.writelines('텍스토리반 성적표 집계\n')
#     builder.writelines(f'{line_x}\n')
#     builder.writelines('이름    국어    영어    수학    평균\n')

#     korean_TotalScore = 0
#     english_TotalScore = 0
#     math_TotalScore = 0
    
#     for studentName, subject in scores.items():
#         builder.writelines(studentName)

#         personal_Score = 0
#         count = 0
#         for subject, score in subject.items():
#             personal_Score += score
#             count += 1
#             if count == 1:
#                 korean_TotalScore += score
#             elif count == 2:
#                 english_TotalScore += score
#             else:
#                 math_TotalScore += score
#             builder.writelines(f'\t {score}')
        
#         builder.writelines(f'\t{personal_Score / count:.2f}')
#         builder.writelines('\n')

#     builder.writelines(f'{line_x}\n')
#     builder.writelines(f'평균\t{korean_TotalScore / len(scores):.2f}\t {english_TotalScore / len(scores):.2f}\t {math_TotalScore / len(scores):.2f}')
#     result = builder.getvalue()
#     print(result)


# Print_Scores(scores)

'''
21.  For 문과 If  문을 아래와 같이 출력되도록 하시요

입력 및 출력 예시



입력
number = [1,2,3,4,5,6,7,8,9,10]

출력
1
2
4
5
7
8
10
'''

# def PrintByOrder(numbers : [list]):
#     [print(x) for x in numbers if x % 3 != 0]
  
# PrintByOrder([1,2,3,4,5,6,7,8,9,10])



'''
22.  For 문과 If  문을 아래와 같이 출력되도록 하시요

입력 및 출력 예시



입력
number = [1,2,3,4,5,6,7,8,9,10]

출력
3
6
9
'''

# def Multiple_Of_Three(numbers : list[int]):
#     [print(x) for x in numbers if x % 3 == 0]
    
# Multiple_Of_Three([1,2,3,4,5,6,7,8,9,10])




'''
23.  For 문과 If  문을 아래와 같이 출력되도록 하시요

입력 및 출력 예시



입력
number = [1,2,3,4,5,6,7,8,9,10]

출력
1
2
3
8
9
10
'''
# def Print_By_Condition(numbers : list[int]):
#     [print(z) for z in numbers if not ((z > 3) and (z < 8))]
    
# Print_By_Condition([1,2,3,4,5,6,7,8,9,10])



'''
24.  While 을 이용해서 아래와 같이 출력하시요

입력 및 출력 예시

출력
1
2
3
4
5
'''

# def Print_In_Order():
#     i = 1
#     while i < 6:
#         print(i) 
#         i += 1

# Print_In_Order()

'''
25.  While 과 if문을  이용해서 아래와 같이 출력하시요

입력 및 출력 예시

출력
1
2
4
5
# '''
# def Print_By_Condition():
#     i = 0
#     while i < 5:
#         i += 1
#         if i == 3:
#             continue
#         print(i)
        
# Print_By_Condition()




'''
26.  for와 range를 이용해서 아래와 같이 출력하시오

입력 및 출력 예시

출력
2 5 8 11 14 17 20 23 26 29
# '''
# def Print_By_Condition():
#     result = [str(x) for x in range(2, 30, 3)]
#     print(' '.join(result))
    
# Print_By_Condition()

'''
27. 아래와 같이 함수를 만들어서 코드를 최대한 짧게 해서 아래와 같이 출력하세요

입력 및 출력 예시

출력

****************************
***     차온유  0세      ***
****************************
****************************
***     차홍기  40세      ***
****************************
****************************
***     조성덕  29세      ***
****************************
****************************
***     이주엽  33세      ***
****************************
# '''
# userData = {
#     '차온유': 0,
#     '차홍기': 40,
#     '조성덕': 29,
#     '이주엽': 33
# }

# from io import StringIO

# def Print_Personal_Info(info: dict):
#     stringBuilder = StringIO() 
#     line_X = '*' * 28
#     short = '*' * 3

#     for name, age in info.items():
#         stringBuilder.write(f'{line_X}\n')
#         line = f'{short}\t {name}  {age}\t {short}\n'
#         stringBuilder.write(line)
#         stringBuilder.write(f'{line_X}\n')  

#     result = stringBuilder.getvalue()
#     print(result)

# Print_Personal_Info(userData)





'''
29.  가변 길이 매개변수(*변수)를 활용한 함수를 만들어서 숫자의 개수를 다르게 넣어주면 그 숫자들의  합을 리턴하는 함수를 만들어라
입력 및 출력 예시 

a = sum_total(1,2,3)
print(a)     // 6 출력됨 

a = sum_total(1,2,3,4,5,6,7,8,9,10)
print(a) 
'''
# def sum_total(*numbers : int) -> int:
#     result = 0
#     for i in numbers:
#         result += i
    
#     return result
        
# a = sum_total(1,2,3,4,5,6,7,8,9,10)
# print(a) 




'''
32.  현재시간을 기준으로 아래의 5가지 형식으로 날짜와 시간, 요일 등을 출력하시오 

출력결과 

2023년1월25일 23시29분50초
20230125 23:29:50
2023/01/25 23:29:50
수요일 01-25-2023, 23:29:50
11:29:50 PM
'''

