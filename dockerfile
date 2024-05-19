# Temel alınacak Docker imajını belirle
FROM python:3.8-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Proje dosyalarını kopyala
COPY . /app/


RUN pip install -r requirements.txt



EXPOSE 8000
ENTRYPOINT ["sh", "-c", "python manage.py migrate && python manage.py makemigrations && python manage.py runserver 0.0.0.0:8000"]