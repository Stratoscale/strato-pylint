# Strato Pylint

strato-pylint is a modified version of pylint that was added support for split packages.
See issue here: http://www.logilab.org/8796
# Installation

```sh
$ sudo make install
```
> It will request root password during the installation

# Usage
### pep8
Your code should comply with pep8 - "Style Guide for Python Code"

Found here: https://www.python.org/dev/peps/pep-0008/

You should add the following line to your Makefile:
```Makefile
../strato-pylint/pep8.sh DIR_TO_TEST
```
### pylint
Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for bad code smells.

This repository comes with a predefined recommended configuration.
any improvements are welcomed.

you should add the flowing line to your Makefile:
```makefile
../strato-pylint/pylint.sh DIR_TO_TEST
```

If you want to enable the split packages feature you could add instead:
```makefile
UPSETO_JOIN_PYTHON_NAMESPACES=yes PYTHONPATH=py:. ../strato-pylint/pylint.sh py/
```

# Return Code
The shell scripts will return 0 on success and non-zero on failure.
