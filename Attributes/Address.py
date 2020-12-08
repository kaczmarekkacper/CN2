import enum


class Address(enum.Enum):
    U = 1
    R = 2

    @staticmethod
    def read_address(address):
        if address == 'U':
            return Address.U
        elif address == 'R':
            return Address.R
        else:
            raise Exception("Wrong address")