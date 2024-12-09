from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from models import db
from routes import ActivityLog, DailyReport

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

api = Api(app)
api.add_resource(ActivityLog, '/activity')
api.add_resource(DailyReport, '/report')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
