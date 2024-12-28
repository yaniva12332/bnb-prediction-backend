from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict_price():
    return jsonify({
        "current_price": 300.50,
        "prediction": 305.75
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
