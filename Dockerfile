FROM python:3.10.3

ENV FLASK_APP=backpythonkpi

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY backpythonkpi /opt/backpythonkpi

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT


