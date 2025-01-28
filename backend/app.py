from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return "Welcome to ARIYA - Artificial Rural Innovation for Youth and Agriculture!"

@app.route('/api/crop-predictions', methods=['GET'])
def get_crop_prediction():
    # For now, just sending a static response as an example
    return jsonify({"crop_prediction": "Wheat"})

if __name__ == '__main__':
    app.run(debug=True)
