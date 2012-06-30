from setuptools import setup, find_packages

version = '0.1'

setup(name='cibuddy',
      version=version,
      description="Class to use the iBuddy device with python",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ibuddy class api',
      author='\xc3\x81lex Gonz\xc3\xa1lez',
      author_email='agonzalezro@gmail.com',
      url='http://twitter.com/agonzalezro',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['python-usb'],
      )
