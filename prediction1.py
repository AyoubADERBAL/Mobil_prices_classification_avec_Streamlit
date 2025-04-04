import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

import streamlit as st

# Définir un mot de passe (remplace "monmotdepasse" par le tien)
PASSWORD = "monmotdepasse"

# Interface d'authentification
st.title("Application sécurisée 🔐")

password = st.text_input("Entrez le mot de passe :", type="password")

if password == PASSWORD:
    st.success("Accès autorisé ✅")
    # Ajoute ici le reste de ton application
    st.write("Bienvenue dans l'application Streamlit sécurisée !")
else:
    st.error("Mot de passe incorrect ❌")
    st.stop()  # Bloque l'accès au reste de l'application

model = pickle.load(open('model1.pkl','rb'))

st.title("📱 Application de Prédiction de la Gamme de Prix des Téléphones Mobiles
Bienvenue dans cette application interactive basée sur l’intelligence artificielle !
Elle vous permet de prédire la gamme de prix d’un téléphone portable (Low, Medium, High, ou Very High Cost) en fonction de ses caractéristiques techniques.

🔍 Il vous suffit de renseigner les spécifications techniques de votre téléphone (RAM, mémoire interne, appareil photo, batterie, etc.), puis de cliquer sur le bouton "Valider" pour obtenir une estimation de sa catégorie de prix.

Cette application a été réalisée dans le cadre d’un mini-projet de classification en machine learning, à partir d’un jeu de données appelé mobile_prices.csv.
Le modèle a été entraîné, sauvegardé, puis déployé à l’aide de Streamlit afin de rendre l’interface accessible à tous.")

st.markdown("Cette application web simple prédit la gamme de prix de votre téléphone mobile en fonction de ses caractéristiques techniques.")
st.markdown("Les gammes de prix sont définies comme suit : ")
st.markdown(
"""
* Low Cost
* Medium Cost
* High Cost
* Very High Cost
""")

st.markdown("Les données utilisées pour ce projet proviennent de mobile_prices.csv, et l’apprentissage automatique a été utilisé pour prédire les gammes de prix en fonction des données collectées.")



battery_power = st.number_input("Entrez la capacité de la batterie en mAh")
bluetooth = st.selectbox("Votre téléphone dispose-t-il du Bluetooth ?", ("Oui","Non"))
if bluetooth == "Oui":
    blue = 1
else:
    blue = 0

clock_speed = st.number_input("Quelle est la vitesse du microprocesseur ?", value=2.0)
sim = st.selectbox("Votre téléphone prend-il en charge la double SIM ?",("Oui","Non"))
if sim == "Oui":
    dual_sim = 1
else:
    dual_sim = 0

fc = st.number_input("Quel est le nombre de mégapixels de votre caméra frontale ?")
speed = st.selectbox("Votre téléphone est-il compatible 4G ?",("Oui","Non"))
if speed == "Oui":
    four_g = 1
else:
    four_g = 0

int_memory = st.number_input("Quelle est la mémoire interne en Go ?")
m_dep = st.number_input("Quelle est l'épaisseur de votre téléphone en cm ?")

mobile_wt = st.number_input("Quel est le poids de votre téléphone ?")
n_cores = st.number_input("Quel est le nombre de cœurs du processeur ?")
pc = st.number_input("Quelle est la qualité de l’appareil photo principal en mégapixels ?")
px_height = st.number_input("Quelle est la hauteur de la résolution en pixels ?")
px_width = st.number_input("Quelle est la largeur de la résolution en pixels ?")
ram = st.number_input("Quelle est la capacité de la RAM en Mo ?")
sch = st.number_input("Quelle est la hauteur de l'écran en cm ?")
scw = st.number_input("Quelle est la largeur de l'écran en cm ?")
talk_time = st.number_input("Quelle est l'autonomie en conversation de votre téléphone (en heures) ?")
speed_2 = st.selectbox("Votre téléphone est-il compatible 3G ?",("Oui","Non"))
if speed_2 == "Oui":
    three_g = 1
else:
    three_g = 0
ts= st.selectbox("Votre téléphone est-il tactile ?",("Oui","Non"))
if ts == "Oui":
    touch_screen = 1
else:
    touch_screen = 0

w = st.selectbox("Votre téléphone dispose-t-il du Wi-Fi ?",("Oui","Non"))
if w == "Oui":
    wifi = 1
else:
    wifi = 0

# Masquer le pied de page de Streamlit
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

data = [[battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width,ram, sch, scw, talk_time, three_g, touch_screen, wifi]]

result = model.predict(data)

if result[0] == 0:
    result_2 = "Low Cost"

elif result[0] == 1:
    result_2 = "Medium Cost"

elif result [0] == 2:
    result_2 = "* High Cost"

else:
    result_2 = "Very High Cos"

if st.button('Valider'):
    st.markdown(f"Votre téléphone appartient à la gamme de prix : <span style='color: red; font-weight: bold;'>{result_2}</span>", unsafe_allow_html=True)
else:
     st.write('')

