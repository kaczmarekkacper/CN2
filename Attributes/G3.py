class G3:
    value = 0

    @staticmethod
    def read_g3(g3):
        int_value = int(g3)
        if 0 <= int_value <= 20:
            return int_value
        else:
            raise Exception("Wrong g3")
