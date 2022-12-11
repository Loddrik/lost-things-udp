from Database.models import Base
from sqlalchemy import create_engine
from Database.config import Config
from Database.models import Base
from Database.session import session
import csv


def init_db():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)

    return True


init_db()
