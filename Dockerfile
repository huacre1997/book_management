# Base con variables de entorno compartidas
FROM python:3.11-slim as python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Etapa de construcción de dependencias
FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libkrb5-dev \
    && apt-get clean

# Instalar Poetry
ENV POETRY_VERSION=1.6.1
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copiar archivos de dependencias
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./

# Instalar solo las dependencias principales del proyecto
RUN poetry install --no-interaction --no-root

# Etapa de producción: Copia las dependencias compiladas
FROM python-base as production

COPY --from=builder-base $VENV_PATH $VENV_PATH
COPY . /app
WORKDIR /app

# Instalar librerías necesarias en producción
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        libkrb5-3 \
    && apt-get clean

EXPOSE 80

# Ejecutar la API
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
