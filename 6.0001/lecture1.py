# type
print(type(5))    # <class 'int'>
print(type(3.0))  # <class 'float'>
print(type(True)) # <class 'bool'>
print(type(None)) # <class 'NoneType'>

# type conversion
print(float(3)) # 3.0
print(int(3.9)) # 3

# operators on ints and floats
print(3 + 2)  # 5
print(3 - 2)  # 1
print(3 * 2)  # 6
print(3 / 2)  # 1.5
print(3 // 2) # 1
print(3 % 2)  # 1
print(3 ** 2) # 9

# precedence, ** > (*,/,//,%) > (+,-)
print(5 + 4 * 3 ** 2)     # 41
print(((5 + 4) * 3) ** 2) # 729

# different operators of same precedence executed from left to right
print(5 * 4 // 3)   # 6
print(5 * (4 // 3)) # 5

# binding and rebinding
x = 1  
print(x)  # 1
y = x 
print(y)  # 1
x = x + 1 
print(x)  # 1
print(y)  # 2
