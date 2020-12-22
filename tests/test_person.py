import unittest
from var_dump import var_dump
from model.Person import Person


class PersonTest(unittest.TestCase):
    def test(self):
        p = Person('long', 'yong', 19810101, 'Chinese', 'M')
        self.assertIsInstance(p, Person)

        self.assertEqual('long', p.get_fname())
        self.assertEqual('yong', p.get_lname())
        self.assertEqual(19810101, p.get_dob())
        self.assertEqual('Chinese', p.get_nationality())
        self.assertEqual('M', p.get_sex())
