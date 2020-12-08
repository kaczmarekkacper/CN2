import enum


class Pstatus(enum.Enum):
    T = 1
    A = 2

    @staticmethod
    def read_pstatus(pstatus):
        if pstatus == 'T':
            return Pstatus.T
        elif pstatus == 'A':
            return Pstatus.A
        else:
            raise Exception("Wrong pstatus")