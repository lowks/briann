from setuptools import setup

setup(name='briann',
      version='0.0.2',
      description='briann',
      url='http://github.com/leehart/briann',
      author='Lee Hart',
      author_email='lee.hart@well.ox.ac.uk',
      license='',
      packages=['briann'],
      entry_points = {
        'console_scripts': ['Brian=briann.__init__:main'],
      },
      install_requires=['numpy'],
      zip_safe=False)
