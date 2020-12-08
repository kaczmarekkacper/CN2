import enum


class Schoolsup(enum.Enum):
    Yes = 1
    No = 2

    @staticmethod
    def read_schoolsup(schoolsup):
        if schoolsup == 'yes':
            return Schoolsup.Yes
        elif schoolsup == 'no':
            return Schoolsup.No
        else:
            raise Exception("Wrong schoolsup")
