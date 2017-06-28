from flask import Flask
from flask_restful import reqparse, Api, Resource
from models import ContentItem
from persist import session, init_db


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class EventContent(Resource):

    def get(self):
        args = parser.parse_args()
        event_id = int({"event_id": args["eventid"]})
        content = ContentItem.query.filter(event_id=event_id)
        return content.desc

    def post(self):
        args = parser.parse_args()
        content = {"content": args["eventcontent"]}
        event_id = int({"event_id": args["eventid"]})
        item = ContentItem(event_id, content)
        session.add(item)
        session.flush()
        return item.id, 201

    def put(self):
        args = parser.parse_args()
        content = {"content", args["eventcontent"]}
        event_id = int({"event_id", args["eventid"]})
        ContentItem.query.filter(event_id=event_id).update(desc=content)
        return content

    def delete(self, event_id):
        item = ContentItem.query.filter(event_id=event_id)
        session.delete(item)
        session.commit()
        return item.desc, 204

    def delete(self):
        args = parser.parse_args()
        event_id = int({"event_id", args["eventid"]})
        self.delete(event_id)

api.add_resource(EventContent, '/api/v1.0/eventcontents')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
