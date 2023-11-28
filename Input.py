# money = input('type Money : ')

# money_float = float(money)
# #info = f'money : {money_float:,.0f}' # 50000 => 50,000
# info = f'money : {money_float:.2f}' # 50000.87458 => 50000.87
# print(info)

# username = input('Enter User Name : ')
# print(f'User Name = {username}')


# quantity = 3
# itemno = 567
# price = 49

# myOrder = f'I want {quantity} of item{itemno} for {price:.2f} Dollars'

# print(myOrder)

# txt = '    ABC  abc abc  '
# result = txt.strip()
# spaceDeleted = txt.replace(' ', '')
# lower = txt.casefold()
# lower_ = txt.lower()
# print(lower)


# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]

# fruits.discard('banana')
# #fruits.update(more_fruits)
# print(fruits)


# y = " Hello abs Absolutely above cab go bye a boy able "
# y = ''.join(y)
# x = 'apple'
# x = ''.join(dict.fromkeys(x))
# print(y)

from collections import deque

#print(dir(deque))

queue = deque()

for i in range(10):
    queue.append(i)


print(queue)
    
queue.reverse()

print(queue)
