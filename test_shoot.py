import unittest
from datetime import date
from shoot import Shoot
from event import Event
from shooter import Shooter
from entry import Entry



class MyTestCase(unittest.TestCase):
    def test_hookup(self):
        self.assertEqual(True, True)

    def test_lambda(self):
        aLambda = lambda each: each == 2
        self.assertTrue(aLambda(2))

    def test_filter(self):
        aList = [1,2,3]
        aLambda = lambda each: each == 2
        result = next(filter(aLambda, aList))
        self.assertEqual(2, result)

    def test_shooter_score(self):
        shoot = self.create_test_shoot()
        event = self.create_test_event(shoot)
        shoot.add_event(event)
        shooter1 = self.create_test_shooter1()
        shooter2 = self.create_test_shooter2()
        event.add_entry(shooter1, 1, 3)

        self.assertEqual('2104285', Entry(shooter1, 1, 3).id())

        event.add_entry(shooter2, 1, 1)

        self.assertEqual(2, len(event.entries))
        self.assertEqual('2104285', event.get_entry(1,3).id())
        event.add_score(1, 1, 25, 24, 23, 25)
        event.add_score(1, 3, 24, 23, 23, 25)

        score = shoot.score_for(1, 2104285)
        self.assertEqual(97, score)

    def create_test_shoot(self):
        shoot = Shoot()
        shoot.add_club("Birmingham Gun Club")
        shoot.add_start_date(date.fromisoformat('2019-12-04'))
        shoot.add_end_date(date.fromisoformat('2019-12-04'))
        return shoot

    def create_test_event(self, aShoot):
        event = Event(1, "SINGLES", 100)
        return event

    def create_test_shooter1(self):
        return Shooter('2104285', 'Chet Hendrickson')

    def create_test_shooter2(self):
        return Shooter('9203001', 'Sue Hendrickson')

if __name__ == '__main__':
    unittest.main()
