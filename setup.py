from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='pythonchile.content',
      version=version,
      description="Content Types for PythonChile website",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='python chile jobs companies',
      author='Alvaro Aguirre',
      author_email='aaguirre@kundart.com',
      url='https://github.com/pythonchile',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pythonchile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          'plone.app.dexterity [grok]',
          'plone.app.referenceablebehavior',
          'plone.app.relationfield',
          'plone.namedfile [blobs]', # makes sure we get blob support
          'archetypes.schemaextender',
          'plone.app.registry',

          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
