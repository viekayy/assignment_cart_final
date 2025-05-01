FROM python:3.10-slim
WORKDIR /app
COPY ./cart_backend /app
COPY ./requirements.txt /app/requirements.txt
COPY wait-for-it.sh /app/wait-for-it.sh
RUN apt-get update && apt-get install -y netcat-openbsd
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /app/wait-for-it.sh
EXPOSE 8000:8000
CMD sh -c "/app/wait-for-it.sh db 5432 -- python manage.py migrate && python create_superuser.py && python manage.py runserver 0.0.0.0:8000"