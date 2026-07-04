import json
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def load_translations(lang):
    # JSON files ko load karne ka function
    file_path = os.path.join(app.root_path, 'translations', f'{lang}.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/lang/<lang_code>")
def get_language(lang_code):
    try:
        data = load_translations(lang_code)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": "Language file not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)