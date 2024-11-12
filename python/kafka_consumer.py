from kafka import KafkaConsumer
import json

# Create a Kafka consumer
consumer = KafkaConsumer(
    "test-topic",  # Topic to subscribe to
    bootstrap_servers="deby.lan:29092",  # Replace with your Kafka broker address
    auto_offset_reset="earliest",  # Start reading at the earliest message
    enable_auto_commit=True,  # Automatically commit offsets
    group_id="test-group",  # Consumer group ID
    value_deserializer=lambda x: json.loads(
        x.decode("utf-8")
    ),  # Deserialize JSON messages
)

# Read messages
try:
    for message in consumer:
        print(
            f"Received: {message.value}, Key: {message.key}, Offset: {message.offset}"
        )
except KeyboardInterrupt:
    consumer.close()  # Close the consumer on exit
finally:
    consumer.close()  # Close the consumer on exitfrom kafka import KafkaProducer
