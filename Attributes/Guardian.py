import enum


class Guardian(enum.Enum):
    Father = 1
    Mother = 2
    Other = 3

    @staticmethod
    def read_guardian(guardian):
        if guardian == 'father':
            return Guardian.Father
        elif guardian == 'mother':
            return Guardian.Mother
        elif guardian == 'other':
            return Guardian.Other
        else:
            raise Exception("Wrong guardian")
