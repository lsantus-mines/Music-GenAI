import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import ollama
import sys
from openai import OpenAI # Importation de la librairie OpenAI

# --- Configuration de la Page (Streamlit) ---
st.title("🎵 Générateur de Noms de Musique")
st.subheader("par IA Générative et Spotify")
st.markdown("Entrez une humeur ou un concept, et l'IA générera des noms de chansons originaux.")

# --- 1. Connexion à l'API Spotify ---
try:
    client_id = st.secrets["SPOTIPY_CLIENT_ID"]
    client_secret = st.secrets["SPOTIPY_CLIENT_SECRET"]
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
except KeyError:
    st.error("ERREUR : Secrets Spotify (SPOTIPY_CLIENT_ID ou SPOTIPY_CLIENT_SECRET) non trouvés.")
    sp = None
except Exception as e:
    st.error(f"Erreur lors de l'initialisation de Spotipy: {e}")
    sp = None

def get_spotify_inspiration(mood):
    """Interroge l'API Spotify pour trouver 5 pistes correspondant à l'humeur."""
    if not sp:
        return "Aucune inspiration Spotify disponible (API non connectée)."
    try:
        results = sp.search(q=mood, limit=5, type='track', market='FR')
        tracks = results['tracks']['items']
        if not tracks:
            return "Aucune piste trouvée sur Spotify pour cette humeur."
        
        inspiration_list = [f"'{t['name']}' par {t['artists'][0]['name']}" for t in tracks]
        return "Inspiré par les chansons existantes : " + ", ".join(inspiration_list)
    except Exception as e:
        st.warning(f"Avertissement (Spotify): {e}")
        return "Impossible de trouver l'inspiration sur Spotify."

# --- 2. Logique GenAI (Hybride) ---

def format_prompt(mood, inspiration, model_type="ollama"):
    """Prépare le prompt pour l'IA."""
    
    system_prompt = "Tu es un producteur de musique créatif. Génère 5 noms de chansons originaux, courts et accrocheurs. Réponds UNIQUEMENT avec la liste des 5 noms, séparés par des nouvelles lignes."
    user_prompt = f"L'humeur est : \"{mood}\". {inspiration}. Génère 5 noms."

    if model_type == "openai":
        # OpenAI préfère les messages séparés
        return system_prompt, user_prompt
    else:
        # Format simple pour Ollama/Llama3
        return f"{system_prompt} {user_prompt}"

# --- Génération Locale ---
def generate_with_ollama(mood, inspiration):
    """Génération via Ollama (local)"""
    try:
        prompt = format_prompt(mood, inspiration, model_type="ollama")
        response = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}],
            options={'temperature': 0.7}
        )
        return response['message']['content']
    except Exception as e:
        st.error(f"Erreur Ollama: {e}. L'application Ollama tourne-t-elle ?")
        return None

# --- Génération Cloud (Stable) ---
def generate_with_openai(mood, inspiration):
    """Génération via OpenAI API (cloud)"""
    try:
        # Initialise le client OpenAI
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        
        # Formate le prompt pour OpenAI
        system_prompt, user_prompt = format_prompt(mood, inspiration, model_type="openai")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            model="gpt-4o-mini", # Modèle rapide, efficace et stable
            temperature=0.7,
            max_tokens=100,
        )
        return chat_completion.choices[0].message.content
            
    except KeyError:
        st.error("Secret OPENAI_API_KEY non trouvé pour le déploiement.")
        return None
    except Exception as e:
        st.error(f"Erreur API OpenAI: {e}")
        return None

# --- 3. Interface Utilisateur (UI) ---

# Détection du mode : Si OPENAI_API_KEY est présent, on est en "cloud".
IS_LOCAL = "OPENAI_API_KEY" not in st.secrets

if IS_LOCAL:
    st.info("Mode local détecté (utilise Ollama / Llama3)")
else:
    st.info("Mode déployé détecté (utilise OpenAI / gpt-4o-mini)")

mood_input = st.text_input(
    "1. Quelle est l'humeur de la chanson ?", 
    placeholder="ex: 'road trip ensoleillé', 'nuit d'orage'"
)

if st.button("Générer les Noms"):
    if not mood_input:
        st.warning("Veuillez entrer une humeur.")
    elif not sp:
        st.error("La connexion à Spotify a échoué. Vérifiez vos secrets.")
    else:
        inspiration = ""
        with st.spinner("Recherche d'inspiration sur Spotify..."):
            inspiration = get_spotify_inspiration(mood_input)
            st.success(f"Inspiration: {inspiration}")
        
        generated_names = None
        if IS_LOCAL:
            with st.spinner("L'IA (Ollama) génère des noms..."):
                generated_names = generate_with_ollama(mood_input, inspiration)
        else:
            with st.spinner("L'IA (OpenAI) génère des noms..."):
                generated_names = generate_with_openai(mood_input, inspiration)
        
        if generated_names:
            st.subheader("✨ Noms de chansons générés :")
            names_list = generated_names.strip().split('\n')
            for name in names_list:
                if name.strip(): # Evite les lignes vides
                    # Enlève les puces ou numéros que l'IA pourrait ajouter
                    clean_name = name.strip().lstrip('*- 12345.').strip()
                    st.markdown(f"* **{clean_name}**")