# Questuion 1: Square Numbers and Return Their Sum

# Sample properties 1, 3, 5
# Sample method output 35
# Coding Starts From Below Line

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(x,y,z)
    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2
    
p = Point(1, 3, 5)
result = p.sqSum()
print(result)

# Output = 1,3,5
# Output = 35



# Question 2: Implement a Calculator Class


class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num2 / self.num1
pass
    
obj = Calculator(10, 94)
print(obj.add())       
print(obj.subtract())  
print(obj.multiply())  
print(obj.divide())  


# Output:#104
#         84
#         940
#         9.4





#3. Implement the Complete Student Class

class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber


student = Student()
student.setName("Robin Hudd")
student.setRollNumber(7)
name = student.getName()
rollNumber = student.getRollNumber()
print("Name:", name)
print("Roll Number:", rollNumber)

# output
# Name: Robin Hudd
# Roll Number: 7





# 4: Implement a Banking Account

class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, account_holder, balance, interestRate):
        super().__init__(account_holder, balance)
        self.interestRate = interestRate

account1 = SavingsAccount("Vijay Malya", 50000000, 5)
print("Account Holder     : ", account1.account_holder)  
print("Account Balance    : ", account1.balance)  
print("Interest Rate(%)   : ", account1.interestRate)  

 
# output  # Vijay Malya is the account holder and 50000000 is the account balance and 5% is the rate of interest.
# Account Holder     :  Vijay Malya
# Account Balance    :  50000000
# Interest Rate(%)   :  5





# 5: Handling a Bank Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    def withdrawal(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def getBalance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def interestAmount(self):
        return (self.balance * self.interestRate)/100

demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print(demo1.getBalance()) 

demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.withdrawal(500)
print(demo1.getBalance()) 

demo1 = SavingsAccount("Ashish", 2000, 5)
print(demo1.interestAmount()) 

# output 
#2500
#1500
#100.0