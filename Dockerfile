FROM python:3.11

COPY pyproject.toml ./

RUN pip install pipenv
RUN pipenv install --dev


CMD mkdir -p /workspace
WORKDIR /workspace
