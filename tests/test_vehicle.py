import unittest
from model.Vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def test(self):
        v = Vehicle('10001', Vehicle.TYPE_HEAVY)
        self.assertIsInstance(v, Vehicle)

        self.assertEqual('10001', v.get_plate())
        self.assertEqual(Vehicle.TYPE_HEAVY, v.get_vtype())

