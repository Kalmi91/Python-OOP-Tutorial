# Property Decorators

# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return ' {}.{}@email.com'.format(self.first, self.last)
#
#     @property
#     def fullname(self):
#         return ' {} {}'.format(self.first, self.last)
#
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#
#     @fullname.deleter
#     def fullname(self):
#         print('Deleted Name!')
#         self.first = None
#         self.last = None
#
#
# emp_1 = Employee('Hohn', 'Pocak')
# emp_1.first = 'Jim'
#
# emp_1.fullname = 'Corey Sopon'
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
# del emp_1.fullname

# Special Dunder Methods
# Te amof
# class Employee:
#
#     raise_amt = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)
#
#     def __repr__(self):
#         return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
#
#     def __str__(self):
#         return '{} - {}'.format(self.fullname(), self.email)
#
#     def __add__(self, other):
#         return self.pay + other.pay
#
#     def __len__(self):
#         return len(self.fullname())
#
#
# emp_1 = Employee('Cody', 'Bomba', 50000)
# emp_2 = Employee('Test', 'Boci', 60000)
#
# print(len(emp_1))

# print(len('test'))
# print('test'.__len__())

# print(emp_1 + emp_2)

#print(emp_2.email)
# print(emp_2)
#
# print(repr(emp_1))
# print(str(emp_1))
#
# print(emp_1.__repr__())
# print(emp_1.__str__())



# Empty Class needs pass
# class Employe:
#     pass

# class  Employee:
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def  __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return print("It's not a workday")
#         return print("It's a workday")
#
# class Developer(Employee):
#     raise_amt = 1.1
#
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
#
# class Manager(Employee):
#
#     def __init__(self, first, last, pay, employess=None):
#         super().__init__(first, last, pay)
#         if employess is None:
#             self.employees = []
#         else:
#             self.employees = employess
#
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def remove_emp(self, emp):
#         if emp is self.employees:
#             self.employees.remove(emp)
#
#     def print_emps(self):
#         for emp in self.employees:
#             print('--->', emp.fullname())
#
# dev_1 = Developer('Cody', 'Fehér', 50000, 'Python')
# emp_2 = Employee('test', 'user', 60000)
#
# mrg_1 = Manager('Sara','Smith', 99000, [dev_1])
#
# print(isinstance(mrg_1, Employee))
# print(issubclass(Developer, Employee))


# print(mrg_1.email)
# mrg_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# look what did we inherited
#print(help(Developer))

## Import ime and use classmethood
# import datetime
# my_date = datetime.date(2016, 7, 11)
#
# print(Employee.is_workday(my_date))

#Creating employee from string
#
# emp_str_1 = 'Bi-kantor-70000'
# emp_str_2 = 'jhon-sarga-40000'
# emp_str_3 = 'telenor-pavalak-30000'
#
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)


# print(emp_1.email)
# print(emp_2.email)
#
# print(emp_1.fullname())
# Employee.fullname((emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.__dict__)

# # Employee.raise_amount = 1.05

# Employee.set_raise_amt(1.06)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.num_of_emps)

