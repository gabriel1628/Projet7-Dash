import joblib, dill
import json
from flask import Flask, request
import numpy as np
import pandas as pd

pipeline = None

def load_pipeline():
    global pipeline
    # pipeline variable refers to the global variable
    with open('pipeline_projet7.joblib', 'rb') as f:
        pipeline = joblib.load(f)


def load_explainer():
    global explainer
    # pipeline variable refers to the global variable
    with open('explainer.dill', 'rb') as f:
        explainer = dill.load(f)


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
        # Get the data
        data_json = request.get_json()  # Get data posted as a json
        data = data_json['data']
        data = np.array(data)[np.newaxis, :]  # converts shape from (p,) to (1, p)

        # Prediction
        pred = pipeline.predict_proba(data)[0, 0]

        # Feature importance
        ## Global importance
        model = pipeline['model']
        coefs = pd.Series(model.coef_[0], index=data_json['features_name'])
        coefs_abs_sort = coefs.abs().sort_values(ascending=False)
        global_feats = list(coefs[coefs_abs_sort.index].index)
        global_vals = - coefs[coefs_abs_sort.index].values  # on prend l'opposé pour plus de lisibilité

        ## Local importance
        explanation = explainer.explain_instance(data,
                                                 pipeline['model'].predict_proba,
                                                 num_features=20)

        explanation_map = explanation.as_map()[1]
        local_feats = np.array(data_json['features_name'])[[x[0] for x in explanation_map]]
        local_vals = [x[1] for x in explanation_map]
        # On prend l'opposée des valeurs pour que ça soit plus lisible
        local_vals = - np.array(local_vals)

        # Imputation
        imputer = pipeline[0]
        X_imp = imputer.transform(np.array(data_json['data']))

    return {'prediction': pred, 'global_imp_features': global_feats, 'global_imp_values': global_vals,
            'local_imp_features': local_feats, 'local_imp_values': local_vals, 'X_imputed': X_imp}


if __name__ == '__main__':
    load_pipeline()  # load model at the beginning once only
    load_explainer()
    app.run(host='0.0.0.0', port=80)
