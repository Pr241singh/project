Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=20
>>> print(a&b)
0
>>> a=10
>>> b=3
>>> print(a&b)
2
>>> a=10
>>> b=3
>>> print(a|b)
11
>>> a=10
>>> b=3
>>> print(a^b)
9
>>> a=10
>>> b=3
>>> print(a~b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=10
>>> b=3
>>> print(a<<b)
80
>>> a=10
>>> b=3
>>> print(a>>b)
1
>>> a={1,2,3,4,5}
>>> print(5 in a)
True
>>> a={1,2,3,4}
>>> print(5 not in a)
True
>>> a=10
>>> b=2=
SyntaxError: cannot assign to literal
>>> a=10
>>> b=20
>>> print(a is b)
False
>>> print(a is not b)
True
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum = ",sum)
s1 = students()
print(s1)
<__main__.students object at 0x00000255D96CCBC0>
class car:
    color = "blue"

    
car1 = car()
print(car1.color)
blue
class car:
        color = "blue"
        brand = "mercedes"
s1 = student()
class student:
    name = "preeti"
    def _init_(self):
        print(self)
        print("adding new student in database..")

        
s1 = student()
print(s1)
<__main__.student object at 0x00000255D91DB800>
