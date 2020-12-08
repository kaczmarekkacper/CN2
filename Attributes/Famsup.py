import enum


class Famsup(enum.Enum):
    Yes = 1
    No = 2

    @staticmethod
    def read_famsup(famsup):
        if famsup == 'yes':
            return Famsup.Yes
        elif famsup == 'no':
            return Famsup.No
        else:
            raise Exception("Wrong famsup")
