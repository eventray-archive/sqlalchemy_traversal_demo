sqlalchemy_traversal_demo
=========================

This is a demo pyramid application that shows how to use sqlalchemy_traversal


    $ python setup.py develop
    $ initialize_sqlalchemy_traversal_demo_db ./development.ini
    $ pserve ./development.ini


* Open your browser to http://0.0.0.0:6543/traverse/country
* Open your browser to http://0.0.0.0:6543/traverse/country/236
* Open your browser to http://0.0.0.0:6543/traverse/country/236/subdivisions
* Open your browser to http://0.0.0.0:6543/traverse/country/236/subdivisions/4615

Open your browser to http://0.0.0.0:6543/traverse/subdivision/4615/country/subdivisions/4617
