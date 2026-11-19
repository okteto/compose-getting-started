FROM python:3.15.2-trixie AS dev

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

FROM python:3.15.2-slim-trixie AS prod

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY static static
COPY templates templates
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
