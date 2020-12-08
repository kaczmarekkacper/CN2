import enum


class Fedu(enum.Enum):
    NoSchool = 1
    PrimaryEdu = 2
    FifthToNinth = 3
    SecondaryEdu = 4
    Higher = 5

    @staticmethod
    def read_fedu(fedu):
        if fedu == '0':
            return Fedu.NoSchool
        elif fedu == '1':
            return Fedu.PrimaryEdu
        elif fedu == '2':
            return Fedu.FifthToNinth
        elif fedu == '3':
            return Fedu.SecondaryEdu
        elif fedu == '4':
            return Fedu.Higher
        else:
            raise Exception("Wrong fedu")
