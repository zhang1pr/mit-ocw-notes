# string
a, b = 'hi', 'chao'
print((a + ' ') * 3, b) # hi hi hi  chao

# input/output
print(input('input number 5') * 5) # 55555

# comparison operators on ints and floats
num1, num2, num3 = 3, 3, 3.0
print(num1 > num2)  # False
print(num1 < num2)  # False
print(num1 >= num3) # True
print(num1 <= num3) # True
print(num2 == num3) # True
print(num2 != num3) # False

# comparison operators on strings
str1, str2, str3 = 'a', 'ab', 'AB'
print(str1 > str2)  # False
print(str1 < str2)  # True
print(str1 >= str3) # True
print(str1 <= str3) # False
print(str2 == str3) # False
print(str2 != str3) # True

# login operators
x, y = False, True
print(not x)   # True
print(x and y) # False
print(x or y)  # True

# if, else and elif
if x:
  print('x is truthy')
elif y:
  print('y is truthy') # y is truthy
else:
  print('none is truthy') 

# while loop
m = 1
while m < 5:
  m = m + 2
print(m) # 5    

# for loop and range(start, stop, step=1)
for n in range(1, 5, 2):
  pass
print(n) # 3

# break
for o in range(1, 5, 2):
  if o >= 3:
    print('break the loop') # break the loop
    break
else:
  print('loop finishes without break')  
