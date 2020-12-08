import enum


class Walc(enum.Enum):
    VeryLow = 1
    Low = 2
    Medium = 3
    High = 4
    VeryHigh = 5

    @staticmethod
    def read_walc(walc):
        if walc == '1':
            return Walc.VeryLow
        elif walc == '2':
            return Walc.Low
        elif walc == '3':
            return Walc.Medium
        elif walc == '4':
            return Walc.High
        elif walc == '5':
            return Walc.VeryHigh
        else:
            raise Exception("Wrong walc")
