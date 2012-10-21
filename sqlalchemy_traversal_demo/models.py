from sqlalchemy                 import Column
from sqlalchemy                 import Integer
from sqlalchemy.types           import Unicode

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm             import scoped_session
from sqlalchemy.orm             import sessionmaker
from zope.sqlalchemy            import ZopeTransactionExtension
from sqlalchemy_traversal       import TraversalMixin


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Country(TraversalMixin, Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    official_name = Column(Unicode(128), nullable=True)
    alpha2 = Column(Unicode(128), nullable=True)
    alpha3 = Column(Unicode(128), nullable=True)
    numeric = Column(Integer, nullable=True)
