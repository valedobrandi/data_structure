FROM python:3-alpine3.17

WORKDIR /src

COPY src/*requeriments.txt ./
RUN pip install --no-cache-dir -r requeriments.txt

ARG FLASK_ENV

RUN if ["$FLASK_ENV" = "dev"] ; then pip install --no-cache-dir -r dev-requeriments.txt ; fi

COPY ./src .

CMD ["python3", "app.py"]