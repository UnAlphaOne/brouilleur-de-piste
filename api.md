📚 Documentation API - Brouilleur de Piste v3.0
🌐 Vue d'ensemble

L'API REST du Brouilleur de Piste permet d'interagir avec le système de manière programmatique. Elle expose toutes les fonctionnalités via des endpoints JSON.

Base URL: http://localhost:5000/api/v1
🔐 Authentification

Actuellement, l'API fonctionne sans authentification. Pour la production, activez l'API key dans la configuration.
python

# Activation de l'API key
config.api_key_required = True
config.api_key = "votre-cle-secrete"

📡 Endpoints
1. 🟢 Statut du système
GET /status

Retourne l'état actuel du brouilleur.

Réponse:
json

{
  "running": true,
  "uptime": "2:30:45",
  "personas": 23,
  "actions": 1542,
  "success_rate": "94.2%",
  "trackers": 156,
  "confusion_score": 78.5
}

2. 📊 Métriques
GET /metrics/current

Métriques en temps réel.

Réponse:
json

{
  "timestamp": "2026-03-09T10:30:00",
  "personas_active": 18,
  "personas_total": 23,
  "confusion_score": 78.5,
  "noise_generated": 1250,
  "trackers_detected": 156,
  "trackers_by_type": {
    "analytics": 89,
    "advertising": 42,
    "social": 18,
    "fingerprint": 7
  },
  "purchases_simulated": 34,
  "fake_accounts_created": 12,
  "cpu_usage": 23.4,
  "memory_usage": 512.8,
  "actions_per_minute": 8.2,
  "success_rate": 0.94
}

GET /metrics/history

Historique des métriques.

Paramètres:
Nom	Type	Description	Défaut
hours	int	Période en heures	24
format	string	json ou csv	json

Exemple: GET /metrics/history?hours=48&format=csv
3. 👥 Personas
GET /personas

Liste tous les personas.

Paramètres:
Nom	Type	Description
active_only	boolean	Uniquement les actifs

Réponse:
json

[
  {
    "id": "a1b2c3d4",
    "name": "Julie Martin",
    "age": 32,
    "gender": "female",
    "location": "Paris",
    "occupation": "Architecte",
    "interests": ["voyage", "photographie", "randonnée"],
    "mood": "curious",
    "consistency_score": 0.87,
    "tech_savviness": 0.65,
    "total_activities": 234,
    "last_active": "2026-03-09T09:15:23"
  }
]

GET /personas/{id}

Détails d'un persona spécifique.

Réponse:
json

{
  "id": "a1b2c3d4",
  "name": "Julie Martin",
  "age": 32,
  "gender": "female",
  "location": "Paris",
  "occupation": "Architecte",
  "interests": ["voyage", "photographie", "randonnée"],
  "dislikes": ["publicité", "réseaux sociaux"],
  "behaviors": {
    "browsing_speed": 1.2,
    "active_hours": {"start": 8, "end": 22},
    "device_preference": "mobile"
  },
  "mood": "curious",
  "consistency_score": 0.87,
  "intelligence_level": 0.72,
  "paranoia_level": 0.45,
  "tech_savviness": 0.65,
  "spending_habit": "average",
  "social_media_presence": {
    "facebook": true,
    "twitter": false,
    "instagram": true
  },
  "total_activities": 234,
  "success_rate": 0.96,
  "recent_activities": [
    {
      "timestamp": "2026-03-09T09:15:23",
      "activity_type": "browse",
      "site": "lemonde.fr",
      "duration": 145
    }
  ]
}

4. 🕵️ Trackers
GET /trackers

Liste des trackers détectés.

Réponse:
json

[
  {
    "name": "Google Analytics",
    "domain": "google-analytics.com",
    "type": "analytics",
    "detection_count": 342,
    "first_seen": "2026-03-08T10:23:15",
    "last_seen": "2026-03-09T10:15:22",
    "sites_found": ["lemonde.fr", "amazon.fr"]
  }
]

GET /trackers/stats

Statistiques globales des trackers.

Réponse:
json

{
  "by_type": {
    "analytics": 89,
    "advertising": 42,
    "social": 18,
    "fingerprint": 7
  },
  "total": 156,
  "most_detected": "Google Analytics",
  "new_today": 12
}

5. 📝 Activités
GET /activities

Flux des activités récentes.

Paramètres:
Nom	Type	Description	Défaut
limit	int	Nombre d'activités	100

Réponse:
json

[
  {
    "timestamp": "2026-03-09T10:28:15",
    "persona_name": "Julie Martin",
    "persona_id": "a1b2c3d4",
    "activity_type": "browse",
    "site": "amazon.fr",
    "duration": 234,
    "success": true
  }
]

6. 🛒 Achats simulés
GET /purchases

Liste des achats simulés.

Réponse:
json

[
  {
    "id": "p123",
    "persona_id": "a1b2c3d4",
    "product_name": "iPhone 15",
    "product_category": "electronics",
    "price": 1299.99,
    "site": "amazon.fr",
    "cart_value": 1299.99,
    "abandoned": true,
    "timestamp": "2026-03-09T09:45:12"
  }
]

7. 📱 Faux comptes
GET /accounts/fake

Liste des faux comptes créés.

Réponse:
json

[
  {
    "platform": "twitter",
    "username": "julie_martin_32",
    "email": "julie.martin.temp@mail.com",
    "posts_count": 23,
    "followers_count": 45,
    "created_at": "2026-03-08T14:23:11",
    "status": "active"
  }
]

8. ⚙️ Configuration
GET /config

Récupère la configuration actuelle.
POST /config

Met à jour la configuration.

Body:
json

{
  "max_personas": 50,
  "personas_activity_level": 0.8,
  "enable_purchase_simulation": true,
  "tracker_adaptation_intensity": 0.9
}

9. 🎮 Contrôle
POST /control/start

Démarre le brouillage.
POST /control/stop

Arrête le brouillage.
POST /control/reset

Réinitialise le système.
10. 📤 Export
GET /export/{format}

Exporte les données.

Paramètres:
Nom	Type	Description
type	string	all, metrics, personas, activities

Formats supportés: json, csv

Exemple: GET /export/csv?type=metrics
📊 Exemples d'intégration
Python
python

import requests
import json

BASE_URL = "http://localhost:5000/api/v1"

# Récupérer les métriques
response = requests.get(f"{BASE_URL}/metrics/current")
metrics = response.json()
print(f"Score de confusion: {metrics['confusion_score']}%")

# Démarrer le brouillage
requests.post(f"{BASE_URL}/control/start")

# Modifier la configuration
config = {
    "max_personas": 30,
    "enable_purchase_simulation": False
}
requests.post(f"{BASE_URL}/config", json=config)

JavaScript
javascript

const BASE_URL = 'http://localhost:5000/api/v1';

// Récupérer les personas
fetch(`${BASE_URL}/personas?active_only=true`)
  .then(response => response.json())
  .then(personas => {
    console.log(`${personas.length} personas actifs`);
  });

// Exporter en CSV
window.location.href = `${BASE_URL}/export/csv?type=metrics&hours=48`;

cURL
bash

# Métriques actuelles
curl http://localhost:5000/api/v1/metrics/current

# Démarrer
curl -X POST http://localhost:5000/api/v1/control/start

# Configuration
curl -X POST http://localhost:5000/api/v1/config \
  -H "Content-Type: application/json" \
  -d '{"max_personas": 40}'

⚡ Rate Limiting

Par défaut: 100 requêtes par minute par IP

Headers de rate limiting:
text

X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1615372842

🚨 Codes d'erreur
Code	Description
400	Requête invalide
401	Non authentifié
403	Accès interdit
404	Ressource non trouvée
429	Trop de requêtes
500	Erreur serveur

Exemple d'erreur:
json

{
  "error": "Persona not found",
  "code": 404,
  "timestamp": "2026-03-09T10:30:00"
}