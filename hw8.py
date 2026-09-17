class employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def display(self):
        print("NAME:{},ROLE:{}".format(self.name,self.role))
        
employee1=employee("priya","personal trainer")
employee1.display()

class trainer(employee):
    def __init__(self, name, role,specialization):
        employee.__init__(self,name, role)
        self.specialization=specialization
    def display(self):
        print("trainer's name:{},role:{},specialization:{}".format(self.name,self.role,self.specialization))
trainer1=trainer("navya","PT","physical education")
trainer1.display()

class yogainstructor(employee):
    def __init__(self, name, role,yoga_style):
        employee.__init__(self,name, role)
        self.yoga_style=yoga_style
    def display(self):
        print("instructor:{},role:{},yoga style:{}".format(self.name,self.role,self.yoga_style))
instructor1=yogainstructor("sreya","instructor","hatha yoga")  
instructor1.display() 

class multitrainer(trainer,yogainstructor):
    def __init__(self, name, role, specialization,yoga_style):
        trainer.__init__(self,name, role, specialization)
        yogainstructor.__init__(self, name, role, yoga_style)
        self.specialization=specialization
        self.yoga_style=yoga_style   
        
    def display(self):
        print("multi-trainer's name:{},role:{},specialization:{},yoga style:{}".format(self.name,self.role,self.specialization,self.yoga_style)) 
instructor1=multitrainer("rohan","special instructor","yoga science","ashtanga yoga")
instructor1.display()