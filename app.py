import streamlit as st
import pandas as pd
import os

# --- LOGO ---
logo_path = os.path.join(os.path.dirname(__file__), "sfr_logo.png")
st.sidebar.image(logo_path, width=140)

# --- NAVIGATION ---
st.sidebar.title("📡 Navigation")

page = st.sidebar.radio("Aller à :", [
    "🏁 Accueil",
    "📊 Exploration réseau",
    "🚨 Détection d'anomalies",
    "📈 Indicateurs avancés",
    "📍 Zones sensibles",
    "📄 Recommandations"
])

st.sidebar.markdown("---")
st.sidebar.markdown("👨‍💻 Réalisé par : **Marvin KADA-SEDODE**")
st.sidebar.markdown("📍 Data Scientist – Crédit Agricole")
st.sidebar.markdown("✉️ marvin.mail@exemple.com")

# --- ACCUEIL ---
if page == "🏁 Accueil":
    st.title("Challenge Nexialog x SFR – Application Anomalies Réseau")
    st.markdown("""
    Cette application vise à **identifier** et **caractériser** les anomalies de performance sur le réseau fixe **SFR**, 
    en combinant **modélisation non supervisée**, visualisations temporelles et indicateurs décisionnels.
    
    📌 **Objectif** : Prioriser les interventions réseau, anticiper les zones à risque et améliorer la qualité de service.
    """)
    st.subheader("📦 Données utilisées")
    st.markdown("Tests réseau SFR entre décembre et janvier : latence, score, nb clients, PEAG, OLT, etc.")
    st.markdown("---")
    st.success("💡 *« L'innovation, ce n'est pas une option. C'est une exigence pour garantir la performance réseau. »*")

# --- EXPLORATION ---
elif page == "📊 Exploration réseau":
    st.title("Exploration du réseau")
    st.markdown("Visualisation de la latence, stabilité, effet horaire...")

# --- ANOMALIES ---
elif page == "🚨 Détection d'anomalies":
    st.title("Détection d'anomalies")
    st.markdown("Isolation Forest appliqué à PEAG / OLT")

# --- INDICATEURS ---
elif page == "📈 Indicateurs avancés":
    st.title("Indicateurs de stabilité réseau")
    st.markdown("PHLR, rolling slope, instabilité, etc.")
    st.info("🧮 Exemples d'indicateurs à valeur ajoutée :\n"
            "- **PHLR** (Peak Hour Latency Ratio)\n"
            "- **Separation Score** (ratio pointe/creuse, utile pour repérer l'effet heure)\n"
            "- **Coefficient de variation** : std / moyenne\n"
            "- **Indice d’asymétrie** (Skewness) : pour la forme de distribution")

# --- ZONES SENSIBLES ---
elif page == "📍 Zones sensibles":
    st.title("Priorisation des zones critiques")
    st.markdown("Top PEAG/OLT sensibles avec forte instabilité ou latence anormale")

# --- RECOMMANDATIONS ---
elif page == "📄 Recommandations":
    st.title("📄 Recommandations Stratégiques")
    st.markdown("""
    **🔄 Monitoring récurrent** :
    - Mettre en place un tableau de bord automatique (Streamlit / PowerBI)
    - Rafraîchissement quotidien ou hebdomadaire

    **🌍 Extension géographique** :
    - Analyser les zones sous-performantes (PHLR > 1.5)
    - Cibler les PEAG à forte densité client

    **💪 Actions prioritaires** :
    - Intervention ciblée sur les 10 PEAG les plus instables
    - Validation par terrain / techniciens

    **✨ Prochaines étapes** :
    - Ajouter les scores NPS clients en aval
    - Coupler avec des données climat / travaux / réclamations
    """)
    st.success("🚀 Cette section est essentielle pour montrer votre compréhension métier à SFR.")

# --- STYLE ---
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

# --- DUMMY DATA ---
@st.cache_data
def load_data():
    return pd.DataFrame()

data = load_data()
