"""
class Person:
    def __int__(self, name):
        self.name=name

    def display(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self,name, roll_no):
        self.name= name
        self.roll_no= roll_no

    def show(self):
        print("Roll No:", self.roll_no)

s= Student("Ravi", 101)
s.display()
s.show()
"""
"""
class Employee:
    def __intit__(self, emp_id):
        self.emp_id= emp_id

    def work(self):
        print("Employee is working")

class Manager(Employee):
    def __init__(self,emp_id, team_size):
        self.emp_id= emp_id
        self.team_size= team_size

    def manage(self):
        print(f"manager manages {self.team_size} employees")

m= Manager(501,10)
m.work()
m.manage()
print(m.emp_id)
    
"""
"""
class BankAccount:
    def __init__(self, balance):
        self.balance= balance

    def deposit(self, amount):
        self.balance+= amount
        print("Balance:",self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, balance, rate):
        self.balance= balance 
        self.rate= rate

    def add_interest(self):
        self.balance*=(1+self.rate)
        print("balance after interest", self.balance)

s= SavingsAccount(1000, 0.05)
s.deposit(500)
s.add_interest()
"""
"""
class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name= name
        self.price= price

    def show_details(self):
        print(f"ID: {self.product_id}, Name: {self.name}, price: {self.price}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size, brand):
        self.product_id= product_id
        self.name= name
        self.price= price
        self.size= size
        self.brand= brand

    def show_clothing(self):
        print(f"clothing -> Brand: {self.brand}, size: {self.size}")


item= Clothing( 101, "T-shirt", 799, "L","Nike")
item.show_details()
item.show_clothing()
"""
"""
class Person:
    def __init__(self):
        self.type= "Person"

    def display(self):
        print("I am a person")

class Employee(Person):
    def __int__(self):
        self.role= "Employee"

    def work(self):
        print("I am working")

class Manager(Employee):
    def __init__(self):
        self.position="Manager"

    def work(self):
        print("I manage Employees")

m= Manager()
m.display()
m.work()
"""

"""
class Appliance:
    def __init__(self):
        self.type= "Appliance"

    def turn_on(self):
        print("Appliance is turned on")

class KitchenAppliance(Appliance):
    def __init__(self):
        self.category= "Kitchen Appliance"

    def use(self):
        print("Using Kitchen Appliance")

class Mixer(KitchenAppliance):
    def init__(self):
        self.name= "Mixer"

    def mix(self):
        print("Mixing food items")

m= Mixer()
m.turn_on()
m.use()
m.mix()

"""
"""
class Bank:
    def __init__(self):
        self.bname= "Bank"
    
    def bank_info(self):
        print("This is a bank")

class Account(Bank):
    def __init__(self):
        self.atype= "Account"

    def account_infor(self):
        print("This is an account")

class SavingsAccount(Account):
    def __init__(self):
        self.stype="Savings"

    def savings_info(self):
        print("This is a savings account")

s= SavingsAccount()
s.bank_info()
s.account_infor()
s.savings_info()

"""

# # class Shape:
# #     def __init__(self, length, width):
# #         self.length= length
# #         self.width= width

# #     def area(self):
# #         return self.length * self.width
    
# # class Rectangle(Shape):
# #     def __init__(self, length,width, perimeter_needed= False):
# #         self.length= length
# #         self.width= width
# #         self.perimeter_nedded= perimeter_needed

# #     def perimeter(self):
# #         return 2*(self.length*self.width)
    
# # class Box(Rectangle):
# #     def __init__(self,length,width,height):
# #         self.length= length
# #         self.width= width
# #         self.height= height

# #     def volume(self):
# #         return self.length*self.width*self.height
    
# # b= Box(10,5,3)
# # print("Area:",b.area())
# # print("perimeter:", b.perimeter())
# # print("Volume:", b.volume())

# class Product:
#     def __init__(self,price):
#         self.price- price

# class Clothing(Product):
#     def __init__(self,price,gst):
#         self.price=price
#         self.gst= gst

#     def price_with_gst(self):
#         return self.price+ (self.price*self.gst/100)
    
# class OrderItem(Clothing):
#     def __init__(self,price,gst,qty):
#         self.price=price
#         self.gst=gst
#         self.qty=qty

#     def total_price(self):
#         return self.price_with_gst()*self.qty
    
# oi= OrderItem(1000,12,3)
# print("Price+GST:", oi.price_with_gst())
# print("Total Order Price;", oi.total_price())

class Employee:
    def __init__(self, name, base_salary):
        self.name= name
        self.base_salary= base_salary

class Developer(Employee):
    def __init__(self,name,base_salary,bonus):
        self.name= name
        self.base_salary= base_salary
        self.bonus= bonus

    def salary_with_bonus(self):
        return self.base_salary + self.bonus
    
class PythonDeveloper(Developer):
    def __init__(self,name,base_salary,bonus,project_allowance):
        self.name= name
        self.base_salary= base_salary
        self.bonus= bonus
        self.project_allowance= project_allowance

    def total_salary(self):
        return self.salary_with_bonus() + self.project_allowance
    
p= PythonDeveloper("Ravi", 50000, 10000,5000)
print("Employee:", p.name)
print("salary+bonus:", p.salary_with_bonus())
print("Total_salary:", p.total_salary())
    



