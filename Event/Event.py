from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from kafka_event import EventStore

iapp = Flask(__name__)
api = Api(app)

class Event(Resource):
    def get(self):
        return EventStore.getEvents()

    def get(self, event_id):
        return EventStore.getEventbyId(event_id)

    def post(self):
        args = parser.parse_args()
        event = {"event": args["event"]}
        return EventStore.createEvent(event), 201
    def put(self, event_id):
        args = parser.parse_args()
        event = {"event", args["event"]}
        return EventStore.updateEvent(event, event_id)

     def delete(self, event_id):
        return EventStore.deleteEvent(event_id), 204

api.add_resource(Event, '/api/v1.0/events')


if __name__ == '__main__':
    app.run(debug=True)
        
        
