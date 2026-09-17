class account:
    def __init__(self,name,balance):
        self._name=name
        self._balance=balance
    def __add__(self, other):
        return self._balance + other._balance   
        
class savingsaccount(account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        
    def calculate_interest(self):
        return self._balance*0.05
    
class currentaccount(account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        
    def calculate_interest(self):
        return self._balance*0.02  
    

    
savings1=savingsaccount("ravi",10000)
current1=currentaccount("anjali",15000)
total_balance = savings1 + current1


print("Name:", savings1._name) 
print("Balance:", savings1._balance) 
print("Interest:", savings1.calculate_interest())

print("Name:", current1._name) 
print("Balance:", current1._balance) 
print("Interest:", current1.calculate_interest())

print("Total Balance:", total_balance)