from pyramid.config         import Configurator
from sqlalchemy             import engine_from_config

from .models                import DBSession
from .models                import Base

from sqlalchemy_traversal   import ISABase
from sqlalchemy_traversal   import ISASession

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    config.registry.registerUtility(DBSession, ISASession)
    config.registry.registerUtility(Base, ISABase)

    config.scan()
    return config.make_wsgi_app()

