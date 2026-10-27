

FROM python:3.12-slim

WORKDIR /app

COPY ./dc_requarment.txt .

RUN pip install -r dc_requarment.txt

COPY . .

ENV PYTHONPATH=/app

CMD [ "python" , "docker/service_b/py_deploy.py" ]