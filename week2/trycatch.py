
try:
    a = '32s'
    b = int(a)
except ValueError:
    b=0
    print('invalid string for interger')