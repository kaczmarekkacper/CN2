import enum


class Fjob(enum.Enum):
    Teacher = 1
    Health = 2
    Services = 3
    AtHome = 4
    Other = 5

    @staticmethod
    def read_fjob(fjob):
        if fjob == 'teacher':
            return Fjob.Teacher
        elif fjob == 'health':
            return Fjob.Health
        elif fjob == 'services':
            return Fjob.Services
        elif fjob == 'at_home':
            return Fjob.AtHome
        elif fjob == 'other':
            return Fjob.Other
        else:
            raise Exception("Wrong fjob")
