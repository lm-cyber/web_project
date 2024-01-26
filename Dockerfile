FROM python:3.11

WORKDIR /app
RUN git clone https://github.com/emshen6/web-project-front -b env frontend/factory
COPY frontend /app/frontend
RUN apt-get update && apt-get install -y npm
RUN npm install -g yarn

RUN cd frontend/factory && yarn install && yarn build && cd ../../
#COPY keys_https /
COPY pyproject.toml /app/
RUN python3 -m pip config --user set global.timeout 150
RUN pip install poetry && poetry install
COPY . /app
RUN ls && pwd
RUN chmod u+x app/setup.py
#RUN poetry run python app/setup.py

CMD cd app && poetry run uvicorn main:app --host 0.0.0.0 --port 8000

#CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
