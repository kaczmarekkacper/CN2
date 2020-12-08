class G2:
    value = 0

    @staticmethod
    def read_g2(g2):
        int_value = int(g2)
        if 0 <= int_value <= 20:
            return int_value
        else:
            raise Exception("Wrong g2")
