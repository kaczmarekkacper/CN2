import enum


class Goout(enum.Enum):
    VeryLow = 1
    Low = 2
    Medium = 3
    High = 4
    VeryHigh = 5

    @staticmethod
    def read_goout(goout):
        if goout == '1':
            return Goout.VeryLow
        elif goout == '2':
            return Goout.Low
        elif goout == '3':
            return Goout.Medium
        elif goout == '4':
            return Goout.High
        elif goout == '5':
            return Goout.VeryHigh
        else:
            raise Exception("Wrong goout")
