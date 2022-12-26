initial_command:
	@echo "it is working"
createsuperuser:
	docker-compose run --rm app sh -c "python3 manage.py createsuperuser"
makemigrations:
	docker-compose run --rm app sh -c "python3 manage.py makemigrations ${app_name}"
migrate:
	docker-compose run --rm app sh -c "python3 manage.py migrate"
pytest:
	docker-compose run app sh -c "touch /tmp/db.sqlite3 && pytest"