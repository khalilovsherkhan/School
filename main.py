class student:
    school_name = ' ABS school '
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        cls.school_name = school_name


    def show(self):
        print(self.name, self.age, 'School:', student.school_name)


jessa = student('Jessa', 20)
jessa.show()



student.change_school('XYZ school')
jessa.show()
        
        



from datetime import date

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):

        return cls(name, date.today().year - birth_year)
    

    def show(self):
        print(self.name + "'s age is: " + str(self.age))


jessa = student('Jessa', 20)
jessa.show



joy = student.calculate_age("Joy", 1995)
joy.show




class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)



Employee.sample(10)

emp = Employee
emp.sample(10)



class Employee(object):
    def __init__(self, name,  salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name



    @staticmethod

    def gather_requirment(project_name):
        if project_name == "ABS Project":
            requirement = ['task_1', 'task_2' 'task_3']

        else:

            requirement = ['task_1']

        return requirement
    

    def work(self):

        requirement =  self.gather_requirment(self.project_name)
        for task in requirement:
            print('Comleted', task)

emp = Employee('Kelly', 12000, 'ABS Project' )
emp.work




class Test :
    @staticmethod
    def static_method_1():
        print('ststic method 1')

    @staticmethod
    def static_method_2():
        Test.static_method_1()


    classmethod
    def class_method_1(cls):
        cls.class_method_1()



Test.class_method_1()
