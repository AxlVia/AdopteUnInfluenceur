# Définir le chemin pour les templates
import flask
import os
from flask import Flask, render_template, jsonify, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
import googleapiclient.discovery
import atexit

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))

# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'AIzaSyB3NzYu0ytU7SOVHvJ0tJEcsAkt7fhMZlI'

# Variable pour stocker les données YouTube
youtube_data = []

# Fonction pour récupérer les données YouTube
def fetch_youtube_data(query="conversation téléphonique"):
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
    request = youtube.search().list(
        part="snippet",
        type='video',
        q=query,
        videoDuration='short',
        videoDefinition='high',
        maxResults=10
    )
    response = request.execute()
    return response.get('items', [])

# Logique pour charger les données YouTube au démarrage du serveur
youtube_data = fetch_youtube_data()

# Planificateur de tâches pour mettre à jour les données tous les jours à 6h
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_youtube_data, 'cron', hour=6)
scheduler.start()

# Enregistrement de la fonction d'arrêt pour le planificateur
atexit.register(lambda: scheduler.shutdown())

# Point de terminaison de l'API pour obtenir les données YouTube
@app.route('/api/youtube-data', methods=['GET'])
def get_youtube_data():
    return jsonify(youtube_data)

# Gérer la page d'accueil "/"
@app.route('/', endpoint='home')
def home():
    return render_template('index.html', youtube_data=youtube_data)

# Point de terminaison pour mettre à jour les données YouTube avec une nouvelle valeur de q
@app.route('/update-data/<query>', methods=['GET'])
def update_data(query):
    update_youtube_data(query)
    return redirect(url_for('home'))

# Fonction pour mettre à jour les données YouTube avec une nouvelle valeur de q
def update_youtube_data(query):
    global youtube_data
    youtube_data = fetch_youtube_data(query)

if __name__ == '__main__':
    app.run(debug=True)