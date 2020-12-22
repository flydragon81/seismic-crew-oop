from model.Person import Person
from model.Vehicle import Vehicle


class Department:
    def __init__(self, name):
        self.__name = name
        self.__personnel = []
        self.__vehicles = []

    def get_name(self):
        return self.__name

    def add_person(self, person):
        if not isinstance(person, Person):
            raise Exception('value is not a person object')
        if person not in self.__personnel:
            self.__personnel.append(person)
            return True
        else:
            return False

    def remove_person(self, person):
        if not isinstance(person, Person):
            raise Exception('value is not a person object')
        if person in self.__personnel:
            self.__personnel.remove(person)
            return True
        else:
            return False

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise Exception('value is not a vehicle object')
        if vehicle not in self.__vehicles:
            self.__vehicles.append(vehicle)
            return True
        else:
            return False

    def remove_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise Exception('value is not a vehicle object')
        if vehicle in self.__vehicles:
            self.__vehicles.remove(vehicle)
            return True
        else:
            return False

    def get_personnel(self):
        return self.__personnel

    def get_vehicle(self):
        return self.__vehicles
