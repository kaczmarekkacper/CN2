import enum


class Sex(enum.Enum):
    F = 1
    M = 2

    @staticmethod
    def read_sex(sex):
        if sex == 'F':
            return Sex.F
        elif sex == 'M':
            return Sex.M
        else:
            raise Exception("Wrong sex")
