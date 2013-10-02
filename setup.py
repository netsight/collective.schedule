from setuptools import setup, find_packages
import os

version = '0.1.4'

long_description = (
    open('README.md').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.schedule',
      version=version,
      description="Plone integration for the python 'schedule' library",
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='python plone schedule cron',
      author='Matt Sital-Singh',
      author_email='',
      url='https://github.com/netsight/collective.schedule',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'schedule',
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )
