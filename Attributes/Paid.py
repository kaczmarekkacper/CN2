import enum


class Paid(enum.Enum):
    Yes = 1
    No = 2

    @staticmethod
    def read_paid(paid):
        if paid == 'yes':
            return Paid.Yes
        elif paid == 'no':
            return Paid.No
        else:
            raise Exception("Wrong paid")
