FROM python:3.11

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

# Команда для запуска Flask
CMD ["python", "run.py"]