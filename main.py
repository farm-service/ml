from flask import Flask, jsonify
import pickle

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    with open('forecaster_hawaii_m.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # Make predictions (Adapt if your data input is different)
    predictions = loaded_model.predict(steps=7)

    return jsonify(predictions.tolist())


if __name__ == '__main__':
    app.run(debug=True)
