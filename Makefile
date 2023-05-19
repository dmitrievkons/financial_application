debug:
	poetry run flask --app financial_app_code.main:financial_app --debug run

start:
	poetry run flask --app financial_app_code.main:financial_app run