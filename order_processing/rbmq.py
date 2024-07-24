import pika

# # Параметры подключения
# connection_params = pika.ConnectionParameters(
#     host='localhost',
#     port=5672,
#     virtual_host='/',
#     credentials=pika.PlainCredentials(
#         username='guest',
#         password='guest'
#     )
# )
#
#
# connection = pika.BlockingConnection(connection_params)
# channel = connection.channel()


def connect_rabbit():
    queue_names = [
        'new_orders',
        'process_orders',
        'notify_customers'
    ]

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq')) #localhost
    channel = connection.channel()

    [channel.queue_declare(queue=queue_name) for queue_name in queue_names]

    return connection, channel
