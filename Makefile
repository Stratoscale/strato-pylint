all: package

clean:
	rm -rf build dist strato_pylint.egg-info

packages: dist/strato_pylint.tar.gz

dist/strato_pylint.tar.gz:
	python setup.py sdist

install:
	pip install .

package: setup.py
	python -m setup sdist

upload: packages
	python setup.py sdist upload -r http://strato-pypi.dc1:5002/strato/staging/
