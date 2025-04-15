# Nova Django Starter Kit

A clean, extensible Django project setup with Docker, PostgreSQL, and best practices for team-based development. This project is ideal as a starting point for new Django applications with authentication and reusability built in.

---

## 🚀 Features

### 🔧 Project Structure
- Dockerized setup with Django + PostgreSQL
- `.env` and `.env.example` for environment configs
- Centralized config system using `config.yaml` with feature flags.
- Logging setup.

### 🔐 Authentication Prep
- `users` app with custom User model:
  - Email as username
  - Password
  - `team` field for grouping users
- Placeholder views ready for login/register/logout

### 🧱 Reusability
- `core` app for reusable logic
- `BaseModel` with:
  - UUID primary key
  - `created_at`, `updated_at` timestamps
  - `created_by`, `updated_by` (ForeignKey to User)
  - `is_active` flag for soft deletes

### 📦 Dependency Management
- Split `requirements/` structure:
  - `base.txt`, `local.txt`, `prod.txt`
- `Makefile` with developer commands (`install`, `run`, `migrate`, etc.)

---

## 🐳 Getting Started

### 1. Clone this project

```bash
git clone https://github.com/your-username/nova-django-starter-kit.git
cd nova-django-starter-kit
```
### 2. Create .env from template
```
cp .env.example .env
```
### 3. Build and run using Docker Compose
```docker-compose up --build```

### 4. Apply migrations and create superuser
```
make migrate
make createsuperuser
```
