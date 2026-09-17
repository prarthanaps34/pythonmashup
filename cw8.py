class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        print("name is {} age is {}".format(self.name,self.age))
person1=person('anu',28)

person1.show_details()

class employee(person):
    def __init__(self, name, age,employee_id):
        super().__init__(name, age)
        self.employee_id=employee_id
        
    def show_details(self):
        print("the name is {}.{} years old and employee id is {}".format(self.name,self.age,self.employee_id))
employee1 = employee("riya",26,"A141")
employee1.show_details()

class parttime(person):
    def __init__(self, name, age,working_hour):
        super().__init__(name, age)
        self.working_hour=working_hour
        
    def show_details(self):
        print("name:{},age:{},working hours:{}".format(self.name,self.age,self.working_hour))
partime_employee=parttime("arun",30,7.5)
partime_employee.show_details()

class consultant(employee,parttime):
    def __init__(self, name, age, employee_id,working_hour,project_name):
        person.__init__(self,name, age)
        self.employee_id=employee_id
        self.working_hour=working_hour
        self.project_name=project_name
        
    def show_details(self):
        print("consultants name:{},age:{},employee id:{},working hours:{},project name:{}".format(self.name,self.age,self.employee_id,self.working_hour,self.project_name))
    
consultant_details=consultant("arya",38,"A125",8.5,"web designing")
consultant_details.show_details()
    

    