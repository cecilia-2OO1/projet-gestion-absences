from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Charger le modèle
model = joblib.load("modele_presence.pkl")

@app.route('/')
def accueil():
    return "API de prédiction de présence opérationnelle !"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données du formulaire (POST HTML classique)
        retard = float(request.form['retard'])
        justificatif = int(request.form['justificatif'])
        distance_domicile = float(request.form['distance_domicile'])
        connecte_wifi = int(request.form['connecte_wifi'])
        nb_notifications = int(request.form['nb_notifications'])

        # Préparer les données pour la prédiction
        data = np.array([[retard, justificatif, distance_domicile, connecte_wifi, nb_notifications]])
        prediction = model.predict(data)

        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
