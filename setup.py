# -*- coding: utf-8 -*-
"""
This module contains the tool of redomino.tokenroleform
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.4'

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt'))

tests_require = ['zope.testing']

setup(name='redomino.tokenroleform',
      version=version,
      description="Token Role Form",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='Davide Moro',
      author_email='davide.moro@redomino.com',
      url='https://github.com/redomino/redomino.tokenroleform',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['redomino', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        'Products.PloneFormGen',
                        'redomino.tokenrole',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='redomino.tokenroleform.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
