Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bts=["jungkook",22]
>>> bts
['jungkook', 22]
>>> bts[0]
'jungkook'
>>> bts=list()
>>> bts=list(range(10))
>>> bts
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=list("jungkook")
>>> a
['j', 'u', 'n', 'g', 'k', 'o', 'o', 'k']
>>> list(range(0,10,2))
[0, 2, 4, 6, 8]
>>> a=x*2 for x in range(5)
SyntaxError: invalid syntax
>>> a=[x*2 for x in range(5)]
>>> a
[0, 2, 4, 6, 8]
>>> a==[x*2 for x in range(100) if x%9==0]
False
>>> a=[x*2 for x in range(100) if x%9==0]
>>> a
[0, 18, 36, 54, 72, 90, 108, 126, 144, 162, 180, 198]
>>> 
