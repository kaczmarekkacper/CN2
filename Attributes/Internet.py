import enum


class Internet(enum.Enum):
    Yes = 1
    No = 2

    @staticmethod
    def read_internet(internet):
        if internet == 'yes':
            return Internet.Yes
        elif internet == 'no':
            return Internet.No
        else:
            raise Exception("Wrong internet")
