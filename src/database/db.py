# core interface to the database
import os
import logging

import sqlalchemy.orm
from sqlalchemy import create_engine
# base contains a metaclass that produces the right table
from sqlalchemy.ext.declarative import declarative_base
# setting up a class that represents our SQL Database
from sqlalchemy import Column, Integer, String
# prints if a table was created - neat check for making sure nothing is overwritten
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker

if not os.path.exists('data/'):
    os.mkdir('data/')

engine = create_engine('sqlite:///data/main.db', echo=True)
Base: declarative_base = declarative_base()

logger = logging.getLogger('my-bot')


# represents a user of the bot
# keeps all relevant data plus some optional information about users 'state' in this entry
# each user should only be entered once
# The addition currently happens in commands.commands.start()
class Users(Base):
    __tablename__ = 'USERS'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    username = Column(String)
    menu = Column(String)         # saves state of the menu the user is in
    listen_mode = Column(String)  # useful if bot shall interpret the next message in a certain way

    def __repr__(self):
        return f"<UsersEntry: username='{self.username}', chat_id='{self.chat_id}', " \
               f"menu='{self.menu}', add_mode='{self.listen_mode}', primary_key='{self.id}'"

# TODO: PUT YOUR ADDITIONAL TABLES HERE


@event.listens_for(Base.metadata, 'after_create')
def receive_after_create(target, connection, tables, **kw):
    """listen for the 'after_create' event"""
    logger.info('A table was created' if tables else 'No table was created')
    print('A table was created' if tables else 'No table was created')


def open_session() -> sqlalchemy.orm.Session:
    """
    :return: new active session
    """
    return sessionmaker(bind=engine)()


# creating db which doesn't happen when it should?
database = Base.metadata.create_all(bind=engine)
