FROM python:3.10.3

ENV FLASK_APP=lab_1_rest_api

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY lab_1_rest_api /opt/lab_1_rest_api

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT


