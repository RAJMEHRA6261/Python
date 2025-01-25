Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 100
print(a)
100
a
100
b=56.7
c=6+4j
v=True
s="Hello"
type(a)
<class 'int'>
type(b)
<class 'float'>
type(c)
<class 'complex'>
type(v)
<class 'bool'>
type(s)
<class 'str'>
isinstance(a,int)
True
isinstance(b,float)
True
isinstance(c,complex)
True
isinstance(v,bool)
True
isinstance(s,str)
True
int(b)
56
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
100.0

x=float(a)
x
100.0
type(x)
<class 'float'>
str(c)
'(6+4j)'
float(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> complex(a)
(100+0j)
>>> complex(b)
(56.7+0j)
>>> b
56.7
>>> 
============================================= RESTART: D:/1.py =============================================
The value of a is  100
The value of b is  200
>>> 
============================================= RESTART: D:/1.py =============================================
The value of a is 100 and the value of b is 200
>>> 
============================================= RESTART: D:/1.py =============================================
The value of a is 100 and the value of b is 200
>>> 
============================================= RESTART: D:/1.py =============================================
The value of a is 100 and the value of b is 200
The value of a is 200 and the value of b is 100
>>> 
============================================= RESTART: D:/1.py =============================================
The value of a is 100 and value of b is 200
>>> ord('A)
...     
SyntaxError: unterminated string literal (detected at line 1)
>>> ord('A')
...     
65
>>> ord("B")
...     
66
>>> chr("a")
...     
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    chr("a")
TypeError: 'str' object cannot be interpreted as an integer
>>> ord(3)
...     
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    ord(3)
TypeError: ord() expected string of length 1, but int found
>>> ord('3')
...     
51
>>> id(a)
...     
140729794889240
>>> chr(100)
...     
'd'
