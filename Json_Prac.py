import json
import Util_Module


'''
Json To Python
'''
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
#print(y)
'''
Json To Python
'''


'''
Python To Json
'''
# a Python object (dict):
x_ = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
#y_ = json.dumps(x_)

# the result is a JSON string:
#print(y_)

'''
Python To Json
'''

# info = Util_Module.info
# with open('fileName.Json', 'w') as file :
#     json.dump(info, file)
# #print(toJson)
# json.loads()

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent= 4, separators= (',', ' : ')))
