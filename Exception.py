
try:
  print(10)
except NameError:
  print("An exception occurred")
except:
  print('Something Went Wrong')
else:
  print('Nothing Went Wrong')
  