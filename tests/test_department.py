import unittest
from var_dump import var_dump
from model.Department import Department
from model.Person import Person
from model.Vehicle import Vehicle


class DepartmentTest(unittest.TestCase):
    def test(self):
        d = Department('QC', )
        self.assertIsInstance(d, Department)

        self.assertEqual('QC', d.get_name())
        p1 = Person('long', 'yong', 19810101, 'Chinese', 'M')
        p2 = Person('li', 'hu', 19810201, 'Chinese', 'M')
        self.assertTrue(d.add_person(p1))
        self.assertTrue(d.add_person(p2))
        self.assertFalse(d.add_person(p1))
        self.assertRaises(Exception, d.add_person, 'It is not object of Person class')
        self.assertEqual(2, len(d.get_personnel()))
        self.assertEqual(p1, d.get_personnel()[0])

        self.assertTrue(d.remove_person(p1))
        self.assertFalse(d.remove_person(p1))
        self.assertEqual(1, len(d.get_personnel()))
        self.assertRaises(Exception, d.remove_person, 'It is not object of Person class')

        v1 = Vehicle('100007', Vehicle.TYPE_HEAVY)
        v2 = Vehicle('10008', Vehicle.TYPE_LIGHT)
        self.assertTrue(d.add_vehicle(v1))
        self.assertFalse(d.add_vehicle(v1))
        self.assertTrue(d.add_vehicle(v2))
        self.assertEqual(2, len(d.get_vehicle()))

        self.assertTrue(d.remove_vehicle(v1))
        self.assertFalse(d.remove_vehicle(v1))
        self.assertEqual(1, len(d.get_vehicle()))
        self.assertTrue(d.remove_vehicle(v2))
        self.assertEqual(0, len(d.get_vehicle()))
        # var_dump(p1)
        # var_dump(['long', 'yong', 19810101, 'Chinese', 'M'])
