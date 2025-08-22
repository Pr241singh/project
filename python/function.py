Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def cal_sum(a,b):
    sum = a+b
    print(sum)
    return sum

cal_sum(5,10)
15
15
cal_sum(9,9)
18
18
def print_hello():
    print("hello")

    
print_hello()
hello
def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

cal_avg(5,10,15)
10.0
10.0
def print_len(list):
    print(list)

    
cities = ["delhi","gurugran","pune","noida","mumbai"]
print_len(cities)
['delhi', 'gurugran', 'pune', 'noida', 'mumbai']
def print_len(list):
    print(len(list))

    
cities = ["delhi","gurugran","pune","noida","mumbai"]
print_len(cities)
5
nums = [2,4,6,8,9,4,3]
print_len(nums)
7
def print_list(list):
    for item in list:
        print(item,end=" ")

        
print_list(cities)
delhi gurugran pune noida mumbai 
n=5
fact = 1
for i in range(1,n+1):
    fact+=1
print(fact)
SyntaxError: invalid syntax

n=5
fact=1
for i in range(1,n+1):
    fact+=i
print(fact)
SyntaxError: invalid syntax
n=5
fact = 1
for i in range(1,n+1):
    fact*=1
print(fact)
SyntaxError: invalid syntax
n=5
fact=1
for i in range(1,n+1):
    fact*=i

    
print(fact)
120
def cal_fact(n):
    n=5
fact=1
for i in range(1,n+1):
    fact*=i
    
SyntaxError: invalid syntax
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i

        
print(fact)
120
cal_fact(6)
print(fact)
120
cal_fact(6)

KeyboardInterrupt
cal_fact(4)

def convertor(usd_value):
    inr_value = usd_value*83
    print(usd_value,"USD = ",inr_value, "INR")

    
convertor(1)
1 USD =  83 INR
convertor(73)
73 USD =  6059 INR
def show(n):
    print(n)
    show(5)

    
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
SyntaxError: invalid syntax
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

    
show(5)
5
4
3
2
1
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n

print(fact(4))
24
print(fact(5))
120
def cal_sum(n);
SyntaxError: expected ':'
>>> def cal_sum(n):
...     if(n==0):
...         print(n-1) + n
... 
...         
>>> cal_sum(5)
>>> def cal_sum(n):
...     if(n==0):
...         return 0
...     return cal_sum(n-1) + n
... 
>>> sum = cal_sum(5)
>>> print(sum)
15
>>> def print_list(list,idx):
...     if(idx == len(list)):
...         return
...     print(list[idx])
...     print_list(list, idx+1)
... 
...     
>>> fruit = ["mangoes","litchi","banana","apple"]
>>> print_list(fruit)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    print_list(fruit)
TypeError: print_list() missing 1 required positional argument: 'idx'
>>> def print_list(list,idx=0):
...     if(idx == len(list)):
...         return
...     print(list[idx])
...     print_list(list, idx+1)
... 
...     
>>> fruit = ["mangoes","litchi","banana","apple"]
>>> print_list(fruit)
mangoes
litchi
banana
apple
