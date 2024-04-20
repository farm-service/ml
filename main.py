from flask import Flask, jsonify
import pickle
from datetime import timedelta, datetime
from math import ceil

app = Flask(__name__)


@app.route('/forecast', methods=['GET'])
def predict():
    with open('./models/forecaster_hawaii_m.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # [(1, date1, 2), (5, date1, 7), (1, date2, 5)]
    # Make predictions (Adapt if your data input is different)
    start_date = datetime(2016, 1, 1)
    predictions = loaded_model.predict(steps=7)
    # [element for element in elements]
    predictions = [(1, start_date + timedelta(days=i), p) for i, p in enumerate(predictions)]
    result = dict()
    for p in predictions:
        if p[0] not in result:
            result[p[0]] = dict()
        result[p[0]][str(p[1])] = ceil(p[2])

    return jsonify(result)


@app.route('/test')
def test():
    return jsonify({'message': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
