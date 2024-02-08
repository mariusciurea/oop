"""OOP Tutorial"""
from datetime import date, datetime


class Employee:
    """Employee class"""
    yearly_amount = 1.2
    number_of_employees = 0
    holidays = 21

    def __new__(cls, first, last, salary=1000):
        obj = super().__new__(cls)
        return obj

    def __init__(self, first, last, salary=1000):
        """Employee constructor"""

        self.first_name = first
        self.last_name = last
        self.income = salary

        Employee.number_of_employees += 1

    @property
    def email(self):
        """Return employee email"""
        if self.first_name and self.last_name:
            return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'
        return None

    @email.setter
    def email(self, mail):
        """Email setter -> cristi.voicu@company.com"""
        ind = mail.rfind('@')
        full_name = mail[0:ind].split('.')
        self.first_name = full_name[0].title()
        self.last_name = full_name[1].capitalize()

    @email.deleter
    def email(self):
        """Deleter"""
        print('Employee details will be deleted!')
        self.first_name = None
        self.last_name = None

    def full_name(self):
        """Return employee full name"""
        return f'{self.first_name} {self.last_name}'

    def display_details(self):
        """Return details about employee"""
        return f'First Name: {self.first_name}\nLast Name: {self.last_name}\n' \
               f'E-mail: {self.email}\nIncome: {self.income}'

    @classmethod
    def set_holidays(cls, nb):
        cls.holidays = nb

    @classmethod
    def from_string(cls, employees_string: str):
        """Objects can inherit from Employee using the alternative constructor
        """
        employees = employees_string.split(';')
        employees_objects = []
        for emp in employees:
            emp_data = emp.split(' ')
            first_name = emp_data[0]
            last_name = emp_data[1]
            income = emp_data[2]
            employees_objects.append(cls(first_name, last_name, income))

        return employees_objects

    @staticmethod
    def weekday(day: date) -> str:
        """Return day of the week
        """
        days = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Saturday',
            7: 'Sunday'
        }
        return days[date.isoweekday(day)]


class Manager(Employee):
    """Manager class"""

    def __new__(cls, first, last, salary=1000, employees=None):
        obj = super().__new__(cls, first, last, salary=1000)
        return obj

    def __init__(self, first, last, salary=1000, employees=None):
        super().__init__(first, last, salary)
        # Employee.__init__(first, last, salary)
        if employees:
            self.employees = employees
        else:
            self.employees = []

    def add_employee(self, emp_obj):
        """Add employees"""
        if emp_obj not in self.employees:
            self.employees.append(emp_obj)

    # def __repr__(self):
    #     return f"Manager('{self.first_name}', '{self.last_name}', '{self.income}')"

    def __str__(self):
        return f"Manager('income={self.yearly_amount}', number of employees='{Manager.number_of_employees}', holidays='{self.holidays}')"

    def __add__(self, other):
        return self.income + other.income

    def __len__(self):
        return len(self.first_name + self.last_name)


if __name__ == '__main__':
    emp1 = Employee('Dan', 'Chivu', 2000)
    emp2 = Employee('Cristi', 'Dragan', 1800)
    emp3 = Employee('Bianca', 'Neacsu', 1000000)
    emp4 = Employee('Cristina', 'Bocai', 10000)

    print(emp3.last_name)
    print(emp3.email)

    emp3.last_name = "Voinea"
    print(emp3.last_name)
    print(emp3.email)
    today = datetime.today()
    print(today.hour)

    emp2.email = 'cristi.voicu@company.com'
    print(emp2.first_name)
    print(emp2.last_name)
    # del emp2.email
    print(emp2.first_name)
    print(emp2.last_name)
    print(emp2.email)


    l = [1, 2, 3]
    print(emp2.__dir__())
    # print(help(object))

    print(dir(emp1))
    # print(emp3.holidays)
    # Employee.set_holidays(23)
    # print(emp1.holidays)
    # print(emp2.holidays)
    #
    # employees = 'Cristi Bogdan 1000;Flori Cozma 2000;Marius Alexandrescu 1300;Mihai Oancea 3000'
    # obj = Employee.from_string(employees)
    # print(obj)
    # print(date.today())
    # print(emp1.weekday(date(2024, 3, 10)))


    # Manager objects

    m1 = Manager('Adi', 'Cristache', 10000, [emp2, emp3, emp1])
    m2 = Manager('Adrian', 'Voiculescu', 40000, [emp2, emp3, emp1])
    print(m1.email)
    print(m1.employees)
    print(m1.display_details())
    print(m1.full_name())
    print(m1.weekday(date(2024, 2, 10)))
    m1.add_employee(emp4)
    print(m1.employees)
    print(m1.__dir__())
    print(m1)
    print(m2)
    print(m1.__repr__())
    print(m1.__str__())

    print(len(m1))

