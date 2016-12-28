import re
from setuptools import setup

# Influence for this taken from https://goo.gl/Pi51aC
version = None
for line in open('./halo5/__init__.py'):
  m = re.search('__version__\s*=\s*(.*)', line)
  if m:
    version = m.group(1).strip()[1:-1]  # quotes
    break
assert version

setup(
  name='halo5.py',
  version=version,
  description='A wrapper for the Halo 5: Guardians API',
  author='Joe Antonakakis',
  author_email='jma353@cornell.edu',
  url='https://github.com/Jma353/halo5.py',
  license='MIT',
  packages=['halo5'],
  include_package_data=True,
  package_data={
    '': ['README.rst']
  },
  install_requires=[
    'requests>=2.12.4',
  ],
  tests_require=[
    'nose>=1.3.7',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet',
    'Topic :: Games/Entertainment :: First Person Shooters',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ]
)
