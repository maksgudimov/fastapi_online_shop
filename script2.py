import pika


# def connection():
#     # Параметры подключения
#     connection_params = pika.ConnectionParameters(
#         host='localhost',  # Замените на адрес вашего RabbitMQ сервера
#         port=5672,  # Порт по умолчанию для RabbitMQ
#         virtual_host='/',  # Виртуальный хост (обычно '/')
#         credentials=pika.PlainCredentials(
#             username='guest',  # Имя пользователя по умолчанию
#             password='guest'  # Пароль по умолчанию
#         )
#     )
#     # Установка соединения
#     connection = pika.BlockingConnection(connection_params)
#     # Создание канала
#     channel = connection.channel()
#     return connection, channel
#
#
# def declare_queues(channel):
#     channel.queue_declare(queue='new_orders')
#     channel.queue_declare(queue='process_orders')
#     channel.queue_declare(queue='notify_customers')
#
#
# def create_order(order_data):
#     order = {
#         'id': order_data.get('id'),
#         'customer_name': order_data.get('customer_name'),
#         'items': order_data.get('items'),
#         'total': order_data.get('total')
#     }
#     return order
#
#
# def validate_order(order):
#     if not order.get('id'):
#         raise ValueError("Order must have an ID")
#     if not order.get('customer_name'):
#         raise ValueError("Order must have a customer name")
#     if not order.get('items') or not isinstance(order['items'], list) or len(order['items']) == 0:
#         raise ValueError("Order must have at least one item")
#     if not order.get('total') or not isinstance(order['total'], (int, float)) or order['total'] <= 0:
#         raise ValueError("Order must have a valid total amount")
#     return True
#
#
# def publish_message():
#     pass
#
#
# def consume_message():
#     pass
#
#
# def connection_close(connection):
#     connection.close()
#
#
# if __name__ == "__main__":
#     connection, channel = connection()
#     declare_queues(channel)

# --------------------------------------------- #

