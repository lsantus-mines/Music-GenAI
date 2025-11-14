# Music-GenAI

Projet: Générateur de Noms de Musique (GenAI + Spotify)

Bienvenue ! Ce document est ton guide principal. Il va te prendre par la main, étape par étape, de zéro jusqu'à avoir ton application qui fonctionne.

1. Concept de l'Application (Rappel)

Nous allons créer un site web simple (avec Streamlit) où :

Tu entres une "humeur" (ex: "triste sous la pluie").

Le code va chercher sur Spotify des chansons qui correspondent à cette humeur (ex: "Hallelujah", "Someone Like You").

Il envoie l'humeur ET ces exemples de chansons à une IA (Llama 3) en lui disant : "Inspire-toi de ça et invente 5 nouveaux noms de chansons".

Le site t'affiche les 5 noms inventés par l'IA.

2. Guide Pas à Pas (Niveau Débutant)

Suis ces étapes dans l'ordre. Ne t'inquiète pas, chaque commande est expliquée.

Étape 1: Mettre en place ton "Quartier Général" (GitHub)

Ce qu'on fait : On crée un dossier sur Internet (un "dépôt" GitHub) pour stocker notre code. C'est la consigne "Utiliser Git".

Crée un compte GitHub : Si ce n'est pas déjà fait, va sur GitHub.com et crée un compte gratuit.

Crée un nouveau dépôt :

Clique sur le "+" en haut à droite, puis "New repository".

Repository name : genai-music-generator (ou un nom que tu aimes).

Description : "Générateur de noms de musique avec GenAI et Spotify."

Public/Private : Choisis "Public".

IMPORTANT : Coche la case "Add a README.md file".

IMPORTANT : Clique sur "Add .gitignore" et choisis "Python" dans la liste.

Clique sur "Create repository".

Copier le projet sur ton ordinateur (Cloner) :

Sur la page de ton nouveau dépôt, clique sur le bouton vert "< > Code".

Copie l'URL (celle qui finit par .git).

Ouvre un Terminal (sur Mac/Linux) ou Git Bash / PowerShell (sur Windows).

Navigue là où tu veux mettre ton projet (ex: cd Documents/Projets) et tape :

git clone [TON_URL_COLLEE_ICI]


Bravo, tu as maintenant un dossier genai-music-generator sur ton PC. Entre dedans :

cd genai-music-generator


C'est dans ce dossier que nous allons travailler.

Étape 2: Préparer ton "Atelier" (Environnement Python)

Ce qu'on fait : On crée une "bulle" (un environnement virtuel) pour ce projet, afin que les outils (librairies) qu'on installe n'entrent pas en conflit avec d'autres projets.

Crée la bulle (venv) :

Assure-toi d'être dans le dossier de ton projet (voir étape 1).

Tape cette commande (elle crée un dossier venv que le .gitignore va ignorer) :

python3 -m venv venv


(Si python3 ne marche pas, essaye python)

Active la bulle :

Sur Mac/Linux :

source venv/bin/activate


Sur Windows (PowerShell) :

.\venv\Scripts\Activate


Tu devrais voir (venv) apparaître au début de ta ligne de commande. La bulle est active ! (Tu devras refaire cette étape à chaque fois que tu ouvres un nouveau terminal pour ce projet).

Étape 3: Installer les "Outils" (Librairies Python)

Ce qu'on fait : On installe les outils (Streamlit, Spotipy, Ollama) dont notre code a besoin.

requirements.txt : C'est le fichier qui liste tous les outils. J'ai déjà créé ce fichier pour toi (voir le fichier requirements.txt à côté).

Installer depuis la liste :

Pendant que ta bulle (venv) est active, tape :

pip install -r requirements.txt


Cela va lire le fichier requirements.txt et tout installer automatiquement.

Étape 4: Installer le "Cerveau" (IA Générative - Ollama)

Ce qu'on fait : On installe l'IA (le LLM) sur ta machine. C'est 100% gratuit et local.

Télécharge Ollama : Va sur Ollama.com et télécharge l'application pour ton système (Mac, Windows, Linux). Installe-la.

Laisse-le tourner : Une fois installé, Ollama tourne en arrière-plan (tu verras une petite icône).

Télécharge le modèle (le cerveau) :

Ouvre ton terminal (pas besoin d'être dans le dossier du projet ou d'activer la bulle pour ça).

Tape cette commande. Elle télécharge le modèle "Llama 3" (environ 5GB, ça peut prendre un peu de temps) :

ollama pull llama3


C'est tout ! L'IA est prête à être appelée par notre code. Laisse juste Ollama tourner en arrière-plan quand tu utilises ton app.

Étape 5: Obtenir les "Clés de la voiture" (API Spotify)

Ce qu'on fait : On demande à Spotify un "Client ID" et un "Client Secret" pour que notre code ait le droit d'utiliser leur API (leur base de données). C'est gratuit.

Va au tableau de bord : Connecte-toi sur Spotify Developer Dashboard.

Crée une "App" :

Clique sur "Create app".

Donne-lui un nom (ex: "GenAI Music") et une description. Coche les cases.

Une fois créée, tu arrives sur la page de ton app.

Copie tes clés :

Tu verras "Client ID". Copie-le.

Clique sur "Client secret" (ou "Show client secret"). Copie-le.

OÙ METTRE CES CLÉS ? (TRÈS IMPORTANT)

NE LES METS JAMAIS DANS TON CODE app.py !

NE LES ENVOIE JAMAIS SUR GITHUB !

Voici la bonne méthode (sécurisée) :

Dans le dossier de ton projet (genai-music-generator), crée un nouveau dossier nommé .streamlit (avec le point au début).

À l'intérieur de ce dossier .streamlit, crée un fichier nommé secrets.toml.

Ouvre secrets.toml et écris-y EXACTEMENT ceci, en remplaçant par tes clés :

# Ce fichier .streamlit/secrets.toml est pour tes clés.
# Il est déjà dans le .gitignore, donc il n'ira pas sur GitHub.

SPOTIPY_CLIENT_ID = "TON_CLIENT_ID_COPIÉ_ICI"
SPOTIPY_CLIENT_SECRET = "TON_CLIENT_SECRET_COPIÉ_ICI"


Streamlit (notre interface) est assez intelligent pour lire ce fichier automatiquement et de manière sécurisée.

Étape 6: Ajouter le Code de l'Application

Ce qu'on fait : On ajoute le fichier app.py (que j'ai généré pour toi) dans notre dossier.

Copie le fichier : Prends le fichier app.py que je t'ai donné.

Colle-le : Mets-le à la racine de ton dossier de projet genai-music-generator (à côté de requirements.txt et du dossier venv).

Étape 7: Lancer l'Application !

Ce qu'on fait : On lance le serveur web local de Streamlit pour voir notre application.

Vérifie :

Tu es dans le dossier genai-music-generator dans ton terminal.

Ta bulle (venv) est active (tu vois (venv)).

Ollama tourne en arrière-plan.

Lance la magie :

streamlit run app.py


Ouvre ton navigateur : Ton terminal va te donner une adresse URL, sûrement http://localhost:8501. Ouvre-la.

Teste ! Écris une humeur, clique sur le bouton, et vois l'IA te générer des noms de chansons !

Étape 8: Sauvegarder ton travail sur GitHub (Commit/Push)

Ce qu'on fait : On envoie notre code (le app.py, le README.md mis à jour, le requirements.txt) sur notre dépôt GitHub.

Arrête ton app : Dans le terminal, appuie sur Ctrl+C pour arrêter le serveur Streamlit.

Ajoute tes changements :

git add .


(Ceci dit à Git : "Regarde tous les nouveaux fichiers et les changements". Il ignorera venv et secrets.toml grâce au .gitignore.)

"Commit" tes changements (Crée un point de sauvegarde) :

git commit -m "feat: Ajout de l'application Streamlit V1 (Spotify + Ollama)"


(Le message -m "..." est une description de ce que tu as fait.)

"Push" tes changements (Envoie-les sur GitHub) :

git push origin main


(Si main ne marche pas, essaye master)

C'EST TERMINÉ ! Tu as maintenant un projet fonctionnel sur ta machine, et le code est sauvegardé sur GitHub, respectant toutes les consignes.
