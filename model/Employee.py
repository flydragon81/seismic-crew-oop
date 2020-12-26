from model.Person import Person
from model.Company import Company


class Employee(Person):
    def __init__(self, id_number, company, fname, lname, dob, country):
        super().__init__(fname, lname, dob, country)
        if not isinstance(company, Company):
            raise Exception('value is not a' + object + ' object')
        self.id_number = id_number
        self.company = company

    def get_id_number(self):
        return self.id_number

    def get_company(self):
        return self.company
