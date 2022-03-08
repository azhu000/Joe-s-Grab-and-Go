from click import password_option
import mysql.connector

conn = mysql.connector.connect(user='root', password="MyDBserver1998", host="localhost",database='test_schema')


class User: #Superclass
    def __init__(self, user_id, user_password, bizID):
        self.user_id = user_id
        self.user_password = user_password
        self.bizId = bizID
        
    @property
    def user_id(self):
        return f'{self.user_id}'
    
    @property
    def user_password(self):
        return f'{self.user_password}'
    
    @property
    def bizId(self):
        return f'{self.bizID}'
    
    
    
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
        super().__init__(user_id, user_password, bizID
                         
                         )
        
#subclass of employee (Chef)
class Chef(Employee):
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
#subclass of employee (Delivery)
class Delivery(Employee):
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
 #subclass of user named VISITOR       
class Visitor(User):
    def __init__(self, user_id, user_password, bizID):
        super().__init__(user_id, user_password, bizID)
        
        
        
