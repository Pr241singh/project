Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> menu = {'pizza' : 40,
...         'pasta' : 50,
...         'Burgur' : 60,
...         'Salad' : 70,
...         'Coffee' : 80,}
>>> print("Welcome to Python restaurant")
Welcome to Python restaurant
>>> print("pizza : Rs40\npasta : Rs50\nBurgur : Rs60\nSalad : Rs70\nCoffee : Rs80")
pizza : Rs40
pasta : Rs50
Burgur : Rs60
Salad : Rs70
Coffee : Rs80
>>> order_total = 0
>>> item_1 = input("Enter the name of item you want to order = ")
Enter the name of item you want to order = pizza
>>> if item_1 in menu:
...     order_total += menu[item_1]
...     print(f"your order {item_1} has been added to your order")
... 
...     
your order pizza has been added to your order
>>> else:
...     
SyntaxError: invalid syntax
>>> if item_1 in menu:
...     order_total += menu[item_1]
...     print(f"your order {item_1} has been added to your order")
... else:
...     print("ordered item {item_1} is not available yet")
... 
...     
your order pizza has been added to your order
>>> another_order = input("Do you want to add another item? (Yes/No) ")
Do you want to add another item? (Yes/No) No
>>> if another_order == "Yes":
...     item_2 = input("Enter the name of second item you want to order = ")
...     if item_2 in menu:
...         order_total += menu[item_2]
...         print(f"your order {item_2} has been added to your order")
    else:
        print(f"ordered item {item_1} is not available yet")

        
print(f"The total amount of items to pay is {order_total}")
The total amount of items to pay is 80

"""inputs we need from the user
 Total rent
 Total food ordered for snacking"""
 
rent= int(input("Enter your hostle/flat rent = "))
food= int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of person living in room/flat = "))
total_bill = electricity_spend*charge_per_unit
output = (food + rent + total_bill ) // persons
print("each person will pay = ", output)
Output:    
Enter your hostle/flat rent = 5000
Enter the amount of food ordered = 2000
Enter the total of electricity spend = 1500
Enter the charge per unit = 10
Enter the number of person living in room/flat = 3
each person will pay =  7333

import random
passlen = int(input("Enter the length of the password : "))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_?"
p = "".join(random.sample(s, passlen ))
print("Gnerated password :  ", p)
Output :
Enter the length of the password : 8
Gnerated password :   47oHRJyu

import os
def show_file_size(size):
    kb = size/1024
    mb = size/1024
    print("The file size in - ")
    print("Bytes : {}". format(size))
    print("Kilobyte (KB) : {0:.2f}". format(kb))
    print("Megabyte (MB) : {0:.2f}". format(mb))

    
file_path = r"C:\Users\DELL\OneDrive\Documents\SQL.docx"
size = os.stat(file_path).st_size
show_file_size(size)
The file size in - 
Bytes : 14281
Kilobyte (KB) : 13.95
Megabyte (MB) : 13.95
