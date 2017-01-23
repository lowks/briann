from setuptools import setup

setup(name='briann',
      version='0.0.1',
      description='',
      url='http://github.com/leehart/briann',
      author='Lee Hart',
      author_email='lee.hart@well.ox.ac.uk',
      license='',
      packages=['briann'],
      entry_points = {
        'console_scripts': ['briann=briann.cli:main'],
      },
      zip_safe=False)