from flask import Flask
from config import config_by_name

app = Flask(__name__)

# Cargar configuración según el entorno
env = os.getenv('FLASK_ENV', 'development')  # 'development', 'testing', 'production'
app.config.from_object(config_by_name[env])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flow_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
lorawan = LoRaManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/realtime', methods=['GET'])
def get_realtime_data():
    """Fetch the latest 10 records from the database."""
    data = FlowData.query.order_by(FlowData.timestamp.desc()).limit(10).all()
    return jsonify([d.to_dict() for d in data])

@app.route('/api/historical', methods=['GET'])
def get_historical_data():
    """Fetch historical data based on a date range."""
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if start_date and end_date:
        data = FlowData.query.filter(FlowData.timestamp.between(start_date, end_date)).all()
        return jsonify([d.to_dict() for d in data])
    return jsonify({'error': 'Invalid date range'}), 400

@app.route('/api/air_volume', methods=['POST'])
def calculate_air_volume():
    """Calculate the total volume of air consumed in a time range."""
    start_date = request.json.get('start_date')
    end_date = request.json.get('end_date')
    if start_date and end_date:
        data = FlowData.query.filter(FlowData.timestamp.between(start_date, end_date)).all()
        total_volume = sum(d.flow_rate for d in data)
        return jsonify({'total_volume': total_volume})
    return jsonify({'error': 'Invalid date range'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(debug=True)