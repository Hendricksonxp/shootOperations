

class Shoots:
    def __init__(self, array):
        self.shoots_array = []

    @classmethod
    def memory(cls):
        return cls([])

    def addShoot(self, shoot):
        self.shoots_array.append(shoot)