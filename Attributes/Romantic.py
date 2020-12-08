import enum


class Romantic(enum.Enum):
    Yes = 1
    No = 2

    @staticmethod
    def read_romantic(romantic):
        if romantic == 'yes':
            return Romantic.Yes
        elif romantic == 'no':
            return Romantic.No
        else:
            raise Exception("Wrong romantic")
