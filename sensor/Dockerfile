FROM python:3-alpine3.11

WORKDIR /sensor

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY sensor.py .

CMD ["python", "sensor.py"]
