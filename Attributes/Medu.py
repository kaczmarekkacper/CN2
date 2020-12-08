import enum


class Medu(enum.Enum):
    NoSchool = 1
    PrimaryEdu = 2
    FifthToNinth = 3
    SecondaryEdu = 4
    Higher = 5

    @staticmethod
    def read_medu(medu):
        if medu == '0':
            return Medu.NoSchool
        elif medu == '1':
            return Medu.PrimaryEdu
        elif medu == '2':
            return Medu.FifthToNinth
        elif medu == '3':
            return Medu.SecondaryEdu
        elif medu == '4':
            return Medu.Higher
        else:
            raise Exception("Wrong Medu")
