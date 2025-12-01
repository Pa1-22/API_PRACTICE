# As a HR manager I want to manage the details of employee

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def domain(self):
        print(f"Employee ID is {self.id} and name is {self.name}")


class Hr(Employee):
    def __init__(self, id, name, domain):
        super().__init__(id, name)
        self.domain = domain

    def manage(self):
        print(f"Employee ID is {self.id} and name is {self.name}, HR manages {self.domain}")


class Hrmanager(Hr):
    def __init__(self, id, name, domain, department):
        super().__init__(id, name, domain)
        self.department = department

    def manage_details(self):
        print(f"HR Manager {self.name} is managing the details of department {self.department}")


def display(manage=None):
    print("The details:")
    if type(manage) is Hrmanager:   
        print(f"id: {Hrmanager.id}, name: {Hrmanager.name}, domain: {Hrmanager.domain}, department: {Hrmanager.department}")
    elif type(manage) is Hr:
        print(f"id: {Hr.id}, name: {Hr.name}, domain: {Hr.domain}")
    elif type(manage) is Employee:
        
        print(f"id: {Employee.id}, name: {Employee.name}")
    else:
        print(" no object detected ") 




manage = Hrmanager(1, "Pallavi", "Recruitment", "Human Resource")

display(manage)

manage= Hr(1,"sam","cse")

display(manage)

manage=Employee(1,"ram")

display(manage)

manage.