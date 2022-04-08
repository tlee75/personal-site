FROM python:3.9.12-slim-bullseye

WORKDIR /app-files

ADD .. /app-files

EXPOSE 443

RUN pip3 install --user psycopg2-binary~=2.6
RUN pip3 install --user --trusted-host pypi.python.org -r requirements.txt

CMD ["python3", "app.py"]