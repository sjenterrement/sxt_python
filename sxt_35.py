Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> bts=[1 2]
SyntaxError: invalid syntax
>>> bts=[1,2]
>>> bts[0]
1
>>> del bts[0]
>>> bts
[2]
>>> b=bts.pop()
>>> b
2
>>> bts.append(1,2,5)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    bts.append(1,2,5)
TypeError: append() takes exactly one argument (3 given)
>>> bts.extend(3,6,7)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    bts.extend(3,6,7)
TypeError: extend() takes exactly one argument (3 given)
>>> bts
[]
>>> bts=[1,2,3,4,5,6,7]
>>> bts
[1, 2, 3, 4, 5, 6, 7]
>>> bts.pop(6)
7
>>> bts.pop(6)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    bts.pop(6)
IndexError: pop index out of range
>>> bts.remove(5)
>>> bts
[1, 2, 3, 4, 6]
>>> 
