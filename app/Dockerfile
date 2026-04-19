FROM python:3.12-slim

ARG BUILD_VERSION=dev
ARG APP_NAME="FastAPI Template"
ARG APP_ENV=prod
ENV APP_VERSION=$BUILD_VERSION
ENV APP_NAME=$APP_NAME
ENV APP_ENV=$APP_ENV

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
