FROM python:3.10

WORKDIR /app
COPY ./poetry.lock .
COPY ./pyproject.toml .
COPY ./oi/ai/mleng/takehome/pipeline oi/ai/mleng/takehome/pipeline
COPY ./oi/ai/mleng/takehome/backend oi/ai/mleng/takehome/backend
COPY ./data/labels data/labels

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

ENV PYTHONPATH=/app
EXPOSE 8000

WORKDIR /app/oi/ai/mleng/takehome/backend

CMD ["uvicorn", "api:app", "--host", "0.0.0.0"]
