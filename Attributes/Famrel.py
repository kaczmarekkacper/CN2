import enum


class Famrel(enum.Enum):
    VeryBad = 1
    Bad = 2
    Medium = 3
    Good = 4
    Excellent = 5

    @staticmethod
    def read_famrel(famrel):
        if famrel == '1':
            return Famrel.VeryBad
        elif famrel == '2':
            return Famrel.Bad
        elif famrel == '3':
            return Famrel.Medium
        elif famrel == '4':
            return Famrel.Good
        elif famrel == '5':
            return Famrel.Excellent
        else:
            raise Exception("Wrong famrel")
