FROM python:3.13

WORKDIR /extractor

COPY extractor/ /extractor

CMD ["python", "main.py"]