FROM python:3.11.4-slim

EXPOSE 8000/tcp
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY bot /app/bot
COPY .env /app
COPY requirements.txt /app

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y gcc default-libmysqlclient-dev pkg-config

RUN python -m venv /opt/venv \
 && pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "-m", "bot"]