import os
import sys
import transaction

import pycountry

from sqlalchemy     import engine_from_config

from pyramid.paster import get_appsettings
from pyramid.paster import setup_logging

from ..models       import DBSession
from ..models       import Base
from ..models       import Country
from ..models       import Subdivision

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        for country in pycountry.countries:
            new_country = Country(
                    name=country.name,
                    alpha2=country.alpha2,
                    alpha3=country.alpha3,
                    numeric=country.numeric
            )

            if hasattr(country, 'official_name'):
                new_country.official_name = country.official_name

            DBSession.add(new_country)

            subdivisions = None
            try:
                subdivisions = pycountry.subdivisions.get(
                    country_code = country.alpha2
                )
            except KeyError:
                pass

            if country.alpha2 == 'US':
                import pdb; pdb.set_trace()

            if subdivisions:
                for subdivision in subdivisions:
                    new_sub = Subdivision(
                            name=subdivision.name
                            , code=subdivision.code
                            , country=new_country
                    )
                    DBSession.add(new_sub)
