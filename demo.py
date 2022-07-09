class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def Name(self):
        return False
class Employee(Person):
    def Name(self):
        return True
emp = Employee("Harshit")
print(emp.getName(),emp.Name())