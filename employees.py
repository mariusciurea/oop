"""OOP Tutorial"""


class Employee:
    """Employee class"""
    yearly_amount = 1.2
    number_of_employees = 0

    def __init__(self, first, last, salary=1000):
        """Employee constructor"""

        self.first_name = first
        self.last_name = last
        self.income = salary
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@company.com'
        Employee.number_of_employees += 1

    def full_name(self):
        """Return employee full name"""
        return f'{self.first_name} {self.last_name}'

    def display_details(self):
        """Return details about employee"""
        return f'First Name: {self.first_name}\nLast Name: {self.last_name}\n' \
               f'E-mail: {self.email}\nIncome: {self.income}'


if __name__ == '__main__':
    emp1 = Employee('Dan', 'Chivu', 2000)
    emp2 = Employee('Cristi', 'Dragan', 1800)
    emp3 = Employee('Bianca', 'Neacsu')
    emp4 = Employee('Cristina', 'Bocai', 10000)

    print(emp3.email)
    print(emp3.full_name())
    print(emp3.income)

    print(Employee.yearly_amount)
    print(emp1.yearly_amount)
    print(emp2.yearly_amount)
    emp1.yearly_amount = 1.4
    print(emp1.yearly_amount)
    print(Employee.number_of_employees)

    print(emp1.display_details())

