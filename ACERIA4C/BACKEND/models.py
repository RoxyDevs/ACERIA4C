from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FlowData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    flow_rate = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.isoformat(),
            'flow_rate': self.flow_rate
        }