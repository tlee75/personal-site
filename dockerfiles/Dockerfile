FROM python:3.8-alpine3.19

RUN apk add bash \
    && apk add git


RUN pip install --upgrade pip

COPY requirements.mkdocs.txt requirements.mkdocs.txt
RUN python3 -m pip install -r requirements.mkdocs.txt

COPY ./docs docs
COPY ./mkdocs.yml mkdocs.yml


EXPOSE 8000

ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
