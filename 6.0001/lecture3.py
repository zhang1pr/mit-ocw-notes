# string
a = 'abc'
print(len(a))  # 3
print(a[1])    # b
print(a[-3])   # a

# slice string
b = 'abcdefgh'
print(b[3:10:2]) # dfj
print(b[4:1:-2]) # ec
print(b[::])     # abcdefgh
print(b[::-1])   # hgfedcba

# iterate string
c = 'xyz'
for char in c:
  c += char
print(c)       # xyzxyz
