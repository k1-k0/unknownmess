import config

from peewee import (
    Model, CharField, DateTimeField,
    ForeignKeyField, AutoField, IntegerField
)
from peewee_async import (
    Manager, PostgresqlDatabase
)


database = PostgresqlDatabase(
    database=config.database_name,
    user=config.database_user,
    password=config.database_pass,
    host=config.database_host,
)


class BaseModel(Model):
    class Meta:
        database = database


class Message(BaseModel):
    id = AutoField(unique=True)
    title = CharField(max_length=70)
    text = CharField(max_length=200)
    created = DateTimeField()


class Emotion(BaseModel):
    message = ForeignKeyField(Message, backref="emotions")
    symbol = CharField(max_length=1)
    count = IntegerField(default=0)


def create_tables():
    with database:
        database.create_tables([Message, Emotion])


objects = Manager(database)
