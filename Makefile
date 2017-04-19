all: packages

clean:
	rm -rf build dist strato_pylint.egg-info

packages: build/strato-pylint.tar.gz

build/strato-pylint.tar.gz:
	python setup.py sdist

install:
	pip install .
