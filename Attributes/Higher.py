import enum


class Higher(enum.Enum):
    Yes = 1
    No = 2

    @staticmethod
    def read_higher(higher):
        if higher == 'yes':
            return Higher.Yes
        elif higher == 'no':
            return Higher.No
        else:
            raise Exception("Wrong higher")
