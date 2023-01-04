import joblib
import json
from flask import Flask, request
import numpy as np

model = None

def load_model():
    global model
    # model variable refers to the global variable
    with open('pipeline_projet7.joblib', 'rb') as f:
        model = joblib.load(f)


app = Flask(__name__)

# Customized JSONEncoder class to serialize numpy objects
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


app.json_encoder = NpEncoder

@app.route('/', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        data_json = request.get_json()  # Get data posted as a json
        data = data_json['data']
        data = np.array(data)[np.newaxis, :]  # converts shape from (p,) to (1, p)
        prediction = model.predict(data)  # runs globally loaded model on the data
    return {'prediction': prediction}
    #return str(prediction[0])


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=80)
