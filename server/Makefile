include .env

export

postgres-up:
	@docker-compose up -d postgres-service --remove-orphans

postgres-down:
	@docker-compose down postgres-service

migrate:
	@read -p "Enter name migration: " name; \
	PYTHONPATH=. alembic revision --autogenerate -m $$name
	@PYTHONPATH=. alembic upgrade head