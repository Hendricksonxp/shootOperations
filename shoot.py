


class Shoot:
    def __init__(self):
        self.start_date = ''
        self.end_date = ''
        self.club = ''
        self.events = []

    def add_event(self, anEvent):
        self.events.append(anEvent)

    def add_club(self, name):
        self.club = name

    def add_start_date(self, date):
        self.start_date = date

    def add_end_date(self, date):
        self.end_date = date

    def score_for(self, anEvent, anId):
        event = next(filter(lambda each: each.event_number == anEvent, self.events))
        return event.score_for(anId)