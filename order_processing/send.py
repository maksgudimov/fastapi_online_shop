import json
from .rbmq import connect_rabbit


def send_order(order: dict):
    connection, channel = connect_rabbit()
    channel.basic_publish(exchange='', routing_key='new_orders', body=json.dumps(order))
    connection.close()
