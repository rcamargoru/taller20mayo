#archivo Dockerfile
FROM python:3.12.3-slim
WORKDIR /app
COPY martes19.py /app/
COPY uninpahu.db /app/uninpahu.db
CMD ["python","martes19.py"]
