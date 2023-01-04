import requests
import pandas as pd

def load_X_y(nan):
    X = pd.read_csv('data/X.csv', index_col=0).fillna(nan)
    y = pd.read_csv('data/y.csv', index_col=0)['TARGET']
    return X, y

nan = 1.01010101 # remplacement des NaN par cette valeur
X, y = load_X_y(nan)
client_id = 100004

# 3: Query the deployment and print the result
data_json = {'data': X.loc[client_id].to_list(),
             'features_name': list(X.columns)
             }
headers = {"Content-Type": "application/json"}
model_uri = 'http://127.0.0.1:80/'

response = requests.request(method='POST', headers=headers, url=model_uri, json=data_json)
#pred, global_features, global_vals, local_features, local_vals, X_imp = response.json().values()

print(response)
