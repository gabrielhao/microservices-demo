from kafka import KafkaConsumer
from EventContent import EventContent



consumer = KafkaConsumer(bootstrap_servers=['eventstore.service.consul:9092'],
                        api_version=(0,10), auto_offset_reset='earliest')
topic = 'event-title-delete'
consumer.subscribe(topic)
#producer.send(topic, b"test")

class EventStore(object):
    def delete(self):
        for message in consumer:
            EventContent.delete(int(message.value))
