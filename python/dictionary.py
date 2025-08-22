Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list1=[1,2,3]
list2=[1,2,3]
preeti=list1.copy()
preeti.reverse()

if(preeti==list1):
    print("palidrone")
else:
    print("not palidrone")

    
not palidrone
grade=("c","d","a","a","b","b","a")
print(grade.count("a"))
3
grade=[c","d","a","a","b","b","a"]
       
SyntaxError: unterminated string literal (detected at line 1)
grade=[c,d,a,a,b,b,a]
       
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    grade=[c,d,a,a,b,b,a]
NameError: name 'c' is not defined
grade=["c","d","a","a","b","b","a"]
       
grade.sort()
       
print(grade)
       
['a', 'a', 'a', 'b', 'b', 'c', 'd']
info={ "name" : "preeti"
       "key" : "value"
       
SyntaxError: '{' was never closed
info={ "name" : "preeti",
       "key" : "value",
       "learn" : "coding",
       "age" : 18,
       "is_adult" : True,
       }
       
print(info)
       
{'name': 'preeti', 'key': 'value', 'learn': 'coding', 'age': 18, 'is_adult': True}
print(info("name"))
       
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(info("name"))
TypeError: 'dict' object is not callable
print(info["name"])
       
preeti
print(info[age])
       
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(info[age])
NameError: name 'age' is not defined
print(info["age"])
       
18
print(info["key"])
       
value
info["name"]= "sreeti"
       
print(info["name"])
       
sreeti
info["surname"]= "singh"
       
print(info)
       
{'name': 'sreeti', 'key': 'value', 'learn': 'coding', 'age': 18, 'is_adult': True, 'surname': 'singh'}

student = {"name" : "preeti singh",
           "subjects" : {
               "physics" : 95,
               "chemistry" : 96,
               "math" : 85,
               "english" : 98
               }
           }
       
print(student)
       
{'name': 'preeti singh', 'subjects': {'physics': 95, 'chemistry': 96, 'math': 85, 'english': 98}}
print(student["subjects"])
       
{'physics': 95, 'chemistry': 96, 'math': 85, 'english': 98}
print(student["subjects"]["chemistry"])
       
96
print(student.keys())
       
dict_keys(['name', 'subjects'])
print(list(student.keys()))
       
['name', 'subjects']
print(student.len())
       
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(student.len())
AttributeError: 'dict' object has no attribute 'len'
print(len(student))
       
2
print(student.values())
       
dict_values(['preeti singh', {'physics': 95, 'chemistry': 96, 'math': 85, 'english': 98}])
KeyboardInterrupt
print(student.items())
       
dict_items([('name', 'preeti singh'), ('subjects', {'physics': 95, 'chemistry': 96, 'math': 85, 'english': 98})])
print(student.get("name"))
       
preeti singh
student.update(("city" : "delhi"))
       
SyntaxError: invalid syntax
student.update("city" : "delhi")
       
SyntaxError: invalid syntax
>>> info.update(("city" : "delhi"))
...        
SyntaxError: invalid syntax
>>> student.update(("city" : "delhi")
...                
SyntaxError: invalid syntax
>>> student.update(("city" : "delhi")
...                
SyntaxError: invalid syntax
>>> student.update({"city" : "delhi"})
...                
>>> print(student)
...                
{'name': 'preeti singh', 'subjects': {'physics': 95, 'chemistry': 96, 'math': 85, 'english': 98}, 'city': 'delhi'}
>>> set={1,2,3,"hello","world"}
...                
>>> print(set)
...                
{'hello', 1, 2, 3, 'world'}
>>> print(type(set))
...                
<class 'set'>
>>> print(len(set))
...                
5
>>> empty=set{}
...                
SyntaxError: invalid syntax
>>> empty=set()
...                
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    empty=set()
TypeError: 'set' object is not callable
>>> collection = set() #empty set
...                
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    collection = set() #empty set
TypeError: 'set' object is not callable
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = dict1.copy()
print(dict2)
{'Name': 'Zara', 'Age': 7}
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print(seq)
('name', 'age', 'sex')
print(dict)
{'name': None, 'age': None, 'sex': None}
dict = dict.fromkeys(seq,10)
print(dict)
{'name': 10, 'age': 10, 'sex': 10}
dict.get('Age')
print(dict)
{'name': 10, 'age': 10, 'sex': 10}
dict = {'Name': 'Zabra', 'Age': 7}
dict.get('Age')
7
count=1
while count<=5:
    print("hello world")
    count+=1
print(count)
i=1
while i<=5:
    print("I love you mumma",i)
    i+=1
i=5
while i>=1:
    print(i)
    i-=1
i=1
while i<=100:
    print(i)
    i+=1
i=100
while i>=1:
    print(i)
    i-=1
n=int(input("enter your number :"))
i=1
while i<=10:
    print(n*i)
    i+=1
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(nums):
    print(idx)
    idx+=1
nums=(1,4,9,16,25,36,49,64,81,100)          output:
x=36                                         found at idx 5
i=0
while i< len(nums):
    if(nums[i]==x):
        print("found at idx",i)
    i+=1
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of code")
i=1
while i<=10:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1
vage=["potatoes","onion","lady finger"]
for num in vage:
    print(num)
element=[1,4,9,16,25,36,49,64,81,100]
for list in element:
    print(list)
element=(1,4,9,16,25,36,49,64,81,49)
x = 49
idx=1
for list in element:                        Output: number found at idx 7
    if(list==x):
        print("number found at idx",idx)
        break
    idx+=1
                   
