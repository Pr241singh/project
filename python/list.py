Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
str= "preeti singh"
print(str(1:4))
SyntaxError: invalid syntax
print(str[1:4])
ree
print(str[0:4])
pree
print(str[1:])
reeti singh
print(str[1:len(str)])
reeti singh
print(str[-3:-1])
ng
str = "i am studying python from apna college"
print(str. endswith("ege"))
True
print(str. endswith("sin"))
False
print(str.upper())
I AM STUDYING PYTHON FROM APNA COLLEGE
print(str.lowerwith())
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(str.lowerwith())
AttributeError: 'str' object has no attribute 'lowerwith'
print(str.lower())
i am studying python from apna college
print(str.replace("0","a"))
i am studying python from apna college
print(str.replace("python","javascript"))
i am studying javascript from apna college
print(str.find("o"))
18
print(str.find("from"))
21
print(str.find("q"))
-1
print(str.count("from"))
1
print(str.count("o"))
3
str=input("enter your name")
enter your name preeti
print("length of your name : ", len(name))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print("length of your name : ", len(name))
NameError: name 'name' is not defined
print("length of your name : ", len(str))
length of your name :  7
light = "green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")

    
go
light="pink"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")

    
light is broken

marks = 75
if(marks>=90):
    print("A")
elif(marks>=80):
    print("B")
elif(marks>=70):
    print("C")
else:
    print("D")

    
C
num=14
rem=num%2
if(rem == 0):
    print("even")
else:
    print("odd")

    
even
a= 4
b= 5
c= 6
if(a>b and a>c):
    print("a is greater")
elif(b>c):
    print("b is greater")
else:
    print("c is greater")

    
c is greater
a= 8
b= 5
c= 6
if(a>b and a>c):
    print("a is greater")
elif(b>c):
    print("b is greater")
else:
    print("c is greater")

    
a is greater
a=10
b=15
c=13
d=8
if(a>b and a>c):
    print("a is greater",a)
elif(b>c):
    print("b is greater",b)
elif(c>d):
    print("c is greater",c)
else:
    print("d is greater",d)

    
b is greater 15
marks={94.4,96.5,85.4,79.9}
print(marks)
{96.5, 85.4, 94.4, 79.9}
print(marks[1])
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print(marks[1])
TypeError: 'set' object is not subscriptable
print(marks(1))
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(marks(1))
TypeError: 'set' object is not callable
print(marks{1})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(marks,{1})
{96.5, 85.4, 94.4, 79.9} {1}
print(marks[1])
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print(marks[1])
TypeError: 'set' object is not subscriptable
marks[1]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    marks[1]
TypeError: 'set' object is not subscriptable
marks{1}
SyntaxError: invalid syntax
marks(0)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    marks(0)
TypeError: 'set' object is not callable
print(marks{0}, marks{1})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
marks=[94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
[94.4, 87.5, 95.2, 66.4, 45.1]
print(marks[0])
94.4
print(marks[1])
87.5
print(len(marks))
5
student=["karan",95.4,17,"Delhi"]
print(student[0])
karan
student[0] = "Arjun"
print(student)
['Arjun', 95.4, 17, 'Delhi']
print(marks[1:4])
[87.5, 95.2, 66.4]
student.append(86.6)
print(student)
['Arjun', 95.4, 17, 'Delhi', 86.6]
list=[8,6,3,7]
list.sort()
print(list)
[3, 6, 7, 8]
>>> list.sort(reverse=True)
>>> print(list)
[8, 7, 6, 3]
>>> list=[z,y,p,a,d]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    list=[z,y,p,a,d]
NameError: name 'z' is not defined
>>> list=['z','y','p','a','d']
>>> list.sort()
>>> print(list)
['a', 'd', 'p', 'y', 'z']
>>> student=["karan",95.4,17,"Delhi"]
>>> list.reverse()
>>> print(list)
['z', 'y', 'p', 'd', 'a']
>>> list.insert(1,5)
>>> print(list)
['z', 5, 'y', 'p', 'd', 'a']
>>> list.pop(2)
'y'
>>> print(list)
['z', 5, 'p', 'd', 'a']
>>> tuple=('z', 5, 'p', 'd', 'a')
>>> print(type(tuple))
<class 'tuple'>
>>> print(tup[1])
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    print(tup[1])
NameError: name 'tup' is not defined
>>> print(tup(1))
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    print(tup(1))
NameError: name 'tup' is not defined
>>> print(tup{1})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(tuple[1])
5
