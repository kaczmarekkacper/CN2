import enum


class Health(enum.Enum):
    VeryBad = 1
    Bad = 2
    Medium = 3
    Good = 4
    VeryGood = 5

    @staticmethod
    def read_health(health):
        if health == '1':
            return Health.VeryBad
        elif health == '2':
            return Health.Bad
        elif health == '3':
            return Health.Medium
        elif health == '4':
            return Health.Good
        elif health == '5':
            return Health.VeryGood
        else:
            raise Exception("Wrong health")
