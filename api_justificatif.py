from flask import Flask, request, jsonify, render_template
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import re

app = Flask(__name__)
UPLOAD_FOLDER = "justificatifs"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Créer le dossier si n'existe pas
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Fonction pour vérifier le type de fichier
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Fonction pour extraire texte depuis image
def extract_text_from_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image, lang='fra')
    return text

# Fonction pour extraire texte depuis PDF
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Fonction d'analyse du texte (motif, date, etc.)
def analyze_text(text):
    motifs_valides = ['maladie', 'hospitalisation', 'urgence', 'entretien', 'administratif']
    date_pattern = r'\d{2}/\d{2}/\d{4}'
    texte_minuscule = text.lower()

    motif = any(m in texte_minuscule for m in motifs_valides)
    date = re.findall(date_pattern, text)
    lisible = len(text.strip()) > 20

    return {
        "motif_valide": motif,
        "date_trouvee": date,
        "lisible": lisible
    }

@app.route('/analyser_justificatif', methods=['POST'])
def analyser_justificatif():
    if 'file' not in request.files:
        return jsonify({"error": "Aucun fichier reçu"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nom de fichier vide"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            texte = extract_text_from_image(file_path)
        elif filename.lower().endswith('pdf'):
            texte = extract_text_from_pdf(file_path)
        else:
            return jsonify({"error": "Type de fichier non pris en charge"}), 400

        resultat = analyze_text(texte)
        return jsonify({"résultat": resultat}), 200
    else:
        return jsonify({"error": "Fichier invalide"}), 400

if __name__ == '__main__':
    app.run(debug=True)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
@app.route('/')
def formulaire():
    return render_template('formulaire_justificatif.html')

