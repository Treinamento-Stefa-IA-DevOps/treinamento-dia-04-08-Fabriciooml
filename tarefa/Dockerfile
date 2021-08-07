FROM centos/python-36-centos7

EXPOSE 5000

COPY . /codigo

WORKDIR /codigo

RUN pip install -r ./codigo/requirements

CMD ["uvicorn", "codigo.main:app","--host", "0.0.0.0", "--port", "5000", "--reload"]
