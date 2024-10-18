from kafka import KafkaProducer
import json

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers='deby.lan:29092',  # Replace with your Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize JSON messages
)

# Send messages
for i in range(100):
    message = {'key': i, 'value': f'Message {i}'}
    producer.send('test-topic', value=message)
    print(f'Sent: {message}')

# Flush the producer to ensure all messages are sent
producer.flush()

# Close the producer
producer.close()
