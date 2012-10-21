from setuptools                 import setup
from setuptools                 import find_packages
from setuptools.command.test    import test as TestCommand

import sys

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        result = pytest.main(self.test_args)
        sys.exit(result)

name = 'sqlalchemy_traversal_demo'

requires = [
    'setuptools'
    , 'pyramid'
    , 'pyramid_debugtoolbar'
    , 'pyramid_tm'
    , 'zope.interface'
    , 'pycountry'
    , 'waitress'
    , 'SQLAlchemy'
    , 'zope.sqlalchemy'
    , 'sqlalchemy_traversal'
]

setup(
    name = name
    , version='0.1'
    , url='http://github.com/eventray/' + name
    , author='John Anderson'
    , author_email='sontek@gmail.com'
    , packages=find_packages()
    , include_package_data = True
    , install_requires = requires
    , tests_require = requires + ['pytest', 'mock', 'webtest']
    , zip_safe = False
    , cmdclass = {'test': PyTest}
    , entry_points="""\
      [paste.app_factory]
      main = sqlalchemy_traversal_demo:main
      [console_scripts]
      initialize_sqlalchemy_traversal_demo_db = sqlalchemy_traversal_demo.scripts.initializedb:main
      """
)
