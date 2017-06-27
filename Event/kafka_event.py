from kafka import KafkaProducer



producer = KafkaProducer(bootstrap_servers=['eventstore.service.consul:9092'], api_version=(0,10))
topic = 'event-title-delete'

#producer.send(topic, b"test")

class EventStore(object):
    def delete(self, event):
        producer.send(topic, event.id)





        
