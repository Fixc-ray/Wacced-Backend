from flask import request, jsonify
from flask_restful import Resource
from models import db, Activity


class ActivityLog(Resource):
    def post(self):
        try:
            data = request.get_json()
            activity = Activity(
                user_id=data['user_id'],
                activity_name=data['activity_name'],
                duration=data['duration'],
                health_score=data['health_score']
            )
            db.session.add(activity)
            db.session.commit()
            return {'message': 'Activity logged successfully!'}, 201
        except Exception as e:
            return {'error': str(e)}, 400
class DailyReport(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        activities = Activity.query.filter_by(user_id=user_id).all()
        report = {
            'activities': [
                {
                    'name': activity.activity_name,
                    'duration': activity.duration,
                    'score': activity.health_score
                } for activity in activities
            ],
            'average_score': sum(a.health_score for a in activities) / len(activities) if activities else 0
        }
        return jsonify(report)
