from kafka import KafkaProducer



producer = KafkaProducer(bootstrap_servers=['eventstore.service.consul:9092'], api_version=(0,10))
topic = 'event-title-delete'

#producer.send(topic, b"test")

class EventStore(object):
    @staticmethod
    def delete(event):
        producer.send(topic, bytes(event.id))





        
