import joblib
import dill
from starlette.requests import Request
from typing import Dict
import numpy as np
import pandas as pd
from ray import serve


# 1: Define a Ray Serve deployment
@serve.deployment(route_prefix="/")
class PipelineHandler:
    def __init__(self, pipeline_path, explainer_path):
        self.pipeline = joblib.load(pipeline_path)
        with open(explainer_path, 'rb') as f:
            self.explainer = dill.load(f)

    async def __call__(self, starlette_request: Request) -> Dict:
        input = await starlette_request.json()

        # Prediction
        pred = self.pipeline.predict_proba(input['data'])[0, 0]

        # Feature importance

        # Global importance
        model = self.pipeline['model']
        coefs = pd.Series(model.coef_[0], index=input['features_name'])
        coefs_abs_sort = coefs.abs().sort_values(ascending=False)
        global_feats = list(coefs[coefs_abs_sort.index].index)
        global_vals = - coefs[coefs_abs_sort.index].values  # on prend l'opposé pour plus de lisibilité

        # Local importance
        explanation = self.explainer.explain_instance(np.array(input['data'][0]),
                                                      self.pipeline['model'].predict_proba,
                                                      num_features=20)

        explanation_map = explanation.as_map()[1]
        local_feats = np.array(input['features_name'])[[x[0] for x in explanation_map]]
        local_vals = [x[1] for x in explanation_map]
        # On prend l'opposée des valeurs pour que ça soit plus lisible
        local_vals = - np.array(local_vals)

        # Imputation
        imputer = self.pipeline[0]
        X_imp = imputer.transform(np.array(input['data']))

        return {'prediction': pred, 'global_imp_features': global_feats, 'global_imp_values': global_vals,
                'local_imp_features': local_feats, 'local_imp_values': local_vals, 'X_imputed': X_imp}


# 2: Deploy the model
defaultrisk_pipeline = PipelineHandler.bind(pipeline_path='pipeline_projet7.joblib',
                                            explainer_path='explainer.dill')
