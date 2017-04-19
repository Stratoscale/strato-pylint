all: packages

clean:
	rm -rf build dist strato_pylint.egg-info

packages: build/strato-pylint.tar.gz

build/strato-pylint.tar.gz:
	python setup.py sdist

install:
	pip install .

upload: packages
	python setup.py sdist upload -r http://strato-pypi.dc1:5002/strato/staging/
