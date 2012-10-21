from sqlalchemy                 import Column
from sqlalchemy                 import Integer
from sqlalchemy                 import ForeignKey
from sqlalchemy.types           import Unicode

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm             import scoped_session
from sqlalchemy.orm             import sessionmaker
from sqlalchemy.orm             import relation
from zope.sqlalchemy            import ZopeTransactionExtension
from sqlalchemy_traversal       import TraversalMixin


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Country(TraversalMixin, Base):
    _json_eager_load = ['subdivisions']
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    official_name = Column(Unicode(128), nullable=True)
    alpha2 = Column(Unicode(128), nullable=True)
    alpha3 = Column(Unicode(128), nullable=True)
    numeric = Column(Integer, nullable=True)

class Subdivision(TraversalMixin, Base):
#    _json_eager_load = ['country']
    __tablename__ = 'subdivision'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    code = Column(Unicode(128), nullable=False)
    country_id  = Column(Integer, ForeignKey(Country.id), nullable=False)
    country = relation(Country, backref='subdivisions')
