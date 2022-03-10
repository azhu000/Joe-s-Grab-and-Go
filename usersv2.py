from pickle import TRUE
from click import password_option
import mysql.connector

#conn = mysql.connector.connect(user='root', password="MyDBserver1998", host="localhost",database='test_schema')


class User: #Superclass
    def __init__(self, user_id, user_password, bizID):
        self._user_id = user_id
        self._user_password = user_password
        self._bizId = bizID
        
    @property
    def user_id(self):
        return f'{self._user_id}'
    
    @property
    def user_password(self):
        return f'{self._user_password}'
    
    @property
    def bizId(self):
        return f'{self._bizID}'
    
    
    
class Customer(User): #customer subclass
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
        
#customer subclass (VIP)
class VIP(Customer):
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
####employee subclass
class Employee(User): 
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
######subclass of employee (Manager)        
class Manager(Employee): 
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
#subclass of employee (Chef)
class Chef(Employee):
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
#subclass of employee (Delivery)
class Delivery(Employee):
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
 #subclass of user named VISITOR    //or maybe make this a separate class    
class Visitor(User):
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
test = User(1,123, 1)
cust = Customer(3,"12345", 2)

vip_test = VIP(3,"11234", 5)

print(test.user_id)

print(cust.user_password)

print(vip_test.user_id)