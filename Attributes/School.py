import enum


class School(enum.Enum):
    GP = 1
    MS = 2

    @staticmethod
    def read_school(school):
        if school == 'MS':
            return School.MS
        elif school == 'GP':
            return School.GP
        else:
            raise Exception("Wrong school")
