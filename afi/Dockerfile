# python:alpine is 3.{latest}
FROM python:alpine3.8

ENV FLASK_ENV development

LABEL maintainer="Dawei Wu"

RUN pip install flask

RUN apk update \
  && apk add iperf3 \
  && apk add bash \
  && rm -rf /var/cache/apk/*

COPY src /src/

EXPOSE 5000
EXPOSE 5001

ENTRYPOINT ["python", "/src/app.py"]
