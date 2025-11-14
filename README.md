# Music-GenAI

🎵 Générateur de Noms de Musique IA

Ce projet est une application web conçue pour les artistes, musiciens et créateurs. Elle utilise l'IA Générative pour créer des noms de chansons originaux basés sur une humeur, un genre ou un concept fourni par l'utilisateur.

Pour enrichir l'inspiration, l'application se connecte également à l'API Spotify pour analyser des pistes existantes correspondant à l'humeur.

➡️ https://music-genai.streamlit.app

🚀 Concept

L'objectif est de combler le "syndrome de la page blanche" lors de la création musicale.

L'utilisateur entre une humeur (ex: "nuit pluvieuse à Paris", "road trip ensoleillé").

L'application interroge Spotify pour trouver des chansons existantes (ex: 'Nightcall' de Kavinsky) pour servir d'"inspiration".

L'application envoie l'humeur ET l'inspiration à un modèle de langage (IA).

L'IA génère 5 nouveaux noms de chansons originaux et créatifs.

✨ Fonctionnalités

Interface utilisateur simple et réactive créée avec Streamlit.

Inspiration en temps réel via l'API Spotify.

Architecture GenAI Hybride :

Mode Local 💻 : Utilise Ollama (avec llama3) pour une génération 100% gratuite et open-source.

Mode Déployé ☁️ : Utilise l'API OpenAI (gpt-4o-mini) pour une génération stable, rapide et fiable sur le cloud.

Détection automatique du mode (local vs cloud) basée sur la présence des clés API.

🛠️ Choix Techniques et Architecture

Ce projet respecte les consignes en priorisant le local, tout en utilisant une API stable pour le déploiement public.

UI (Front-end) : Streamlit, pour sa simplicité et sa capacité de déploiement rapide sur Streamlit Cloud.

Versionning : Git & GitHub, pour le suivi des versions et la sécurité (avec un .gitignore robuste pour protéger les clés API).

API de Données : Spotify API, pour récupérer des données musicales pertinentes servant d'inspiration.

IA Locale (Priorité n°1) : Ollama (Llama 3). C'est le moteur principal pour le développement local. Il est gratuit, open-source et performant.

IA Cloud (Déploiement) : OpenAI API (GPT-4o mini). Après avoir constaté l'instabilité extrême des API gratuites (Hugging Face, Groq) qui changent leurs modèles sans préavis (erreurs 404, 410, "decommissioned"), le passage à une API payante mais stable était nécessaire pour garantir la fonctionnalité de l'application déployée, conformément au "dernier recours" autorisé par les consignes.

⚙️ Comment l'installer et le lancer localement

Suivez ces étapes pour lancer le projet sur votre propre machine (en mode Ollama).

Prérequis

Python 3.9+

Git

Ollama (et avoir lancé le modèle llama3 au moins une fois)

ollama pull llama3


1. Cloner le Dépôt

Ouvrez votre terminal et clonez ce projet :

git clone [https://github.com/ton-username/ton-repo-name.git](https://github.com/ton-username/ton-repo-name.git)
cd ton-repo-name


2. Créer un Environnement Virtuel

C'est essentiel pour isoler les dépendances de votre projet.

# Créer l'environnement
python3 -m venv venv

# Activer l'environnement
# Sur macOS/Linux:
source venv/bin/activate
# Sur Windows:
.\venv\Scripts\Activate


3. Installer les Dépendances

Installez toutes les librairies nécessaires (Streamlit, Ollama, Spotipy, OpenAI).

pip install -r requirements.txt


4. Configurer vos Clés Secrètes (Secrets)

L'application a besoin de clés API pour fonctionner. Créez un dossier et un fichier pour les stocker localement.

Créez un dossier .streamlit à la racine de votre projet.

Dans ce dossier, créez un fichier nommé secrets.toml.

Ouvrez secrets.toml et collez-y vos clés Spotify (nécessaires pour le mode local) :

# Fichier: .streamlit/secrets.toml
# Requis pour le mode local

SPOTIPY_CLIENT_ID = "VOTRE_CLIENT_ID_SPOTIFY_ICI"
SPOTIPY_CLIENT_SECRET = "VOTRE_CLIENT_SECRET_SPOTIFY_ICI"

# Vous pouvez aussi ajouter votre clé OpenAI ici si vous
# voulez tester le mode OpenAI en local.
# OPENAI_API_KEY = "sk-..."


IMPORTANT : Le fichier .gitignore de ce projet est configuré pour ignorer le dossier .streamlit/, vous ne publierez donc jamais vos clés secrètes sur GitHub.

5. Lancer l'Application

Assurez-vous que votre environnement venv est activé et que votre application Ollama tourne en arrière-plan.

streamlit run app.py


Votre navigateur devrait s'ouvrir automatiquement sur http://localhost:8501.

☁️ Déploiement sur Streamlit Cloud

Cette application est conçue pour un déploiement facile sur Streamlit Cloud.

Faites un "push" de votre code sur un dépôt GitHub.

Connectez votre compte GitHub à Streamlit Cloud.

Pointez Streamlit vers votre dépôt et le fichier app.py.

Dans les Settings > Secrets de l'application Streamlit, ajoutez vos 3 clés (Spotify ID, Spotify Secret, et OPENAI_API_KEY).

L'application détectera la clé OPENAI_API_KEY et basculera automatiquement en mode "OpenAI".

🚧 Limitations

API OpenAI : Le mode déployé utilise gpt-4o-mini. Bien que très bon marché, c'est une API payante.

Ollama : Le mode local nécessite que l'utilisateur ait installé et lancé l'application Ollama, ainsi que le modèle llama3.

Spotify : L'inspiration est limitée à ce que l'API Spotify peut trouver. Des humeurs très abstraites peuvent ne renvoyer aucune chanson.
