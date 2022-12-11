import json
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float,  Boolean, Date
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(String(50), primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String(90), nullable=False)
    faculty = Column(String(100), nullable=False)
    addres = Column(String(90), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


class Thing(Base):
    __tablename__ = 'Thing'
    id = Column(String(50), primary_key=True)
    userId = Column(String(50), ForeignKey('User.id'), nullable=False)
    name = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    meetingDate = Column(DateTime, nullable=True)
    publishedDate = Column(DateTime, nullable=False)
    recoveredDate = Column(DateTime, nullable=True)

    def __repr__(self):
        return '< %r>' % self.id


def to_dict(obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                # this will fail on non-encodable values, like other classes
                json.dumps(data)
                if data is not None:
                    fields[field] = data
            except TypeError:
                pass
        # a json-encodable dict
        return fields
