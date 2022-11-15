install:
		python3 -m venv ./.virtualenv &&\
			source .virtualenv/bin/activate &&\
				python3 -m pip install --upgrade pip &&\
					pip install -r requirements.txt

lint:
		pylint --disable=R,C lint.py


test:
		pytest -vv --cov=lint test.py