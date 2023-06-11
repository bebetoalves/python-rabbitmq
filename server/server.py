import logging
import pika
import json

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | [%(levelname)s] | %(message)s"
)

rabbitmq_host = "rabbitmq"
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()
channel.exchange_declare(exchange="sensores", exchange_type="fanout")
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange="sensores", queue=queue_name)


def callback(ch, method, properties, body):
    data = json.loads(body)
    value = data["value"]
    logging.info(f"Leitura recebida: {value}")

    if value > 60:
        logging.critical("Sensor apresentando altas temperaturas!")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
