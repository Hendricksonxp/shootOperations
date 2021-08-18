import unittest
from datetime import date
from shoot_operations import Shoot_Operations
from shoot import Shoot
from event import Event
from shooter import Shooter
from entry import Entry
from csv import reader




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
        system = Shoot_Operations.memory()
        shoot = self.create_test_shoot(system)
        event = self.create_test_event(shoot)
        shoot.add_event(event)
        shooter1 = self.create_test_shooter1()
        shooter2 = self.create_test_shooter2()
        event.add_entry(shooter1, 1, 3)

        self.assertEqual('2104285', Entry(shooter1, 4, 1, 3).id())

        event.add_entry(shooter2, 1, 1)

        self.assertEqual(2, len(event.entries))
        self.assertEqual('2104285', event.get_entry(1,3).id())
        event.add_score(1, 1, 25, 24, 23, 25)
        event.add_score(1, 3, 24, 23, 23, 25)

        event = next(filter(lambda each: each.event_number == 1, shoot.events))
        self.assertEqual(1, event.event_number)

        score = event.score_for('2104285')
        self.assertEqual(95, score)

    def test_southern_zone_berea_preliminary_singles(self):
        system = Shoot_Operations.memory()
        shoot = Shoot(system)
        shoot.add_club("Central Kentucky Gun Club")
        shoot.add_start_date(date.fromisoformat('2021-07-15'))
        shoot.add_end_date(date.fromisoformat('2021-07-18'))

        event = Event(1, "SINGLES", 100, 4)
        shoot.add_event(event)
        counter = 1
        with open('c:/Users/suechet/Dropbox/southernzonebereaprelimsingles.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                counter = counter + 1
                event.add_entry(Shooter(str(counter), row[0]), row[2], row[3])
                event.add_score(row[2], row[3], row[6], row[7], row[8],row[9])

        score = event.score_for('5')
        self.assertEqual(100, score)

    def create_test_shoot(self, shoot_operations):
        shoot = shoot_operations.create_shoot("Birmingham Gun Club",'2019-12-04','2019-12-04')
        return shoot

    def create_test_event(self, shoot):
        event = Event(shoot, 1, "SINGLES", 100, 4)
        return event

    def create_test_shooter1(self):
        return Shooter('2104285', 'Chet Hendrickson')

    def create_test_shooter2(self):
        return Shooter('9203001', 'Sue Hendrickson')

if __name__ == '__main__':
    unittest.main()
