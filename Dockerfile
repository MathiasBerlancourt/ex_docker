FROM python:3.9-slim
COPY authentification.py /
ENV LOG 1
CMD python3 authentification.py
