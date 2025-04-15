FROM python:3.12-alpine as builder

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libpq-dev \
    build-base

WORKDIR /app

COPY requirements /app/requirements
RUN pip install --upgrade pip
RUN pip install --prefix=/install --no-cache-dir -r requirements/prod.txt


FROM python:3.12-alpine

RUN apk add --no-cache libpq-dev

WORKDIR /app

COPY --from=builder /install /usr/local

COPY backend /app/backend
