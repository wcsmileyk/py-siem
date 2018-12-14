import datetime

from models import db, Event


def write_event(msg):
    db.connect()
    event = Event(message=msg)
    event.save()
    db.close()


def parse_pix(msg):
    pass
