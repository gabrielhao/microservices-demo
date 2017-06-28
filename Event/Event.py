from flask import Flask
from flask_restful import reqparse, Api, Resource

from kafka_event import EventStore
from models import EventItem
from persist import session, init_db


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class Event(Resource):
    #get last event
    def get(self, event_id=None):
        if event_id is not None:
            event = EventItem.query.filter(id=event_id)
        else:
            event = EventItem.query.first()

        return event.title

    def post(self):
        args = parser.parse_args()
        event = args["event"]
        item = EventItem(title=event)
        session.add(event)
        session.flush()
        return event.id, 201

    def put(self, event_id):
        args = parser.parse_args()
        event = args["event"]
        EventItem.query.filter(id=event_id).update(title=event)

        return event

    def delete(self, event_id):
        event = EventItem.query.filter(id=event_id)
        EventStore.delete(event)
        session.delete(event)
        session.commit()

        return event.title, 204

api.add_resource(Event, '/api/v1.0/events')


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
