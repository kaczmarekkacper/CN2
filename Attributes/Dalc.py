import enum


class Dalc(enum.Enum):
    VeryLow = 1
    Low = 2
    Medium = 3
    High = 4
    VeryHigh = 5

    @staticmethod
    def read_dalc(dalc):
        if dalc == '1':
            return Dalc.VeryLow
        elif dalc == '2':
            return Dalc.Low
        elif dalc == '3':
            return Dalc.Medium
        elif dalc == '4':
            return Dalc.High
        elif dalc == '5':
            return Dalc.VeryHigh
        else:
            raise Exception("Wrong dalc")
