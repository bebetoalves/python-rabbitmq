import time
import json
import random
import logging
import pika

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | [%(levelname)s] | %(message)s"
)

rabbitmq_host = "rabbitmq"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.exchange_declare(exchange="sensores", exchange_type="fanout")

while True:
    value = random.randint(1, 100)
    message = json.dumps({"value": value})
    channel.basic_publish(exchange="sensores", routing_key="", body=message)

    logging.info(f"Enviando para o servidor: {value}")

    time.sleep(random.uniform(0, 2))
