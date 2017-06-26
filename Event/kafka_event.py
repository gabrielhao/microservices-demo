from kafka import KafkaProducer



producer = KafkaProducer(bootstrap_servers=['kafka.service.consul:9092'])
topic = 'event-title-delete'



class EventStore(object):
    def delete(self, event):
        producer.send(topic, event.id)





        
