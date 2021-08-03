


class Shoot:
    def __init__(self):
    start_date = ''
    end_date = ''
    club = ''
    events = []

    def add_club(self, name):
        club = name

    def add_start_date(self, date):
        start_date = date

    def add_end_date(self, date):
        end_date = date

    def score_for(anEvent, anId):
        event = filter(lambda each: each.event_number() == anEvent, events)
        return event(score_for(id))