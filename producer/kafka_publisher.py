import json
from mongo_connection import collection

from confluent_kafka import Producer

producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode("utf-8")}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")
cursor = collection.find({},{"_id": 0})
for c in cursor:
    value = json.dumps(c).encode('utf-8')
    producer.produce(
    topic="suspicious_customers_orders",
    value=value,
    callback=delivery_report)
    producer.flush(timeout=0.5)