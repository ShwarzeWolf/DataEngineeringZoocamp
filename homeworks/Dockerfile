FROM python:3.9.1

WORKDIR /app
COPY . ./

RUN pip install -r requirements.txt --no-cache-dir

ENTRYPOINT ["python", "load_data.py"]