import json
from services import send_notification
from rbmq import connect_rabbit


connection, channel = connect_rabbit()


def process_new_orders_callback(ch, method, properties, body):
    print(" [x] process_new_orders_callback Received %r" % body)
    order = json.loads(body)
    order['status'] = 'in work'
    order['accept'] = True
    ch.basic_publish(exchange='', routing_key='process_orders', body=json.dumps(order))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def notify_customers_callback(ch, method, properties, body):
    print(" [x] notify_customers_callback Received %r" % body)
    order = json.loads(body)
    send_notification(order)
    print("method.delivery_tag === ", method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume('new_orders', process_new_orders_callback)
channel.basic_consume('process_orders', notify_customers_callback)


channel.start_consuming()
