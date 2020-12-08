import enum


class Famsize(enum.Enum):
    LE3 = 1
    GT3 = 2

    @staticmethod
    def read_famsize(famsize):
        if famsize == 'LE3':
            return Famsize.LE3
        elif famsize == 'GT3':
            return Famsize.GT3
        else:
            raise Exception("Wrong famsize")