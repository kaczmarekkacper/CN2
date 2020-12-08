class Age:
    value = 0

    @staticmethod
    def read_age(age):
        int_value = int(age)
        if 15 <= int_value <= 22:
            return int_value
        else:
            raise Exception("Wrong age")
