📘 GUIDE D'UTILISATION - Brouilleur de Piste v3.0
📑 Table des matières

    Introduction

    Installation

    Premiers pas

    Interface utilisateur

    Configuration

    Dépannage

    FAQ

🎯 Introduction

Le Brouilleur de Piste est un outil de protection de la vie privée qui génère un bruit numérique crédible autour de votre activité réelle, rendant votre profil inexploitable par les algorithmes de tracking.
🔍 Pourquoi l'utiliser ?

    🛡️ Protéger votre vie privée en ligne

    🎯 Rendre votre profil inexploitable

    🤖 Contrer les algorithmes de profilage

    🌐 Reprendre le contrôle de vos données

💻 Installation
📋 Prérequis système

    OS: Windows 10/11, macOS 12+, Linux (Ubuntu 20.04+)

    RAM: 4GB minimum (8GB recommandé)

    Espace: 500MB

    Python: 3.8 ou supérieur

⚙️ Installation pas à pas
Windows
bash

# 1. Installer Python depuis python.org
# 2. Ouvrir PowerShell en administrateur
# 3. Installer les dépendances
pip install playwright customtkinter matplotlib flask psutil numpy pandas scipy flask-cors
playwright install chromium

# 4. Télécharger le projet
git clone https://github.com/UnAlphaOne/brouilleur-de-piste.git
cd brouilleur-de-piste

# 5. Lancer
python brouilleur_piste_v3.py

macOS/Linux
bash

# 1. Installer Python
brew install python3  # macOS
sudo apt install python3 python3-pip  # Ubuntu

# 2. Installer les dépendances
pip3 install playwright customtkinter matplotlib flask psutil numpy pandas scipy flask-cors
playwright install chromium

# 3. Lancer
python3 brouilleur_piste_v3.py

🚀 Premiers pas
1️⃣ Lancement initial
bash

python brouilleur_piste_v3.py

2️⃣ Configuration rapide

Dans l'interface, réglez :

    Personas: 10-20 pour commencer

    Intensité: 50% pour tester

    Activez: toutes les fonctionnalités

3️⃣ Démarrage

Cliquez sur 🚀 DÉMARRER et observez :
text

✅ Persona créé: Julie Martin (32 ans, Architecte)
✅ Persona créé: Pierre Dubois (45 ans, Ingénieur)
✅ Persona créé: Sophie Bernard (28 ans, Designer)
✅ Brouilleur démarré avec 3 personas

4️⃣ Surveillance

Le dashboard affiche en temps réel :

    Score de confusion

    Nombre de personas actifs

    Trackers détectés

    Performances système


📑 Onglets disponibles
Onglet	Description
Dashboard	Vue d'ensemble avec KPIs
Métriques	Historique détaillé
Personas	Liste et détails des profils
Trackers	Statistiques et liste des trackers
Activités	Flux en temps réel
Logs	Messages système
⚙️ Configuration
📁 Fichiers de configuration

Les fichiers de configuration sont créés automatiquement dans :

    Windows: %APPDATA%\BrouilleurPiste\

    macOS/Linux: ~/.config/brouilleur-piste/

📝 Configuration manuelle

Créez config/default.json :
json

{
  "max_personas": 30,
  "personas_activity_level": 0.7,
  "enable_purchase_simulation": true,
  "enable_fake_accounts": true,
  "enable_tracker_detection": true,
  "tracker_adaptation_intensity": 0.8,
  "data_retention_days": 30,
  "headless": true,
  "user_agent_rotation": true,
  "api_port": 5000
}

🎛️ Configuration avancée

Créez config/advanced.json :
json

{
  "min_personas": 5,
  "max_personas": 100,
  "personas_creation_rate": 2,
  "personas_consistency_min": 0.6,
  "personas_consistency_max": 0.98,
  "navigation_timeout": 30000,
  "min_delay_between_actions": 0.3,
  "max_delay_between_actions": 8.0,
  "mouse_movement_curve": true,
  "scroll_behavior": "natural",
  "proxy_rotation_frequency": 300,
  "fingerprint_rotation": true,
  "purchase_frequency": 15,
  "account_creation_frequency": 60,
  "social_activity_frequency": 10,
  "noise_intensity": 0.9,
  "confusion_intensity": 0.85,
  "data_retention_days": 90,
  "backup_interval_hours": 12,
  "api_rate_limit": 200,
  "strategies": [
    "profile_pollution",
    "search_noise",
    "click_farming",
    "purchase_simulation",
    "tracker_poisoning"
  ]
}

🔧 Dépannage
❌ Problèmes courants
1. Rien ne s'affiche dans l'onglet Trackers

Cause: La base de données est vide ou les requêtes échouent

Solution:
python

# Vérifiez manuellement
import sqlite3
conn = sqlite3.connect('brouilleur_v3.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM trackers')
print(f"Trackers en base: {cursor.fetchone()[0]}")

2. Rien ne s'affiche dans l'onglet Activités

Cause: Aucune activité enregistrée

Solution:

    Vérifiez que le brouillage est bien démarré

    Attendez quelques minutes que des activités se génèrent

    Vérifiez les logs pour les erreurs

3. Erreur "no such column: tracker_name"

Cause: Ancien schéma de base de données

Solution:
bash

# Supprimez l'ancienne base
rm brouilleur_v3.db
# Relancez l'application
python brouilleur_piste_v3.py

4. L'API ne répond pas

Cause: Port déjà utilisé

Solution:
bash

# Changez le port dans la config
"api_port": 5001
# Ou tuez le processus sur le port 5000
netstat -ano | findstr :5000  # Windows
taskkill /PID <PID> /F

❓ FAQ
Q1: Combien de personas puis-je exécuter ?

R: Cela dépend de votre RAM :

    4GB RAM: 10-15 personas

    8GB RAM: 25-30 personas

    16GB RAM: 50+ personas

Q2: Est-ce que ça consomme beaucoup de bande passante ?

R: Environ 50-100 MB par heure selon le nombre de personas. Chaque persona génère du trafic web simulé.
Q3: Mes données personnelles sont-elles en danger ?

R: Non, le système ne collecte aucune donnée personnelle réelle. Toutes les données générées sont fictives.
Q4: Puis-je utiliser un VPN avec le brouilleur ?

R: Oui, c'est même recommandé ! Le brouilleur fonctionne parfaitement avec un VPN actif.
Q5: Pourquoi les onglets Trackers et Activités sont vides ?

R: Plusieurs causes possibles :

    Le brouillage n'est pas démarré

    Pas assez de temps écoulé (attendez 5-10 minutes)

    Problème de base de données (voir Dépannage)

Q6: Comment voir les trackers en temps réel ?

R: Utilisez l'API :
bash

curl http://localhost:5000/api/v1/trackers

Q7: Puis-je exporter les données ?

R: Oui, via l'interface (bouton "Exporter") ou l'API :
bash

curl http://localhost:5000/api/v1/export/csv?type=all

Q8: Les sites peuvent-ils détecter le brouilleur ?

R: Le système utilise des techniques avancées pour éviter la détection :

    Rotation des user-agents

    Mouvements de souris naturels

    Délais humains

    Cookies simulés

Q9: Comment arrêter proprement ?

R: Cliquez sur "ARRÊTER" dans l'interface ou utilisez l'API :
bash

curl -X POST http://localhost:5000/api/v1/control/stop

Q10: Le score de confusion est bas, que faire ?

R: Augmentez :

    Le nombre de personas

    L'intensité du brouillage

    Activez plus de fonctionnalités

    Laissez tourner plus longtemps

📊 Optimisation des performances
🚀 Pour de meilleures performances

    Montez le nombre de personas progressivement

    Utilisez le mode headless (pas d'interface graphique)

    Activez la rotation des fingerprints

    Nettoyez régulièrement les anciennes données

📈 Monitoring avancé
python

# Script de monitoring personnalisé
import requests
import time

while True:
    metrics = requests.get('http://localhost:5000/api/v1/metrics/current').json()
    print(f"Confusion: {metrics['confusion_score']}% | Personas: {metrics['personas_active']}")
    time.sleep(60)

🆘 Support
📧 Contact

    Issues GitHub: https://github.com/votre-nom/brouilleur-de-piste/issues


📚 Ressources

    Documentation API

    Guide utilisateur


<div align="center">

🌟 Si ce projet vous aide, n'hésitez pas à lui donner une étoile ! 🌟

⬆ Retour en haut
</div> ```