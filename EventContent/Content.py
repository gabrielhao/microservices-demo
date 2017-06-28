from flask import Flask
from flask_restful import reqparse, Api, Resource
from models import ContentItem
from persist import session, init_db
import sys
import logging


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('eventcontent')
parser.add_argument('eventid', type=int)

class EventContent(Resource):

    def get(self):
        args = parser.parse_args()
        event_id = args["eventid"]
        content = ContentItem.query.filter_by(event_id=event_id).first()
        return content.desc

    def post(self):
        args = parser.parse_args()
        content = args["eventcontent"]
        event_id = args["eventid"]
        item = ContentItem(event_id, content)
        session.add(item)
        session.flush()
        return item.id, 201

    def put(self):
        args = parser.parse_args()
        content = args["eventcontent"]
        event_id = args["eventid"]
        ContentItem.query.filter_by(event_id=event_id).update(desc=content)
        return content

    @staticmethod
    def delete(event_id):
        item = ContentItem.query.filter_by(event_id=event_id).first()
        session.delete(item)
        session.commit()
        return item.desc, 204


api.add_resource(EventContent, '/api/v1.0/eventcontents', '/api/v1.0/eventcontents/<int:event_id>')


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
