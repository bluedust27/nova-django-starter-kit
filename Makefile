run:
	python backend/manage.py runserver

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

migrate:
	docker compose exec web python /app/backend/manage.py makemigrations
	docker compose exec web python /app/backend/manage.py migrate

createsuperuser:
	docker compose exec web python /app/backend/manage.py createsuperuser

shell-docker:
	docker compose exec web python backend/manage.py shell

createapp:
	docker compose exec web python /app/backend/manage.py startapp $(appname)

local:

	uv pip sync -r requirements/local.txt --update

	@echo "Building Docker image for local..."
	docker compose build

	@echo "Starting Docker containers..."
	docker compose up -d

prod:
	@echo "Adding psycopg for local development..."
	uv pip sync -r requirements/prod.txt --update

	@echo "Building Docker image"
	docker compose build

	@echo "Starting Docker containers..."
	docker compose up -d

pre-commit:
	pre-commit run --all-files --verbose

