import unittest
from model.Employee import Employee
from model.Company import Company
from model.Country import Country
from model.Person import Person


class EmployeeTest(unittest.TestCase):
    def test(self):
        c1 = Company('BGP')
        co1 = Country('UAE', 'UE')
        e = Employee('B1001', c1, 'LI', 'YU', 19960101, co1)
        self.assertIsInstance(e, Employee)
        self.assertEqual(co1, e.get_country())
        e1 = Employee('B101', c1, 'AA', 'BB', 19970101, co1)
        e2 = Employee('B102', c1, 'CC', 'DD', 19830202, co1)
