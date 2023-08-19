FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV POSTGRES_USER='postgres'
    POSTGRES_HOST='db'
    POSTGRES_PASSWORD='postgres'
    POSTGRES_DATABASE='django'


EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

