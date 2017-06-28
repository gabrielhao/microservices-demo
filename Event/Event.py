from flask import Flask
from flask_restful import reqparse, Api, Resource
import sys
import logging
from kafka_event import EventStore
from models import EventItem
from persist import session, init_db


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('event')

class Event(Resource):
    #get last event
    def get(self, event_id=None):
        if event_id is not None:
            item = EventItem.query.filter_by(id=event_id).first()
        else:
            item = EventItem.query.first()

        return item.title

    def post(self):
        args = parser.parse_args()
        event = args['event']
        #app.logger("post event: "+ event)
        item = EventItem(title=event)
       # app.logger("post: "+ item.title)
        session.add(item)
        session.flush()
        return item.id, 201

    def put(self, event_id):
        args = parser.parse_args()
        event = args['event']
        EventItem.query.filter_by(id=event_id).update(title=event)

        return event

    def delete(self, event_id):
        item = EventItem.query.filter_by(id=event_id).first()
        EventStore.delete(item)
        session.delete(item)
        session.commit()
        return item.title, 204

#api.add_resource(Event, '/api/v1.0/events')
api.add_resource(Event, '/api/v1.0/events','/api/v1.0/events/<int:event_id>')


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
