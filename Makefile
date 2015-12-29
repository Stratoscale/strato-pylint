all: packages

clean:
	rm -rf build dist strato_pylint.egg-info

packages: build/strato-pylint.tar.gz build/rpm/strato-pylint.rpm
	
build/strato-pylint.tar.gz:
	python setup.py sdist

build/rpm/strato-pylint.rpm:
	python setup.py bdist --format=rpm

install:
	pip install .
