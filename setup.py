__author__="cooke"
__date__ ="$23-Nov-2011 17:16:55$"
from setuptools import setup, find_packages
import os
setup (
  name = 'django-filer-svg',
  version = '0.1',
  packages = find_packages(),
  install_requires=[
                    'django',
                    'django-cms',
                    'django-filer',
                    'django-south',
                  ],
  
  author = 'Adrian Cooke',
  author_email = 'adriangerardcooke@gmail.com',
  description = 'Django Filer CMS SVG plugin.',
  url = 'https://github.com/agcooke/django-filer-svg',
  zipfile=None,
)
