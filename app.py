from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Tree Drive!"

@app.route('/ride', methods=['POST'])
def request_ride():
    data = request.get_json()
    return jsonify({
        "status": "Ride requested",
        "pickup": data.get("pickup"),
        "destination": data.get("destination")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
