from flask import Flask
app = Flask(__name__)

# chemin de base / exécute la fonction home()
@app.route('/')
def home():
    return "Hello, World!"

# Création d'une page supplémentaire localhost:5000/about
@app.route("/about")
def about():
    return "This is an about page."
