FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV POSTGRES_USER='postgres'
ENV POSTGRES_HOST='db'
ENV POSTGRES_PASSWORD='postgres'
ENV POSTGRES_DATABASE='django'

EXPOSE 8000

RUN chmod +x /app/setup.sh

ENTRYPOINT ["/app/setup.sh"]

