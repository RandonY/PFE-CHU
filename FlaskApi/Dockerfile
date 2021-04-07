FROM python:3.8

WORKDIR /project

ADD . /project

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["python3","app.py"]