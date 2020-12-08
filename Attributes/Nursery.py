import enum


class Nursery(enum.Enum):
    Yes = 1
    No = 2

    @staticmethod
    def read_nursery(nursery):
        if nursery == 'yes':
            return Nursery.Yes
        elif nursery == 'no':
            return Nursery.No
        else:
            raise Exception("Wrong nursery")
