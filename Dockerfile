FROM python:3.12-slim

WORKDIR /app

COPY monitor.py .

RUN pip install requests

CMD ["python", "monitor.py"]