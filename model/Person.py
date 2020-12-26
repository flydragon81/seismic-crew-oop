from model.Country import Country


class Person:
    def __init__(self, fname, lname, dob, Country, sex='M'):
        self.__fname = fname
        self.__lname = lname
        self.__dob = dob
        self.__country = Country
        self.__sex = sex

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_dob(self):
        return self.__dob

    def get_country(self):
        return self.__country

    def get_sex(self):
        return self.__sex
