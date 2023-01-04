# Projet-7

Pour utiliser l'application déployée sur le cloud utiliser la branche __main__, pour déployer l'application en
locale, utiliser la branche __local__.

Ce repo contient des livrables du projet 7 de la formation Data Scientist chez OpenClassrooms.
On peut y trouver les codes pour le déploiement du modèle et du dashboard. On y trouve notamment :
- Modelisation.ipynb : le notebook pour la modélisation des données.
- deployment.py : le code pour déployer le modèle sous forme d'API.
- dashboard.py : le code du dashboard déployé via `streamlit`.

Vous pouvez accéder à l'application en cliquant sur le lien ci-dessous :

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gabriel1628-projet-7-dashboard-umy46h.streamlit.app)

Pour le déploiement en local (branche __local__) :

- déployer le modèle en utilisant Ray Serve avec la commande : <br>
`serve run deployment:defaultrisk_pipeline`

- déployer le dashboard en utilisant streamlit avec la commande : <br>
`streamlit run dashboard.py`
