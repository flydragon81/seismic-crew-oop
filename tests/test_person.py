import unittest
from var_dump import var_dump
from model.Person import Person
from model.Country import Country


class PersonTest(unittest.TestCase):
    def test(self):
        co1 = Country('China', 'CN')
        p = Person('long', 'yong', 19810101, co1, 'M')
        self.assertIsInstance(p, Person)

        self.assertEqual('long', p.get_fname())
        self.assertEqual('yong', p.get_lname())
        self.assertEqual(19810101, p.get_dob())
        self.assertEqual(co1,  p.get_country())
        self.assertEqual('M', p.get_sex())
