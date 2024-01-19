FROM python:3.11

WORKDIR /app
COPY pyproject.toml /app/
#COPY frontend /
#COPY keys_https /
RUN pip install poetry && poetry install
COPY . /app

RUN chmod u+x app/setup.py
#RUN poetry run python app/setup.py

CMD cd app && poetry run uvicorn main:app --host 0.0.0.0 --port 8000

#CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
