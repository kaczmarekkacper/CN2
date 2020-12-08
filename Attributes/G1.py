class G1:
    value = 0

    @staticmethod
    def read_g1(g1):
        int_value = int(g1)
        if 0 <= int_value <= 20:
            return int_value
        else:
            raise Exception("Wrong g1")
