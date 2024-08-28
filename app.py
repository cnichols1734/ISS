from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# http://98.39.74.161:5001

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/iss_location')
def iss_location():
    # Fetch ISS position from wheretheiss.at API
    try:
        iss_response = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
        iss_data = iss_response.json()

        return jsonify({
            'latitude': iss_data['latitude'],
            'longitude': iss_data['longitude'],
            'altitude': iss_data['altitude'],
            'velocity': iss_data['velocity'],
            'timestamp': iss_data['timestamp']
        })
    except Exception as e:
        print(f"Error fetching ISS data: {e}")
        return jsonify({'error': 'Failed to fetch ISS data'}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

