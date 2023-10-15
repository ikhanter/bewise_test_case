dev:
	poetry run flask --app bewise_test_case:app run --debug

lint:
	poetry run flake8 ./beware_test_case/

install:
	poetry install

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:5000 bewise_test_case:app
