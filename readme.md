🛡️ Brouilleur de Piste - Le Paradoxe de la Confidentialité
<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-3.0-orange)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Downloads](https://img.shields.io/github/downloads/UnAlphaOne/brouilleur-de-piste/total)
![Stars](https://img.shields.io/github/stars/UnAlphaOne/brouilleur-de-piste)

Transformez votre empreinte numérique en brouillard digital infranchissable

Installation •
Fonctionnalités •
Démarrage •
API •
Screenshots •
FAQ
</div>
🎯 Le Concept

    "Si vous ne pouvez pas les battre, noyez-les dans le bruit."

Le Brouilleur de Piste est une IA défensive qui génère un bruit numérique crédible autour de votre activité réelle. Au lieu de simplement bloquer les traceurs (ce qui vous signale comme cible intéressante), cette solution crée des milliers de signaux contradictoires qui rendent votre profil inexploitable.
🔄 Comment ça marche ?
✨ Fonctionnalités
🧠 IA Comportementale Avancée
Fonctionnalité	Description
50+ personas simultanés	Création de profils fictifs ultra-réalistes
Personnalités uniques	Âge, profession, centres d'intérêt, humeurs
IA comportementale	Adaptation des comportements selon le contexte
Heures d'activité réalistes	Simulation de rythmes de vie crédibles
🕵️ Détection de Trackers
Tracker	Type	Contre-mesure
Google Analytics	Analytics	Spoofing de données
Facebook Pixel	Pixel	Génération d'événements factices
DoubleClick	Publicitaire	Clics aléatoires
Amazon Ads	Publicitaire	Simulations d'achat
FingerprintJS	Empreinte	Rotation de fingerprints
🌐 Navigation Humaine

    Mouvements de souris avec courbes de Bézier

    Scroll naturel avec accélération/décélération

    Micro-pauses et temps de réaction humains

    Rotation de fingerprints (viewport, user-agent, etc.)

🛒 Simulations Réalistes

    Achats en ligne sans validation finale

    Génération de cartes valides (algorithme de Luhn)

    Abandon de panier crédible (70% des cas)

    Recherches de produits contextuelles

📱 Réseaux Sociaux

    Création de faux comptes sur 10+ plateformes

    Génération de bios, photos, posts initiaux

    Interactions sociales simulées

    Rotation des identités

📊 Architecture Technique
text

┌─────────────────────────────────────────────────────────┐
│                   Interface Graphique                   │
│                    (CustomTkinter)                      │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────v────────────────────────────────┐
│                    Moteur Principal                     │
├─────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │   Personas   │  │  Navigation  │  │   Trackers   │   │
│  │   Generator  │  │    Engine    │  │   Detector   │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────v────────────────────────────────┐
│                    Base de Données                      │
│                     (SQLite optimisée)                  │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────v────────────────────────────────┐
│                       API REST                          │
│                    (Flask + CORS)                       │
└─────────────────────────────────────────────────────────┘

🚀 Installation
📋 Prérequis

    Python 3.8 ou supérieur

    4GB RAM minimum (8GB recommandé)

    Connexion internet

⚙️ Installation rapide
bash

# 1. Cloner le repository
git clone https://github.com/UnAlphaOne/brouilleur-de-piste.git
cd brouilleur-de-piste

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Installer les navigateurs pour Playwright
playwright install chromium

# 4. Lancer l'application
python brouilleur_piste_v3.py

📦 Dépendances principales
txt

playwright==1.40.0
customtkinter==5.2.1
matplotlib==3.8.0
flask==3.0.0
flask-cors==4.0.0
psutil==5.9.6
numpy==1.24.3
pandas==2.1.3
scipy==1.11.4

🎮 Démarrage rapide
1️⃣ Interface Graphique
python

# Lancement simple
python brouilleur_piste_v3.py

# Configuration personnalisée
python brouilleur_piste_v3.py --config ma_config.json

2️⃣ Configuration de base

Dans l'interface, ajustez :

    Nombre de personas : 5-50 selon votre RAM

    Intensité : 0-100% selon vos besoins

    Fonctionnalités : activez/désactivez selon votre usage

3️⃣ Premier démarrage
bash

# Le programme va :
# - Créer 5 personas initiaux
# - Démarrer la navigation simulée
# - Détecter les trackers
# - Générer des métriques en temps réel

🌐 API REST
📡 Endpoints disponibles
Méthode	Endpoint	Description
GET	/api/v1/status	Statut du brouilleur
GET	/api/v1/metrics/current	Métriques actuelles
GET	/api/v1/metrics/history	Historique (JSON/CSV)
GET	/api/v1/personas	Liste des personas
GET	/api/v1/trackers	Trackers détectés
GET	/api/v1/activities	Activités récentes
POST	/api/v1/config	Modifier configuration
POST	/api/v1/control/start	Démarrer
POST	/api/v1/control/stop	Arrêter
📝 Exemples d'utilisation
bash

# Récupérer les métriques actuelles
curl http://localhost:5000/api/v1/metrics/current

# Exporter en CSV
curl "http://localhost:5000/api/v1/metrics/history?hours=24&format=csv"

# Voir les trackers
curl http://localhost:5000/api/v1/trackers

# Démarrer le brouillage
curl -X POST http://localhost:5000/api/v1/control/start

📊 Exemple de réponse JSON
json

{
  "timestamp": "2026-03-09T10:30:00",
  "personas_active": 12,
  "confusion_score": 78.5,
  "trackers_detected": 145,
  "noise_generated": 1250,
  "cpu_usage": 23.4,
  "memory_usage": 512.8
}

📈 Métriques en temps réel
🎯 KPIs surveillés
Métrique	Description	Objectif
Confusion	Qualité du brouillage	>70%
Personas	Profils actifs	20-50
Bruit	Signaux générés	>1000/h
Trackers	Détections	>100
Achats simulés	Faux paniers	>50
Faux comptes	Identités créées	>20
📊 Graphiques disponibles

    Score de confusion : Évolution sur 24h

    Activité des personas : Distribution horaire

    Trackers par type : Répartition en camembert

    Performances système : CPU/RAM en temps réel

🖼️ Captures d'écran
<div align="center">
Dashboard Principal
text

┌─────────────────────────────────────────────────────┐
│  🎯 78%    👥 23    📊 1452    🕵️ 156    ⚡ 89/min  │
├─────────────────────────────────────────────────────┤
│                                                     │
│           [Graphique de confusion]                  │
│                                                     │
├─────────────────────────────────────────────────────┤
│  Personas Actifs          |  Trackers détectés      │
│  • Julie (32) - Voyage    |  • Google Analytics     │
│  • Pierre (45) - Tech     |  • Facebook Pixel       │
│  • Sophie (28) - Mode     |  • DoubleClick          │
│  • Thomas (51) - Auto     |  • Amazon Ads           │
└─────────────────────────────────────────────────────┘

Configuration
text

┌─────────────────────────────────────────────────────┐
│  ⚙️ CONFIGURATION                                  │
├─────────────────────────────────────────────────────┤
│  Personas:    [████████░░░░] 25/50                  │
│  Intensité:   [███████░░░░░] 70%                    │
│                                                     │
│  ☑ Simulation d'achats                            │
│  ☑ Faux comptes réseaux                           │
│  ☑ Mode caméléon                                  │
│  ☐ Machine Learning (beta)                         │
└─────────────────────────────────────────────────────┘

</div>
🔧 Configuration avancée
📁 Fichier de configuration
json

{
  "max_personas": 50,
  "personas_activity_level": 0.8,
  "enable_purchase_simulation": true,
  "enable_fake_accounts": true,
  "enable_tracker_detection": true,
  "tracker_adaptation_intensity": 0.9,
  "data_retention_days": 90,
  "api_port": 5000,
  "headless": true,
  "user_agent_rotation": true
}

🎛️ Variables d'environnement
bash

# Configuration
export BROUILLEUR_MAX_PERSONAS=50
export BROUILLEUR_API_PORT=5000
export BROUILLEUR_DATA_RETENTION=90

# Lancement
python brouilleur_piste_v3.py

📚 Structure du projet
text

brouilleur-de-piste/
├── brouilleur_piste_v3.py      # Application principale
├── requirements.txt             # Dépendances
├── README.md                    # Documentation
├── config/                      # Configurations
│   ├── default.json
│   └── advanced.json
├── backups/                     # Sauvegardes auto
├── exports/                     # Exports CSV/JSON
├── logs/                        # Fichiers de log
│   └── brouilleur.log
└── docs/                        # Documentation
    ├── API.md
    └── GUIDE.md

🛡️ Sécurité & Éthique
⚠️ Avertissements

    🎯 Usage défensif uniquement : Cet outil est conçu pour protéger votre vie privée

    ⚖️ Conformité légale : Respectez les CGU des sites visités

    🔒 Données personnelles : Aucune donnée réelle n'est collectée

    🌍 Usage responsable : Ne pas utiliser pour des activités illégales

✅ Bonnes pratiques

    Utilisez un VPN en complément

    Limitez le nombre de personas selon votre matériel

    Surveillez les métriques pour ajuster la configuration

    Exportez régulièrement vos données

🤝 Contribution

Les contributions sont les bienvenues !
📋 Processus

    Fork le projet

    Créez votre branche (git checkout -b feature/AmazingFeature)

    Committez vos changements (git commit -m 'Add AmazingFeature')

    Push vers la branche (git push origin feature/AmazingFeature)

    Ouvrez une Pull Request

🎯 Idées d'amélioration

    Support de plus de trackers

    Interface web

    Mode multi-utilisateurs

    Intégration avec des VPN

    Apprentissage automatique des patterns

    Support mobile

📜 License

Distribué sous la licence MIT. Voir LICENSE pour plus d'informations.
📧 Contact

    Auteur : Gérard D UnAlphaOne 

    Projet : https://github.com/UnAlphaOne/brouilleur-de-piste

🌟 Remerciements

    Playwright pour l'automatisation

    CustomTkinter pour l'UI

    Matplotlib pour les graphiques

    Flask pour l'API

<div align="center">

⭐ N'oubliez pas de laisser une étoile si ce projet vous a été utile ! ⭐

⬆ Retour en haut

</div> ```
