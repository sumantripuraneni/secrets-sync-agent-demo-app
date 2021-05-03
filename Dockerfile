FROM registry.redhat.io/rhel8/python-38

COPY app.py requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python","app.py"]
