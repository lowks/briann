from setuptools import setup

setup(name='brian',
      version='0.0.1',
      description='',
      url='http://github.com/leehart/brian',
      author='Lee Hart',
      author_email='lee.hart@well.ox.ac.uk',
      license='',
      packages=['brian'],
      entry_points = {
        'console_scripts': ['brian=brian.cli:main'],
      },
      zip_safe=False)