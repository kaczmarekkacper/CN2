import enum


class Reason(enum.Enum):
    Home = 1
    Reputation = 2
    Course = 3
    Other = 4

    @staticmethod
    def read_reason(reason):
        if reason == 'home':
            return Reason.Home
        elif reason == 'reputation':
            return Reason.Reputation
        elif reason == 'course':
            return Reason.Course
        elif reason == 'other':
            return Reason.Other
        else:
            raise Exception("Wrong reason")
