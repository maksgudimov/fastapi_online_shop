import json


def send_notification(order):
    print(f"Sending notification for user {order['user_id']}\n\n"
          f"{json.dumps(order, indent=4)}")
