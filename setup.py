#!/usr/bin/env python
from setuptools import setup

INSTALL_REQUIRES = [
    "suds-jurko >= 0.6",
]

setup(
  name = 'turbosmsua',
  packages = ['turbosmsua'],
  version = '0.1',
  description = 'Client for https://turbosms.ua',
  author = 'Serbokryl Oleg',
  author_email = 'chezar1995@gmail.com',
  url = 'https://github.com/Krokop/turbosmsua', 
  download_url = 'https://github.com/Krokop/turbosmsua/tarball/0.1',
  keywords = ['turbosmsua', 'sms ua'],
  classifiers = [],
  install_requires = INSTALL_REQUIRES,
)