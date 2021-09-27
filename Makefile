init:
	pip install -r requirements.txt

initdb:
	python initdb.py

lint:
	pylint --ignored-classes=SQLAlchemy flaskpet/models.py
test:
	python -m unittest tests.test_unit
behave:
	python -m behave tests/features

run:
	python run.py