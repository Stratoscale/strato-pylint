Installation:
=============
1. Install using pip::
    pip install strato-pylint

2. Install from github::
    git clone https://github.com/stratoscale/strato-pylint.git
    cd strato-pylint
    python setup.py install

Flake8:
=======

flake8 is a wrapper around 3 projects that improve python code:
    * PyFlakes
    * pep8
    * Ned Batchelder’s McCabe script

Flake8 runs all the tools by launching the single flake8 script. It displays the warnings in a per-file, merged output.

In order to config flake8 we took the per-project approch defined in:
    http://flake8.readthedocs.io/en/latest/user/configuration.html

We place the flake8 configuration per project in a flake8 section in the setup.cfg file.


Pylint:
=======


pylint loads it's configuration using the following algoritm (taken from: http://docs.pylint.org/run.html):

1. pylintrc in the current working directory
2. .pylintrc in the current working directory
3. If the current working directory is in a Python module, Pylint searches up the hierarchy of Python modules until it finds a pylintrc file. This allows you to specify coding standards on a module-by-module basis. Of course, a directory is judged to be a Python module if it contains an __init__.py file.
4. The file named by environment variable PYLINTRC
5. if you have a home directory which isn’t /root:
    * .pylintrc in your home directory
    * .config/pylintrc in your home directory
6. /etc/pylintrc

We chose to utilize steps 5 and 6 to configure pylint settings.

Using setup.py we install at ~/.config and at /etc/pylintrc if we install as root -- have permissions to write in /etc.

One can choose to override with specific configurations py adding a .pylintrc in the working project directory.


Return Code:
------------
The shell scripts will return 0 on success and non-zero on failure.
