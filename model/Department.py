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
        self.__instancecheck(person, Person)
        if person not in self.__personnel:
            self.__personnel.append(person)
            return True
        else:
            return False

    def remove_person(self, person):
        self.__instancecheck(person, Person)
        if person in self.__personnel:
            self.__personnel.remove(person)
            return True
        else:
            return False

    def add_vehicle(self, vehicle):
        self.__instancecheck(vehicle, Vehicle)
        if vehicle not in self.__vehicles:
            self.__vehicles.append(vehicle)
            return True
        else:
            return False

    def remove_vehicle(self, vehicle):
        self.__instancecheck(vehicle, Vehicle)
        if vehicle in self.__vehicles:
            self.__vehicles.remove(vehicle)
            return True
        else:
            return False

    def get_personnel(self):
        return self.__personnel

    def get_vehicle(self):
        return self.__vehicles

    def __instancecheck(self, object, name_class):
        if not isinstance(object, name_class):
            raise Exception('value is not a' + object + ' object')
