class Vehicle:
    TYPE_HEAVY = 'HEAVY'
    TYPE_LIGHT = 'LIGHT'

    def __init__(self, plate, vtype):
        self.__plate = plate
        self.__vtype = vtype

    def get_plate(self):
        return self.__plate

    def get_vtype(self):
        return self.__vtype
