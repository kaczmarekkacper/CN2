class Failures():
    value = 0
    
    @staticmethod
    def read_failures(failures):
        int_value = int(failures)
        if 0 <= int_value <= 4:
            return int_value
        else:
            raise Exception("Wrong failures")
