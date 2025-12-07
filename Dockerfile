FROM python:3.10-slim

WORKDIR /app

COPY Migrate_to_mongo.py .
COPY requirements.txt .
COPY healthcare_dataset.csv .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "Migrate_to_mongo.py"]