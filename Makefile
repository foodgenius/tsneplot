all: init

clean-pyc:
	-@find . -name '*.pyc' -exec rm --force {} +
	-@find . -name '*.pyo' -exec rm --force {} +
	-@find . -name '*~' -exec rm --force  {} +
	-@find . -name '__pycache__' -exec rm --force --recursive {} +

clean-venv:
	-@test -d venv && rm -r venv || true

clean: clean-pyc clean-venv
	-@find . -name '*.egg-info' -exec rm --force --recursive {} +
	-@find . -name 'build' -exec rm --force --recursive {} +
	-@find . -name 'dist' -exec rm --force --recursive {} +

venv: venv/bin/activate
venv/bin/activate:
	test -d venv || virtualenv venv
	venv/bin/pip install -r requirements.txt -r requirements.dev.txt
	touch venv/bin/activate

lint:
	flake8 tsneplot scripts/tsneplot tests

test: venv lint
	nosetests -v tests --nologcapture

cover: venv lint
	test -d test-reports || mkdir -p test-reports
	nosetests -v  tests --with-coverage --cover-package tsneplot \
		--cover-xml --cover-xml-file test-reports/coverage.xml \
		--cover-html --cover-html-dir test-reports \
		--with-xunit --xunit-file test-reports/nosetests.xml
