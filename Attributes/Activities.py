import enum


class Activities(enum.Enum):
    Yes = 1
    No = 2

    @staticmethod
    def read_activities(activities):
        if activities == 'yes':
            return Activities.Yes
        elif activities == 'no':
            return Activities.No
        else:
            raise Exception("Wrong activities")
