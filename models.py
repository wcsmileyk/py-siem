import datetime

from peewee import *

db = SqliteDatabase('events.sqlite')


class Event(Model):
    device_id = ForeignKeyField(Device, backref='events')
    occured_timestamp = DateTimeField(default=datetime.datetime.now())
    received_timestamp = DateTimeField(default=datetime.datetime.now())
    message = TextField()

    class Meta:
        database = db


class Device(Model):
    name = TextField()

# class SourceIp(Model):
#     ip = CharField()
#     event_id = ForeignKeyField(Event, backref='source_ips')
#
#     class Meta:
#         database = db
#
#
# class DestIp(Model):
#     ip = CharField()
#     event_id = ForeignKeyField(Event, backref='dest_ips')
#
#     class Meta:
#         database = db
#
#
# class URL(Model):
#     url = CharField()
#     event_id = ForeignKeyField(Event, backref='urls')
#
#     class Meta:
#         database = db


def initialize():
    db.connect()
    db.create_tables([Event, Device])
