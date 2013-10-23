#!/usr/bin/env python
from distutils.core import setup

setup(name='localizable',
      version='0.1.2',
      description='Localizable.strings parser for Apple-specific localization files',
      author='Chris Ballinger',
      author_email='chris@chatsecure.org',
      url='https://github.com/chrisballinger/python-localizable',
      license="GPLv2",
      long_description=open('README.md').read(),
      py_modules=['localizable'],
      install_requires=[
        'chardet',
      ],     
)