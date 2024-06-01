FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5007
CMD ["gunicorn", "-b", "0.0.0.0:5007", "app:app"]
