from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from models import ContentItem
from persist import session, init_db

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

#all event content is asociated with event ID
class EventContent(Resource):
    def get(self, event_id):
        return EventStore.getEventbyId(event_id)

    def post(self, event_id):
        args = parser.parse_args()
        event = {"eventcontent": args["eventcontent"]}
        return EventStore.createEvent(event, event_id)

    def put(self, event_id):
        args = parser.parse_args()
        event = {"event", args["event"]}
        return EventStore.updateEvent(event, event_id)

    def delete(self, event_id):
        content = EventContent.query.filter(id=event_id)
        session.delete(content)
        session.commit()

        return content.desc, 204

        


api.add_resource(EventContent, '/api/v1.0/eventcontents')


if __name__ == '__main__':
    app.run(debug=True)
