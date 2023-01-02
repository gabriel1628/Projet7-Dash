import joblib
from flask import Flask, request
import numpy as np

model = None

def load_model():
    global model
    # model variable refers to the global variable
    with open('pipeline_projet7.joblib', 'rb') as f:
        model = joblib.load(f)


app = Flask(__name__)

# home endpoint, which when hit, returns a ‘Hello World!’ message.
@app.route('/')
def home_endpoint():
    return 'Hello World!'


@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json()  # Get data posted as a json
        data = np.array(data)[np.newaxis, :]  # converts shape from (p,) to (1, p)
        prediction = model.predict(data)  # runs globally loaded model on the data
    return str(prediction[0])


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
