# Projet-7

Ce repo contient des livrables du projet 7 de la formation Data Scientist chez OpenClassrooms.
On peut y trouver les codes pour le déploiement du modèle et du dashboard. On y trouve notamment :
- Modelisation.ipynb : le notebook pour la modélisation des données.
- deployment.py : le code pour déployer le modèle sous forme d'API.
- dashboard.py : le code du dashboard déployé via `streamlit`.

Vous (ne) pouvez (pas encore) accéder à l'application en cliquant sur le lien ci-dessous :

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://<your-custom-subdomain>.streamlit.app)

Pour le moment, pour faire fonctionner l'application, il faut:

- déployer le modèle en utilisant Ray Serve avec la commande : <br>
`serve run deployment:defaultrisk_pipeline`

- déployer le dashboard en utilisant streamlit avec la commande : <br>
`streamlit run dashboard.py`

Problème : les data sont sur mon compte AWS et je ne sais pas comment les partager pour l'instant...
