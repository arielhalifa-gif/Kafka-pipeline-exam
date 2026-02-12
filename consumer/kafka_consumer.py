import json

from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "week-17-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["suspicious_customers_orders"])

print("🟢 Consumer is running and subscribed to orders topic")

customers_lst = []
orders_lst = []


try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        suspicious_customers = json.loads(value)
        for suspicious in suspicious_customers:
            if suspicious['type'] == 'customers':
                customers_lst.append(suspicious)
            elif suspicious['type'] == 'orders':
                orders_lst.append(suspicious)
except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.close()

total_tables = {'customers': customers_lst,
                'orders': orders_lst}