from sqlalchemy import Column, DateTime, Integer, Text, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

"""SQLAlchemy Mixins"""


class IDMixin:
    id = Column(Integer, primary_key=True, nullable=False)


class CreatedTimestampMixin:
    created_datetime_utc = Column(
        DateTime, nullable=False, server_default=text("(now() at time zone 'utc')")
    )


"""SQLAlchemy Models"""


class ApiRequest(IDMixin, CreatedTimestampMixin, Base):

    __tablename__ = "api_requests"

    url = Column(Text, nullable=False)
    method = Column(Text, nullable=False)
    status = Column(Text, nullable=False)
    status_code = Column(Integer, nullable=False)
    remote_addr = Column(Text, nullable=False)
