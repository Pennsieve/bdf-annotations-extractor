FROM python:3.13

WORKDIR /extractor

RUN ls

COPY requirements.txt /extractor/requirements.txt

RUN pip install -r requirements.txt

COPY extractor/ /extractor

CMD ["python", "main.py"]