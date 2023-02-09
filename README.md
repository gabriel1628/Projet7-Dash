# Projet 7 - Parcours Data Scientist (OpenClassrooms)

Ce repo est une alternative au repo de base dédié au [projet 7](https://github.com/gabriel1628/Projet-7) qui utilise
`streamlit` pour déployer le dashboard. Dans ce repo, nous utiliserons `Dash`.

Si le modèle n'est plus disponible sous forme d'API, vous pouvez le déployer vous-même en suivant les explications dans
[ce repo](https://github.com/gabriel1628/Projet-7).

Pour déployer le dashboard en __local__, il suffit de lancer le script ``dashboard.py``.

Pour le déployer sur le __cloud__, il y a plusieurs possibilités :
- Avec [Pythonanywhere](https://www.pythonanywhere.com/) (vous pouvez suivre le tutoriel sur [ce lien](https://www.youtube.com/watch?v=WOWVat5BgM4))
- Avec [Render](https://render.com). Il y a également [un tutoriel]() sur youtube.
Cependant, je vous conseille de choisir __Docker__ dans l'onglet __Environment__
au moment de déployer l'application et le fichier ``Dockerfile`` sera utilisé pour le déploiement. Lorsque j'ai essayé
avec Python ça n'a pas fonctionné, je pense parce que Render utilisait la version 3.7, or j'ai utilisé la version 3.9
pour mes programmes.