#!/bin/sh
docker compose up -d

docker compose exec broker \
  kafka-topics --create \
    --topic calculator_requests \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1

docker compose exec broker \
  kafka-topics --create \
    --topic calculator_results \
    --bootstrap-server localhost:9092 \
    --replication-factor 1 \
    --partitions 1

# Make sure a virtual environment is running when you run this command
python ./client/producer.py ./client/getting_started.ini & python ./server/consumer.py ./client/getting_started.ini 