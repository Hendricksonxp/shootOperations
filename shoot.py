from event import Event


class Shoot:
    def __init__(self, club, start, end):
        self.start_date = start
        self.end_date = end
        self.club = club
        self.events = []

    def add_event(self, anEvent):
        self.events.append(anEvent)

    def add_club(self, name):
        self.club = name

    def add_start_date(self, date):
        self.start_date = date

    def add_end_date(self, date):
        self.end_date = date

    def score_for(self, anEvent_number, anId):
        event = next(filter(lambda each: each.is_event_number(anEvent_number)  , self.events))
        return event.score_for(anId)