FROM python:3.10-slim

#RUN apt-get update && apt-get install -y \
#  curl \
#  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app

#ENTRYPOINT ["gunicorn", "app.main:app", "-k uvicorn.workers.UvicornWorker"]
ENTRYPOINT ["gunicorn", "app.main:app", "-k app.main.ServerlessUvicornWorker"]
