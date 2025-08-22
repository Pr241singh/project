Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> collection = set()
>>> print(type(collection))
<class 'set'>
>>> collection.add(1)
>>> collection.add(2)
>>> collection.add(1)
>>> print(collection)
{1, 2}
>>> collection.remove(1)
>>> print(collection)
{2}
>>> print(len(collection))
1
>>> collection.clear()
>>> print(collection)
set()
>>> collection = {"hello","apna college","world","coding","python"}
>>> python(collection.pop())
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    python(collection.pop())
NameError: name 'python' is not defined
>>> print(collection.pop())
python
>>> print(collection.pop())
apna college
>>> set1= {1,2,3}
>>> set2= {3,4,5,6}
>>> print(set1.union(set2))
{1, 2, 3, 4, 5, 6}
>>> print(set1.intersection(set2))
{3}
>>> classroom= {"python","java","c++","python","javascript","python","java","java","c++","c"}
>>> print(classroom)
{'python', 'c++', 'java', 'c', 'javascript'}
>>> print(len(classroom))
5
