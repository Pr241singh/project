Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Student:
    name = "karan"
    def __init__(self, fullname):
        self.name = fullname
        print('creating new student in database..')
  
# creating object
s1 = Student("karan")
print(s1.name)
#print(s1.name)
#class Car:
    #color = "blue"
    #brand = "mercedes"
#car1  = Car()
#print(car1.color)
#print(car1.brand)
SyntaxError: invalid syntax
class Student:
    name = "karan"
    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks = marks
        print('creating new student in database..')
  
# creating object
s1 = Student("karan",97)
print(s1.name, s1.marks)
s2 = Student("arjun",95)
print(s2.name, s2.marks)
SyntaxError: invalid syntax
crearing new student in database..
karan 97
crearing new student in database..
arjun 95
SyntaxError: invalid syntax
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your average score is:" ,sum/3)
        
s1 = Student("tony", [99, 98, 97])
s1.get_average()
s1.name = "ironman"
s1.get_average()
SyntaxError: invalid syntax
>>> hi tony your average score is: 98.0
... hi ironman your average score is: 98.0
... 
SyntaxError: invalid syntax
>>> class student:
...     @staticmethod
...     def college():
...         print("ABC college")
... 
...         
>>> class Account:
...     def __init__(self, bal, acc):
...         self.balance = bal
...         self.account = acc
...     def debit(self, amount):
...         self.balance -= amount
...         print("Rs", amount, "was debited")
...         print("total balance : ", self.get_balance())
...         
...     def credit(self, amount):
...         self.balance += amount
...         print("Rs", amount, "was credited")
...         print("total balance : ", self.get_balance())
...         
...     def get_balance(self):
...         return self.balance
...         
... account1 = Account(10000, 12345)
... print(account1.balance)
... print(account1.account)
... account1.debit(1000)
... account1.credit(500)
SyntaxError: invalid syntax
>>> 10000
... 12345
... Rs 1000 was debited
... total balance :  9000
... Rs 500 was credited
... total balance :  9500
SyntaxError: multiple statements found while compiling a single statement
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pass())
output : 12345
abcde
None
class person:
    __name = "anonymous"
    def __hello():
        print("hello person!")
    def welcome(self):
        __hello()
    
p1 = person()
print(p1.welcome)
output : <bound method person.welcome of <__main__.person object at 0x7e51ea645610>>
class Car:
    color = "black"
    def start():
        print("car started..")
    def stop():
            print("car stopped.")
            
class Toyatocar(Car):
    def __init__(self, name):
        self.name = name
        
car1 = Toyatocar("fortuner")
car2 = Toyatocar("thar")

print(car1.color)
output : black
class Car:
    def start():
        print("car started..")
    def stop():
            print("car stopped.")
            
class Toyatocar(Car):
    def __init__(self, brand):
        self.brand = brand
        
class Fortuner(Toyatocar):
    def __init__(self, type):
        self.type = type
        
car1 = Fortuner("diesel")
car1.start()
class A:
    varA = "welcome to class A"
    
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class C"
    
c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
output : welcome to class C
         welcome to class B
         welcome to class A
class Person:
    name = "anomynous"
    
    def changename(self, name):
        self.name = name
    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = Person()
p1.changename("preeti singh")
print(p1.name)
print(Person.name)
output : preeti singh
         preeti singh

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        #self.percentage =str((self.phy + self.chem + self.math)/3)+"%"
   # def calcpercentage(self):
        # self.percentage =str((self.phy + self.chem + self.math)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)+"%"
stu1 = Student(99, 98, 97)
print(stu1.percentage)
    
stu1.phy = 86
print(stu1.percentage)
output : 98.0%
         93.66666666666667%
         
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)
        
    def __sub__(self, num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newreal, newimg)
num1 = Complex(4,8)
num1.shownumber()
num2 = Complex(2,4)
num2.shownumber()
num3 = num1 - num2
num3.shownumber()
output: 4 i + 8 j
2 i + 4 j
2 i + 4 j

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
        
    def perimeter(self):
        return 2 * 3.14 * self.radius
        
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())
output : 1384.74
131.88

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showdetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")
        
engg1 = Engineer("elon musk", 40)
engg1.showdetails()
    
        
e1 = Employee("accountant","finance","60,000")
e1.showdetails()
output : role = Engineer
dept = IT
salary = 75,000
role = accountant
dept = finance
salary = 60,000

odr1 = Order("chips", 20)
output : True

import random
target = random.randint(1,100)

while True:
    userchoice =int(input("guess the target or quit : "))
    if(userchoice == "quit"):
        break
    userchoice = int(userchoice)
    if(userchoice == target):
        print("success : correct guess!!")
        break
    elif(userchoice < target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number was too big. Take a smaller guess..")
print("____GAME OVER_____")
output : guess the target or quit : 50
your number was too small. Take a bigger guess..
guess the target or quit : 80
your number was too small. Take a bigger guess..
guess the target or quit :

import random
import string

password_len = 12
charvalues = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(password_len):
    password += random.choice(charvalues)

print("your random password is : ", password)
output : your random password is :  \8Y=w7;MkaR.

    



        
    
        
