"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os
from os import path
from os.path import expanduser
import subprocess

PKG_INFO = 'PKG-INFO'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# add to user site
data_files = [("{}/.config".format(expanduser("~")), ['config/flake8', 'config/pep8', 'config/pylintrc'])]

# add in case we are running as root
if os.geteuid() == 0:
    data_files.append(("/etc", ['config/pylintrc']))


def get_git_version():
    if os.path.exists(PKG_INFO):
        with open(PKG_INFO) as package_info:
            for key, value in (line.split(':', 1) for line in package_info):
                if key.startswith('Version'):
                    return value.strip()

    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode()


setup(
    name='strato_pylint',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=get_git_version(),

    description='A project suppling pylint flask and pep8 utilities.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/Stratoscale/strato-pylint.git',

    # Author details
    author='Stratoscale',
    author_email='support@stratoscale.com',

    # Choose your license
    license='TBD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: TBD',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='pylint pep8 flask8 development',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages('', exclude=['contrib', 'docs', 'tests']),
    packages=find_packages(),

    dependency_links=[
        "http://pip-repo/simple/",
        "http://mirrors.stratoscale.com.s3-website-us-east-1.amazonaws.com/pip/simple",
        "https://pypi.python.org/simple/"
    ],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'pylint==1.9.5; python_version < "3"',
        'pylint>=2.13.9; python_version > "3"',
        'pep8==1.6.2',
        'flake8==2.6.2; python_version < "3"',
        'flake8==5.0.4; python_version > "3"',
        'future; python_version < "3"',
        'flake8-debugger==1.4.0; python_version < "3"',
        'flake8-debugger==3.2.1; python_version > "3"',
        'pep8-naming==0.3.3',
        'logilab-common==1.1.0'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
    },
    include_package_data=True,
    data_files=data_files,
)
