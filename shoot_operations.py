from shoots import Shoots
from shoot import Shoot

class Shoot_Operations:
    def __init__(self, shoots):
        self.shoots = shoots

    @classmethod
    def memory(cls):
        return cls(Shoots.memory())

    def create_shoot(self, club, start_date, end_date):
        shoot = Shoot(club, start_date, end_date)
        self.shoots.addShoot(shoot)
        return shoot
