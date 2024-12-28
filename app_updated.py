from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Function to get the current price from Binance API
def get_current_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return float(data["price"])
    else:
        return None

@app.route('/predict', methods=['GET'])
def predict_price():
    current_price = get_current_price()
    if current_price is None:
        return jsonify({"error": "Failed to fetch current price"}), 500
    
    # Simple prediction example (2% increase)
    prediction = current_price * 1.02  # Example prediction logic
    return jsonify({
        "current_price": current_price,
        "prediction": prediction
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
