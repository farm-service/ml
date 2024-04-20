from flask import Flask, jsonify
import pickle
from datetime import timedelta, datetime
from math import ceil

app = Flask(__name__)


@app.route('/forecast', methods=['GET'])
def predict():
    with open('forecaster_hawaii_m.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # Make predictions (Adapt if your data input is different)
    predictions = loaded_model.predict(steps=7)

    start_date = datetime(2016, 1, 1)

    predictions = [{'product_id': 1, 'amount': ceil(p), 'date': start_date + timedelta(days=i)} for i, p in
                   enumerate(predictions)]

    return jsonify(predictions)


if __name__ == '__main__':
    app.run(debug=True)
