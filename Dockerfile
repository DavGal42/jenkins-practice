FROM python:3.7-alpine

COPY hello.py /

RUN pip install requests

CMD ["python", "hello.py"]