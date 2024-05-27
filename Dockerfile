FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py .
COPY raghu.jpg .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]