import enum


class Mjob(enum.Enum):
    Teacher = 1
    Health = 2
    Services = 3
    AtHome = 4
    Other = 5

    @staticmethod
    def read_mjob(mjob):
        if mjob == 'teacher':
            return Mjob.Teacher
        elif mjob == 'health':
            return Mjob.Health
        elif mjob == 'services':
            return Mjob.Services
        elif mjob == 'at_home':
            return Mjob.AtHome
        elif mjob == 'other':
            return Mjob.Other
        else:
            raise Exception("Wrong mjob")
