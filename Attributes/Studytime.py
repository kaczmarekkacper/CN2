class Studytime:
    value = 0

    @staticmethod
    def read_studytime(studytime):
        float_value = float(studytime)
        if 1 <= float_value <= 10:
            return float_value
        else:
            raise Exception("Wrong studytime")
