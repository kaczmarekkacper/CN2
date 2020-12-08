class Absences:
    value = 0

    @staticmethod
    def read_absences(absences):
        int_value = int(absences)
        if 0 <= int_value <= 93:
            return int_value
        else:
            raise Exception("Wrong absences")
