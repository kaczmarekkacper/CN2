import enum


class Freetime(enum.Enum):
    VeryLow = 1
    Low = 2
    Medium = 3
    High = 4
    VeryHigh = 5

    @staticmethod
    def read_freetime(freetime):
        if freetime == '1':
            return Freetime.VeryLow
        elif freetime == '2':
            return Freetime.Low
        elif freetime == '3':
            return Freetime.Medium
        elif freetime == '4':
            return Freetime.High
        elif freetime == '5':
            return Freetime.VeryHigh
        else:
            raise Exception("Wrong freetime")
