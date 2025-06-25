# projet-gestion-absences
# 🧠 Projet de gestion des absences - Data & API

Ce projet propose une solution de détection d’anomalies dans les absences étudiantes à l’aide du **Machine Learning**, d’une **API Flask** et de **dashboards Power BI**.

## 🎯 Objectifs
- Prédire la présence ou l'absence d’un étudiant à l’aide d’un modèle ML (fichier `.pkl`)
- Intégrer une API Flask pour faire des prédictions en temps réel
- Visualiser les données via des dashboards Power BI
- Automatiser le traitement de justificatifs

## 🧩 Technologies utilisées
- Python (Flask, Pandas, NumPy, Scikit-learn)
- Power BI pour la data visualisation
- Jupyter Notebook pour l’analyse et l’entraînement
- GitHub pour le versioning
- HTML (formulaire justificatif)

## 🔍 Structure du projet
- `api_ml_presence.py` : API Flask avec le modèle de prédiction
- `modele_presence.pkl` : modèle ML entraîné
- `ProjetData1.ipynb` : traitement, entraînement, évaluation du modèle
- `formulaire_justificatif.html` : exemple de formulaire HTML
- `justificatifs/` : exemples de documents traités
- `powerbi/` : captures ou fichiers `.pbix` du dashboard

## 📊 Dashboard Power BI
Le rapport Power BI met en évidence :
- Les absences justifiées / non justifiées
- Les retards fréquents
- Les étudiants à risque (prédiction ML)
*(Voir dossier `powerbi/`)*

## 🚀 Pour exécuter l’API Flask
```bash
pip install -r requirements.txt
python api_ml_presence.py
