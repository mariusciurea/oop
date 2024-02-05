"""OOP Tutorial"""
from datetime import date, datetime


class Employee:
    """Employee class"""
    yearly_amount = 1.2
    number_of_employees = 0
    holidays = 21

    def __init__(self, first, last, salary=1000):
        """Employee constructor"""

        self.first_name = first
        self.last_name = last
        self.income = salary

        Employee.number_of_employees += 1

    @property
    def email(self):
        """Return employee email"""
        return f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'

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


if __name__ == '__main__':
    emp1 = Employee('Dan', 'Chivu', 2000)
    emp2 = Employee('Cristi', 'Dragan', 1800)
    emp3 = Employee('Bianca', 'Neacsu')
    emp4 = Employee('Cristina', 'Bocai', 10000)

    print(emp3.last_name)
    print(emp3.email)

    emp3.last_name = "Voinea"
    print(emp3.last_name)
    print(emp3.email)
    today = datetime.today()
    print(today.hour)


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
