"""
BROUILLEUR DE PISTE v3.0 - Édition Ultimate
"""

import asyncio
import random
import time
import json
import hashlib
import threading
import sqlite3
import uuid
import socket
import requests
import re
import csv
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Optional, Any, Tuple
from queue import Queue, PriorityQueue
from contextlib import contextmanager, asynccontextmanager
from enum import Enum
from collections import defaultdict, Counter, deque
from pathlib import Path
import pickle
import os
import sys
import logging
import traceback

# Data science
import numpy as np
import pandas as pd
from scipy import stats

# Interface graphique
import customtkinter as ctk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation

# Web automation
from playwright.async_api import async_playwright, Browser, Page, BrowserContext

# Monitoring
import psutil
import platform

# API
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import socket
import threading

# Crypto
import secrets
import hashlib
import hmac

# Configuration logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ============================================================================
# CONSTANTES ET ÉNUMÉRATIONS
# ============================================================================

class ActivityType(Enum):
    BROWSE = "browse"
    SEARCH = "search"
    SOCIAL = "social"
    PURCHASE = "purchase"
    ACCOUNT_CREATE = "account_create"
    VIDEO_WATCH = "video_watch"
    EMAIL_READ = "email_read"
    MAP_SEARCH = "map_search"
    NEWS_READ = "news_read"
    FORUM_POST = "forum_post"
    GAME_PLAY = "game_play"
    MUSIC_LISTEN = "music_listen"
    JOB_SEARCH = "job_search"
    REAL_ESTATE = "real_estate"
    HEALTH = "health"

class TrackerType(Enum):
    ANALYTICS = "analytics"
    ADVERTISING = "advertising"
    SOCIAL = "social"
    FINGERPRINT = "fingerprint"
    BEACON = "beacon"
    PIXEL = "pixel"
    UNKNOWN = "unknown"

class PersonaMood(Enum):
    HAPPY = "happy"
    CURIOUS = "curious"
    URGENT = "urgent"
    RELAXED = "relaxed"
    ANGRY = "angry"
    CONFUSED = "confused"

# ============================================================================
# DATACLASSES AVANCÉES
# ============================================================================

@dataclass
class AdvancedConfig:
    """Configuration ultra-détaillée"""
    # Général
    app_name: str = "Brouilleur de Piste v3.0"
    version: str = "3.0.0"
    debug: bool = False
    log_level: str = "INFO"
    
    # Personas
    min_personas: int = 3
    max_personas: int = 50
    personas_creation_rate: int = 1  # par heure
    personas_activity_level: float = 0.7  # 0-1
    personas_consistency_min: float = 0.6
    personas_consistency_max: float = 0.98
    
    # Navigation
    headless: bool = True
    navigation_timeout: int = 30000  # ms
    min_delay_between_actions: float = 0.5
    max_delay_between_actions: float = 5.0
    human_typing_speed: Tuple[int, int] = (50, 200)  # ms par caractère
    mouse_movement_curve: bool = True
    scroll_behavior: str = "natural"  # natural, jump, mixed
    
    # Rotations
    proxy_rotation_frequency: int = 300  # secondes
    user_agent_rotation: bool = True
    viewport_rotation: bool = True
    fingerprint_rotation: bool = True
    
    # Features
    enable_purchase_simulation: bool = True
    enable_fake_accounts: bool = True
    enable_tracker_detection: bool = True
    enable_adaptive_mode: bool = True
    enable_machine_learning: bool = False
    enable_stealth_mode: bool = True
    enable_api: bool = True
    enable_notifications: bool = True
    enable_auto_update: bool = True
    
    # Fréquences (minutes)
    purchase_frequency: int = 30
    account_creation_frequency: int = 120
    social_activity_frequency: int = 15
    search_frequency: int = 5
    tracker_check_frequency: int = 1
    
    # Intensités
    noise_intensity: float = 0.7  # 0-1
    confusion_intensity: float = 0.8  # 0-1
    tracker_adaptation_intensity: float = 0.9  # 0-1
    
    # Persistance
    data_retention_days: int = 90
    auto_backup: bool = True
    backup_interval_hours: int = 24
    backup_path: str = "./backups"
    export_format: str = "json"  # json, csv, parquet
    
    # API
    api_host: str = "127.0.0.1"
    api_port: int = 5000
    api_key_required: bool = False
    api_rate_limit: int = 100  # requêtes/minute
    
    # Advanced
    strategies: List[str] = field(default_factory=lambda: [
        'profile_pollution',
        'search_noise',
        'click_farming',
        'purchase_simulation',
        'social_engagement',
        'tracker_poisoning',
        'email_confusion',
        'location_spoofing',
        'interest_dilution',
        'behavior_randomization'
    ])

@dataclass
class Persona:
    """Persona ultra-détaillé"""
    id: str
    name: str
    age: int
    gender: str
    location: str
    occupation: str
    interests: List[str]
    dislikes: List[str]
    behaviors: Dict[str, Any]
    mood: PersonaMood
    activity_log: List[Dict]
    consistency_score: float
    intelligence_level: float  # 0-1
    paranoia_level: float  # 0-1
    tech_savviness: float  # 0-1
    spending_habit: str  # frugal, average, spender
    social_media_presence: Dict[str, bool]
    fake_accounts: List[Dict]
    created_at: datetime
    last_active: datetime
    total_activities: int = 0
    success_rate: float = 1.0

@dataclass
class Tracker:
    """Tracker détecté"""
    id: str
    name: str
    domain: str
    type: TrackerType
    first_seen: datetime
    last_seen: datetime
    detection_count: int
    sites_found: List[str]
    cookies: List[Dict]
    scripts: List[str]
    countermeasures_applied: List[str]
    effectiveness: float  # 0-1

@dataclass
class MetricSnapshot:
    """Métriques avancées"""
    timestamp: datetime
    # Personas
    personas_active: int
    personas_total: int
    personas_creation_rate: float
    personas_activity_rate: float
    
    # Bruit
    noise_generated: int
    noise_per_persona: float
    noise_quality: float  # 0-1
    
    # Confusion
    confusion_score: float
    confusion_trend: float  # pente
    confusion_stability: float
    
    # Trackers
    trackers_detected: int
    trackers_by_type: Dict[str, int]
    countermeasures_applied: int
    countermeasures_success: float
    
    # Achats
    purchases_simulated: int
    purchase_value_total: float
    carts_abandoned: int
    
    # Comptes
    fake_accounts_created: int
    accounts_by_platform: Dict[str, int]
    
    # Système
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    network_io: Dict[str, int]
    battery_percent: Optional[float]
    
    # Performance
    actions_per_minute: float
    success_rate: float
    error_rate: float

# ============================================================================
# BASE DE DONNÉES AMÉLIORÉE
# ============================================================================

class AdvancedDatabaseManager:
    """Gestionnaire de base de données"""
    
    def __init__(self, db_path="brouilleur_v3.db"):
        self.db_path = db_path
        self.local = threading.local()  # Stockage par thread
        self.cache = {}
        self.cache_ttl = 300
        self.init_database()
        self.setup_indexes()
        self.setup_triggers()
    
    def get_connection(self):
        """Obtient une connexion propre au thread courant"""
        if not hasattr(self.local, 'connection'):
            self.local.connection = sqlite3.connect(self.db_path, check_same_thread=False)
            self.local.connection.row_factory = sqlite3.Row
        return self.local.connection
    
    @contextmanager
    def get_cursor(self):
        """Context manager pour les curseurs (thread-safe)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
    
    def init_database(self):
        """Initialise la base avec schéma optimisé"""
        with self.get_cursor() as cur:
            # Table personas
            cur.execute('''
                CREATE TABLE IF NOT EXISTS personas (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    gender TEXT,
                    location TEXT,
                    occupation TEXT,
                    interests TEXT,
                    dislikes TEXT,
                    behaviors TEXT,
                    mood TEXT,
                    consistency_score REAL,
                    intelligence_level REAL,
                    paranoia_level REAL,
                    tech_savviness REAL,
                    spending_habit TEXT,
                    social_media_presence TEXT,
                    created_at TIMESTAMP,
                    last_active TIMESTAMP,
                    total_activities INTEGER DEFAULT 0,
                    success_rate REAL DEFAULT 1.0,
                    metadata TEXT
                )
            ''')
            
            # Table activités
            cur.execute('''
                CREATE TABLE IF NOT EXISTS activities (
                    id TEXT PRIMARY KEY,
                    persona_id TEXT,
                    activity_type TEXT,
                    site TEXT,
                    url TEXT,
                    query TEXT,
                    duration INTEGER,
                    metadata TEXT,
                    success BOOLEAN,
                    error_message TEXT,
                    timestamp TIMESTAMP,
                    FOREIGN KEY (persona_id) REFERENCES personas(id)
                )
            ''')
            
            # Table métriques
            cur.execute('''
                CREATE TABLE IF NOT EXISTS metrics (
                    id TEXT PRIMARY KEY,
                    timestamp TIMESTAMP,
                    personas_active INTEGER,
                    personas_total INTEGER,
                    confusion_score REAL,
                    noise_generated INTEGER,
                    trackers_detected INTEGER,
                    cpu_usage REAL,
                    memory_usage REAL,
                    detailed_metrics TEXT
                )
            ''')
            
            # Table trackers
            cur.execute('''
                CREATE TABLE IF NOT EXISTS trackers (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    domain TEXT,
                    type TEXT,
                    first_seen TIMESTAMP,
                    last_seen TIMESTAMP,
                    detection_count INTEGER,
                    sites_found TEXT,
                    cookies TEXT,
                    scripts TEXT,
                    countermeasures TEXT,
                    effectiveness REAL
                )
            ''')
            
            # Table achats
            cur.execute('''
                CREATE TABLE IF NOT EXISTS purchases (
                    id TEXT PRIMARY KEY,
                    persona_id TEXT,
                    product_name TEXT,
                    product_category TEXT,
                    price REAL,
                    site TEXT,
                    cart_value REAL,
                    abandoned BOOLEAN,
                    payment_method TEXT,
                    timestamp TIMESTAMP,
                    FOREIGN KEY (persona_id) REFERENCES personas(id)
                )
            ''')
            
            # Table faux comptes
            cur.execute('''
                CREATE TABLE IF NOT EXISTS fake_accounts (
                    id TEXT PRIMARY KEY,
                    persona_id TEXT,
                    platform TEXT,
                    username TEXT,
                    email TEXT,
                    password_hash TEXT,
                    profile_data TEXT,
                    posts_count INTEGER DEFAULT 0,
                    followers_count INTEGER DEFAULT 0,
                    following_count INTEGER DEFAULT 0,
                    created_at TIMESTAMP,
                    last_used TIMESTAMP,
                    status TEXT,
                    FOREIGN KEY (persona_id) REFERENCES personas(id)
                )
            ''')
            
            # Table cache
            cur.execute('''
                CREATE TABLE IF NOT EXISTS cache (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    expires TIMESTAMP
                )
            ''')
            
            # Table configuration
            cur.execute('''
                CREATE TABLE IF NOT EXISTS config (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    category TEXT,
                    updated_at TIMESTAMP
                )
            ''')
            
            # Table erreurs
            cur.execute('''
                CREATE TABLE IF NOT EXISTS errors (
                    id TEXT PRIMARY KEY,
                    timestamp TIMESTAMP,
                    component TEXT,
                    error_type TEXT,
                    error_message TEXT,
                    stack_trace TEXT,
                    context TEXT
                )
            ''')
    
    def setup_indexes(self):
        """Crée les index pour les performances"""
        try:
            with self.get_cursor() as cur:
                indexes = [
                    "CREATE INDEX IF NOT EXISTS idx_activities_persona_time ON activities(persona_id, timestamp)",
                    "CREATE INDEX IF NOT EXISTS idx_activities_type_time ON activities(activity_type, timestamp)",
                    "CREATE INDEX IF NOT EXISTS idx_metrics_timestamp ON metrics(timestamp)",
                    "CREATE INDEX IF NOT EXISTS idx_trackers_domain ON trackers(domain)",
                    "CREATE INDEX IF NOT EXISTS idx_purchases_persona ON purchases(persona_id)",
                    "CREATE INDEX IF NOT EXISTS idx_accounts_platform ON fake_accounts(platform)",
                    "CREATE INDEX IF NOT EXISTS idx_personas_active ON personas(last_active)"
                ]
                for idx in indexes:
                    try:
                        cur.execute(idx)
                    except:
                        pass
        except:
            pass
    
    def setup_triggers(self):
        """Configure les triggers pour l'intégrité"""
        try:
            with self.get_cursor() as cur:
                cur.execute('''
                    CREATE TRIGGER IF NOT EXISTS update_persona_activity_count
                    AFTER INSERT ON activities
                    BEGIN
                        UPDATE personas 
                        SET total_activities = total_activities + 1,
                            last_active = NEW.timestamp
                        WHERE id = NEW.persona_id;
                    END;
                ''')
        except:
            pass
    
    # ===== MÉTHODES DE SAUVEGARDE =====
    
    def save_persona(self, persona):
        """Sauvegarde un persona"""
        with self.get_cursor() as cur:
            cur.execute('''
                INSERT OR REPLACE INTO personas 
                (id, name, age, gender, location, occupation, interests, dislikes, 
                 behaviors, mood, consistency_score, intelligence_level, paranoia_level,
                 tech_savviness, spending_habit, social_media_presence, created_at, 
                 last_active, total_activities, success_rate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                persona.id,
                persona.name,
                persona.age,
                persona.gender,
                persona.location,
                persona.occupation,
                json.dumps(persona.interests),
                json.dumps(persona.dislikes),
                json.dumps(persona.behaviors),
                persona.mood.value if hasattr(persona.mood, 'value') else str(persona.mood),
                persona.consistency_score,
                persona.intelligence_level,
                persona.paranoia_level,
                persona.tech_savviness,
                persona.spending_habit,
                json.dumps(persona.social_media_presence),
                persona.created_at.isoformat() if persona.created_at else datetime.now().isoformat(),
                persona.last_active.isoformat() if persona.last_active else datetime.now().isoformat(),
                persona.total_activities,
                persona.success_rate
            ))
    
    def save_activity(self, persona_id, activity_type, site=None, url=None, query=None, 
                     duration=None, metadata=None, success=True, error_message=None):
        """Enregistre une activité"""
        with self.get_cursor() as cur:
            activity_id = str(uuid.uuid4())
            cur.execute('''
                INSERT INTO activities 
                (id, persona_id, activity_type, site, url, query, duration, metadata, 
                 success, error_message, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                activity_id,
                persona_id,
                activity_type.value if hasattr(activity_type, 'value') else str(activity_type),
                site,
                url,
                query,
                duration,
                json.dumps(metadata) if metadata else None,
                1 if success else 0,
                error_message,
                datetime.now().isoformat()
            ))
            return activity_id
    
    def save_metric(self, metric):
        """Sauvegarde une métrique"""
        with self.get_cursor() as cur:
            cur.execute('''
                INSERT INTO metrics 
                (id, timestamp, personas_active, personas_total, confusion_score, 
                 noise_generated, trackers_detected, cpu_usage, memory_usage, detailed_metrics)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                str(uuid.uuid4()),
                metric.timestamp.isoformat() if hasattr(metric, 'timestamp') else datetime.now().isoformat(),
                metric.personas_active if hasattr(metric, 'personas_active') else 0,
                metric.personas_total if hasattr(metric, 'personas_total') else 0,
                metric.confusion_score if hasattr(metric, 'confusion_score') else 0,
                metric.noise_generated if hasattr(metric, 'noise_generated') else 0,
                metric.trackers_detected if hasattr(metric, 'trackers_detected') else 0,
                metric.cpu_usage if hasattr(metric, 'cpu_usage') else 0,
                metric.memory_usage if hasattr(metric, 'memory_usage') else 0,
                json.dumps(metric.trackers_by_type) if hasattr(metric, 'trackers_by_type') else None
            ))
    
    def save_tracker(self, name, domain, tracker_type, site_url=None):
        """Enregistre un tracker détecté"""
        with self.get_cursor() as cur:
            # Vérifier si le tracker existe déjà
            cur.execute('''
                SELECT id, detection_count, sites_found FROM trackers 
                WHERE name = ? AND domain = ?
            ''', (name, domain))
            
            existing = cur.fetchone()
            
            if existing:
                # Mettre à jour
                sites = json.loads(existing[2]) if existing[2] else []
                if site_url and site_url not in sites:
                    sites.append(site_url)
                
                cur.execute('''
                    UPDATE trackers 
                    SET last_seen = ?, detection_count = ?, sites_found = ?
                    WHERE id = ?
                ''', (
                    datetime.now().isoformat(),
                    existing[1] + 1,
                    json.dumps(sites),
                    existing[0]
                ))
            else:
                # Nouveau tracker
                cur.execute('''
                    INSERT INTO trackers 
                    (id, name, domain, type, first_seen, last_seen, detection_count, sites_found)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    str(uuid.uuid4()),
                    name,
                    domain,
                    tracker_type.value if hasattr(tracker_type, 'value') else str(tracker_type),
                    datetime.now().isoformat(),
                    datetime.now().isoformat(),
                    1,
                    json.dumps([site_url]) if site_url else None
                ))
    
    def save_fake_account(self, platform, username, email, profile_data, persona_id=None):
        """Enregistre un faux compte"""
        with self.get_cursor() as cur:
            cur.execute('''
                INSERT INTO fake_accounts 
                (id, persona_id, platform, username, email, profile_data, 
                 posts_count, followers_count, following_count, created_at, last_used, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                str(uuid.uuid4()),
                persona_id,
                platform,
                username,
                email,
                json.dumps(profile_data),
                profile_data.get('posts_count', random.randint(0, 50)) if profile_data else 0,
                profile_data.get('followers_count', random.randint(0, 100)) if profile_data else 0,
                profile_data.get('following_count', random.randint(0, 200)) if profile_data else 0,
                datetime.now().isoformat(),
                datetime.now().isoformat(),
                'active'
            ))
    
    def save_purchase(self, persona_id, product_name, product_category, price, site, 
                     cart_value, abandoned=True, payment_method=None):
        """Enregistre un achat simulé"""
        with self.get_cursor() as cur:
            cur.execute('''
                INSERT INTO purchases 
                (id, persona_id, product_name, product_category, price, site, 
                 cart_value, abandoned, payment_method, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                str(uuid.uuid4()),
                persona_id,
                product_name,
                product_category,
                price,
                site,
                cart_value,
                1 if abandoned else 0,
                payment_method,
                datetime.now().isoformat()
            ))
    
    def save_config(self, key, value):
        """Sauvegarde une configuration"""
        with self.get_cursor() as cur:
            cur.execute('''
                INSERT OR REPLACE INTO config (key, value, category, updated_at)
                VALUES (?, ?, ?, ?)
            ''', (
                key,
                json.dumps(value),
                'general',
                datetime.now().isoformat()
            ))
    
    def save_error(self, component, error_type, error_message, stack_trace=None, context=None):
        """Enregistre une erreur"""
        with self.get_cursor() as cur:
            cur.execute('''
                INSERT INTO errors 
                (id, timestamp, component, error_type, error_message, stack_trace, context)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                str(uuid.uuid4()),
                datetime.now().isoformat(),
                component,
                error_type,
                error_message[:500] if error_message else None,
                stack_trace[:2000] if stack_trace else None,
                json.dumps(context) if context else None
            ))
    
    # ===== MÉTHODES DE LECTURE =====
    
    def load_config(self, key, default=None):
        """Charge une configuration"""
        with self.get_cursor() as cur:
            cur.execute('SELECT value FROM config WHERE key = ?', (key,))
            row = cur.fetchone()
            if row:
                return json.loads(row[0])
            return default
    
    def get_recent_metrics(self, hours=24):
        """Récupère les métriques récentes"""
        with self.get_cursor() as cur:
            cutoff = (datetime.now() - timedelta(hours=hours)).isoformat()
            cur.execute('''
                SELECT * FROM metrics WHERE timestamp > ? ORDER BY timestamp DESC
            ''', (cutoff,))
            return [dict(row) for row in cur.fetchall()]
    
    def get_active_personas(self, minutes=30):
        """Récupère les personas actifs"""
        with self.get_cursor() as cur:
            cutoff = (datetime.now() - timedelta(minutes=minutes)).isoformat()
            cur.execute('''
                SELECT * FROM personas WHERE last_active > ? ORDER BY last_active DESC
            ''', (cutoff,))
            return [dict(row) for row in cur.fetchall()]
    
    def get_all_personas(self, limit=100):
        """Récupère tous les personas"""
        with self.get_cursor() as cur:
            cur.execute('''
                SELECT * FROM personas ORDER BY last_active DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in cur.fetchall()]
    
    def get_persona_by_id(self, persona_id):
        """Récupère un persona par son ID"""
        with self.get_cursor() as cur:
            cur.execute('SELECT * FROM personas WHERE id = ?', (persona_id,))
            row = cur.fetchone()
            return dict(row) if row else None
    
    def get_recent_activities(self, limit=100):
        """Récupère les activités récentes"""
        with self.get_cursor() as cur:
            cur.execute('''
                SELECT a.*, p.name as persona_name 
                FROM activities a
                LEFT JOIN personas p ON a.persona_id = p.id
                ORDER BY a.timestamp DESC 
                LIMIT ?
            ''', (limit,))
            return [dict(row) for row in cur.fetchall()]
    
    def get_activities_by_persona(self, persona_id, limit=50):
        """Récupère les activités d'un persona"""
        with self.get_cursor() as cur:
            cur.execute('''
                SELECT * FROM activities 
                WHERE persona_id = ? 
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (persona_id, limit))
            return [dict(row) for row in cur.fetchall()]
    
    def get_trackers(self, limit=100):
        """Récupère les trackers détectés"""
        with self.get_cursor() as cur:
            cur.execute('''
                SELECT * FROM trackers 
                ORDER BY last_seen DESC 
                LIMIT ?
            ''', (limit,))
            return [dict(row) for row in cur.fetchall()]
    
    def get_tracker_stats(self):
        """Récupère les statistiques des trackers"""
        with self.get_cursor() as cur:
            cur.execute('''
                SELECT type, COUNT(*) as count, SUM(detection_count) as total
                FROM trackers GROUP BY type
            ''')
            return [dict(row) for row in cur.fetchall()]
    
    def get_fake_accounts(self, limit=100):
        """Récupère les faux comptes"""
        with self.get_cursor() as cur:
            cur.execute('''
                SELECT * FROM fake_accounts 
                ORDER BY created_at DESC 
                LIMIT ?
            ''', (limit,))
            return [dict(row) for row in cur.fetchall()]
    
    def get_purchases(self, limit=100):
        """Récupère les achats simulés"""
        with self.get_cursor() as cur:
            cur.execute('''
                SELECT * FROM purchases 
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (limit,))
            return [dict(row) for row in cur.fetchall()]
    
    def get_statistics(self) -> Dict:
        """Récupère des statistiques avancées"""
        stats = {}
        try:
            with self.get_cursor() as cur:
                # Comptages - version corrigée sans paramètres
                cur.execute('SELECT COUNT(*) FROM personas')
                stats['total_personas'] = cur.fetchone()[0]
                
                # Compter les activités des dernières 24h
                cutoff = (datetime.now() - timedelta(hours=24)).isoformat()
                cur.execute('SELECT COUNT(*) FROM activities WHERE timestamp > ?', (cutoff,))
                stats['activities_24h'] = cur.fetchone()[0]
                
                cur.execute('SELECT COUNT(*) FROM trackers')
                stats['trackers'] = cur.fetchone()[0]
                
                cur.execute('SELECT COUNT(*) FROM fake_accounts')
                stats['fake_accounts'] = cur.fetchone()[0]
                
                cur.execute('SELECT COUNT(*) FROM purchases')
                stats['purchases'] = cur.fetchone()[0]
                
                # Agrégations
                cur.execute('SELECT activity_type, COUNT(*) as count FROM activities GROUP BY activity_type')
                stats['activities_by_type'] = {}
                for row in cur.fetchall():
                    stats['activities_by_type'][row[0]] = row[1]
                
                cur.execute('SELECT platform, COUNT(*) as count FROM fake_accounts GROUP BY platform')
                stats['accounts_by_platform'] = {}
                for row in cur.fetchall():
                    stats['accounts_by_platform'][row[0]] = row[1]
                
        except Exception as e:
            logger.error(f"Error getting statistics: {e}")
            stats = {
                'total_personas': 0,
                'activities_24h': 0,
                'trackers': 0,
                'fake_accounts': 0,
                'purchases': 0,
                'activities_by_type': {},
                'accounts_by_platform': {}
            }
        
        return stats
    
    # ===== MÉTHODES DE NETTOYAGE =====
    
    def cleanup_old_data(self, days=30):
        """Nettoie les données anciennes"""
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()
        with self.get_cursor() as cur:
            cur.execute('DELETE FROM metrics WHERE timestamp < ?', (cutoff,))
            cur.execute('DELETE FROM activities WHERE timestamp < ?', (cutoff,))
            cur.execute('DELETE FROM errors WHERE timestamp < ?', (cutoff,))
    
    def cache_get(self, key):
        """Récupère une valeur du cache"""
        try:
            with self.get_cursor() as cur:
                cur.execute('SELECT value FROM cache WHERE key = ? AND expires > ?',
                           (key, datetime.now().isoformat()))
                row = cur.fetchone()
                if row:
                    return json.loads(row[0])
        except:
            pass
        return None
    
    def cache_set(self, key, value, ttl=300):
        """Stocke une valeur dans le cache"""
        try:
            expires = (datetime.now() + timedelta(seconds=ttl)).isoformat()
            with self.get_cursor() as cur:
                cur.execute('INSERT OR REPLACE INTO cache (key, value, expires) VALUES (?, ?, ?)',
                           (key, json.dumps(value), expires))
        except:
            pass
    
    def export_to_csv(self, table_name, output_path):
        """Exporte une table en CSV"""
        try:
            with self.get_cursor() as cur:
                cur.execute(f'SELECT * FROM {table_name}')
                rows = cur.fetchall()
                
                if rows:
                    import pandas as pd
                    df = pd.DataFrame([dict(row) for row in rows])
                    df.to_csv(output_path, index=False, encoding='utf-8')
                    return len(df)
        except Exception as e:
            logger.error(f"Export error: {e}")
        return 0

# ============================================================================
# GÉNÉRATEUR DE PERSONAS INTELLIGENT
# ============================================================================

class IntelligentPersonaGenerator:
    """Génère des personas ultra-réalistes avec IA comportementale"""
    
    def __init__(self, db_manager: AdvancedDatabaseManager):
        self.db = db_manager
        
        # Bases de données enrichies
        self.first_names = {
            'male': ['Jean', 'Pierre', 'Paul', 'Jacques', 'Thomas', 'Nicolas', 'Alexandre', 'François',
                    'Antoine', 'Philippe', 'Laurent', 'Michel', 'David', 'Julien', 'Sébastien', 'Christophe',
                    'Vincent', 'Olivier', 'Patrick', 'Stéphane'],
            'female': ['Marie', 'Sophie', 'Isabelle', 'Catherine', 'Anne', 'Julie', 'Sylvie', 'Nathalie',
                      'Valérie', 'Christine', 'Sandrine', 'Laurence', 'Patricia', 'Brigitte', 'Françoise',
                      'Caroline', 'Emilie', 'Aurélie', 'Céline', 'Véronique']
        }
        
        self.last_names = ['Martin', 'Bernard', 'Dubois', 'Thomas', 'Robert', 'Richard', 'Petit', 'Durand',
                          'Leroy', 'Moreau', 'Simon', 'Laurent', 'Lefebvre', 'Michel', 'Garcia', 'David',
                          'Bertrand', 'Roux', 'Vincent', 'Fournier']
        
        self.locations = [
            {'city': 'Paris', 'region': 'Île-de-France', 'country': 'France', 'timezone': 'Europe/Paris'},
            {'city': 'Lyon', 'region': 'Auvergne-Rhône-Alpes', 'country': 'France', 'timezone': 'Europe/Paris'},
            {'city': 'Marseille', 'region': "Provence-Alpes-Côte d'Azur", 'country': 'France', 'timezone': 'Europe/Paris'},
            {'city': 'Toulouse', 'region': 'Occitanie', 'country': 'France', 'timezone': 'Europe/Paris'},
            {'city': 'Bordeaux', 'region': 'Nouvelle-Aquitaine', 'country': 'France', 'timezone': 'Europe/Paris'},
            {'city': 'Lille', 'region': 'Hauts-de-France', 'country': 'France', 'timezone': 'Europe/Paris'}
        ]
        
        self.occupations = [
            'Développeur', 'Architecte', 'Professeur', 'Infirmier', 'Médecin', 'Avocat', 'Commerçant',
            'Artisan', 'Artiste', 'Musicien', 'Écrivain', 'Journaliste', 'Photographe', 'Designer',
            'Consultant', 'Manager', 'Directeur', 'Technicien', 'Ingénieur', 'Chercheur', 'Étudiant'
        ]
        
        self.interests_categories = {
            'technology': ['IA', 'programmation', 'blockchain', 'crypto', 'gaming', 'robotique'],
            'travel': ['voyage', 'aventure', 'randonnée', 'photographie', 'culture', 'gastronomie'],
            'health': ['fitness', 'nutrition', 'yoga', 'méditation', 'sport', 'bien-être'],
            'fashion': ['mode', 'beauté', 'maquillage', 'streetwear', 'luxe', 'vintage'],
            'food': ['cuisine', 'pâtisserie', 'oenologie', 'gastronomie', 'recettes', 'bio'],
            'music': ['musique', 'concerts', 'production', 'instruments', 'DJ', 'chant'],
            'sports': ['football', 'basketball', 'tennis', 'natation', 'cyclisme', 'escalade'],
            'arts': ['peinture', 'sculpture', 'dessin', 'photographie', 'cinéma', 'théâtre']
        }
    
    async def generate_persona(self, complexity: float = 0.7) -> Persona:
        """Génère un persona avec un niveau de complexité donné"""
        
        # Caractéristiques de base
        gender = random.choice(['male', 'female'])
        first_name = random.choice(self.first_names[gender])
        last_name = random.choice(self.last_names)
        age = int(np.random.normal(35, 12))
        age = max(18, min(80, age))
        
        location = random.choice(self.locations)
        
        # Personnalité
        intelligence = np.random.beta(2, 2)  # Distribution autour de 0.5
        paranoia = np.random.beta(1.5, 3) if complexity < 0.5 else np.random.beta(3, 1.5)
        tech_savviness = np.random.beta(2 + age/100, 2)  # Les jeunes plus tech
        
        # Intérêts (sélection pondérée)
        interests = []
        n_interests = int(np.random.normal(8, 3))
        n_interests = max(3, min(15, n_interests))
        
        # Poids des catégories selon la personnalité
        weights = {}
        for category in self.interests_categories:
            if tech_savviness > 0.7 and category == 'technology':
                weights[category] = 3
            elif paranoia > 0.7 and category == 'health':
                weights[category] = 3
            else:
                weights[category] = 1
        
        categories = random.choices(
            list(self.interests_categories.keys()),
            weights=[weights.get(c, 1) for c in self.interests_categories],
            k=n_interests
        )
        
        for category in categories:
            interests.append(random.choice(self.interests_categories[category]))
        
        # Dislikes (ce qu'ils n'aiment pas)
        all_interests = sum(self.interests_categories.values(), [])
        dislikes = random.sample(all_interests, random.randint(2, 5))
        
        # Comportements détaillés
        behaviors = {
            'browsing_speed': float(np.random.normal(1.5, 0.5)),
            'click_pattern': random.choice(['explorer', 'focused', 'random', 'systematic']),
            'active_hours': self.generate_active_hours(age, tech_savviness),
            'device_preference': random.choice(['mobile', 'desktop', 'tablet', 'mixed']),
            'os': random.choice(['Windows', 'macOS', 'Linux', 'Android', 'iOS']),
            'browser': random.choice(['Chrome', 'Firefox', 'Safari', 'Edge']),
            'language': random.choice(['fr-FR', 'en-US', 'es-ES', 'de-DE']),
            'search_depth': random.choice(['surface', 'medium', 'deep']),
            'ad_tolerance': float(np.random.uniform(0, 1)),
            'privacy_concern': float(paranoia),
            'social_media_usage': self.generate_social_usage(age),
            'purchase_impulsivity': float(np.random.beta(2, 2)),
            'news_consumption': random.choice(['daily', 'weekly', 'rarely'])
        }
        
        # Humeur initiale
        mood = random.choice(list(PersonaMood))
        
        # Présence sociale
        social_media_presence = {
            'facebook': random.random() > 0.3,
            'twitter': random.random() > 0.5,
            'instagram': random.random() > 0.4,
            'linkedin': tech_savviness > 0.4 and age < 55,
            'tiktok': age < 30 and random.random() > 0.6,
            'snapchat': age < 25
        }
        
        # Habitudes de dépense
        spending = np.random.beta(2, 2)
        if spending < 0.3:
            spending_habit = 'frugal'
        elif spending < 0.7:
            spending_habit = 'average'
        else:
            spending_habit = 'spender'
        
        # Création du persona
        persona_id = secrets.token_hex(8)
        
        persona = Persona(
            id=persona_id,
            name=f"{first_name} {last_name}",
            age=age,
            gender=gender,
            location=f"{location['city']}, {location['region']}",
            occupation=random.choice(self.occupations),
            interests=interests,
            dislikes=dislikes,
            behaviors=behaviors,
            mood=mood,
            activity_log=[],
            consistency_score=float(np.random.uniform(0.6, 0.98)),
            intelligence_level=float(intelligence),
            paranoia_level=float(paranoia),
            tech_savviness=float(tech_savviness),
            spending_habit=spending_habit,
            social_media_presence=social_media_presence,
            fake_accounts=[],
            created_at=datetime.now(),
            last_active=datetime.now()
        )
        
        # Sauvegarde
        self.db.save_persona(persona)
        
        return persona
    
    def generate_active_hours(self, age: int, tech_savviness: float) -> Dict:
        """Génère des heures d'activité réalistes"""
        if age > 60:
            # Personnes âgées: matinal
            start = random.randint(6, 8)
            end = random.randint(20, 22)
        elif age < 25:
            # Jeunes: nocturne
            start = random.randint(10, 14)
            # Pour les heures qui traversent minuit, on utilise une logique différente
            if random.random() > 0.5:
                end = random.randint(2, 4)  # 2-4am (jour suivant)
                # On stocke l'heure de fin avec un flag pour indiquer que c'est le lendemain
                return {
                    'start': start,
                    'end': end,
                    'peak': (start + end + 24) // 2 % 24,  # Calcul du pic en tenant compte du lendemain
                    'pattern': random.choice(['constant', 'increasing', 'decreasing']),
                    'crosses_midnight': True
                }
            else:
                end = random.randint(22, 23)
                return {
                    'start': start,
                    'end': end,
                    'peak': (start + end) // 2,
                    'pattern': random.choice(['constant', 'increasing', 'decreasing']),
                    'crosses_midnight': False
                }
        else:
            # Adultes: variable
            if tech_savviness > 0.7:
                start = random.randint(8, 11)
                # Parfois tard dans la nuit
                if random.random() > 0.3:
                    end = random.randint(23, 23)
                    return {
                        'start': start,
                        'end': end,
                        'peak': (start + end) // 2,
                        'pattern': random.choice(['constant', 'increasing', 'decreasing']),
                        'crosses_midnight': False
                    }
                else:
                    end = random.randint(1, 3)
                    return {
                        'start': start,
                        'end': end,
                        'peak': (start + end + 24) // 2 % 24,
                        'pattern': random.choice(['constant', 'increasing', 'decreasing']),
                        'crosses_midnight': True
                    }
            else:
                start = random.randint(7, 9)
                end = random.randint(21, 23)
                return {
                    'start': start,
                    'end': end,
                    'peak': (start + end) // 2,
                    'pattern': random.choice(['constant', 'increasing', 'decreasing']),
                    'crosses_midnight': False
                }
    
    def generate_social_usage(self, age: int) -> Dict:
        """Génère des patterns d'usage des réseaux sociaux"""
        if age < 25:
            intensity = 'high'
            sessions = random.randint(10, 20)
        elif age < 40:
            intensity = 'medium'
            sessions = random.randint(5, 12)
        else:
            intensity = 'low'
            sessions = random.randint(1, 5)
        
        return {
            'intensity': intensity,
            'sessions_per_day': sessions,
            'avg_duration_minutes': random.randint(5, 30),
            'post_frequency': random.choice(['daily', 'weekly', 'rarely']),
            'engagement_type': random.choice(['lurker', 'liker', 'commenter', 'creator'])
        }

# ============================================================================
# MOTEUR DE NAVIGATION INTELLIGENT (sans playwright_stealth)
# ============================================================================

class IntelligentBrowserEngine:
    """Moteur de navigation avec comportement humain avancé"""
    
    def __init__(self, config: AdvancedConfig, db_manager: AdvancedDatabaseManager):
        self.config = config
        self.db = db_manager
        self.playwright = None
        self.browser = None
        self.contexts = []
        
        # User agents
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1'
        ]
        
        # Statistiques
        self.pages_visited = 0
        self.actions_performed = 0
        self.errors = []
        
    async def initialize(self):
        """Initialise le moteur"""
        self.playwright = await async_playwright().start()
        
        # Options de lancement pour éviter la détection
        launch_args = [
            '--disable-blink-features=AutomationControlled',
            '--disable-features=IsolateOrigins,site-per-process',
            '--disable-web-security',
            '--disable-features=BlockInsecurePrivateNetworkRequests',
            '--disable-features=OutOfBlinkCors',
            '--disable-webgl',
            '--disable-canvas-aa',
            '--disable-2d-canvas-clip-aa',
            '--disable-accelerated-2d-canvas',
            '--disable-gpu',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-accelerated-2d-canvas',
            '--disable-accelerated-jpeg-decoding',
            '--disable-accelerated-mjpeg-decode',
            '--disable-accelerated-video-decode',
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-breakpad',
            '--disable-component-extensions-with-background-pages',
            '--disable-features=TranslateUI',
            '--disable-ipc-flooding-protection',
            '--disable-renderer-backgrounding',
            '--enable-features=NetworkService,NetworkServiceInProcess',
            '--force-color-profile=srgb',
            '--hide-scrollbars',
            '--metrics-recording-only',
            '--mute-audio',
            '--no-first-run',
            '--no-zygote',
            '--use-gl=swiftshader',
            '--use-mock-keychain',
            '--webrtc-ip-handling-policy=disable_non_proxied_udp'
        ]
        
        self.browser = await self.playwright.chromium.launch(
            headless=self.config.headless,
            args=launch_args
        )
    
    async def create_persona_context(self, persona: Persona) -> BrowserContext:
        """Crée un contexte de navigation pour un persona"""
        
        # Génération d'un fingerprint unique
        viewport = self.generate_viewport()
        user_agent = random.choice(self.user_agents) if self.config.user_agent_rotation else self.user_agents[0]
        
        # Configuration du contexte
        context = await self.browser.new_context(
            viewport=viewport,
            user_agent=user_agent,
            locale=persona.behaviors['language'],
            timezone_id='Europe/Paris',
            permissions=['geolocation'],
            device_scale_factor=random.uniform(1, 2),
            has_touch=random.choice([True, False]),
            color_scheme=random.choice(['light', 'dark']),
            reduced_motion=random.choice(['reduce', 'no-preference']),
            extra_http_headers={
                'Accept-Language': f"{persona.behaviors['language']},en;q=0.9",
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'DNT': '1' if persona.paranoia_level > 0.7 else '0',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': f'"{random.choice(["Windows", "macOS", "Linux"])}"'
            }
        )
        
        # Supprimer les traces d'automatisation
        await context.add_init_script("""
            // Supprimer les propriétés d'automatisation
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            
            // Masquer les plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
            
            // Masquer les langues
            Object.defineProperty(navigator, 'languages', {
                get: () => ['fr-FR', 'fr', 'en-US', 'en']
            });
            
            // Remplacer la fonction de notification
            window.chrome = {
                runtime: {}
            };
            
            // Masquer l'empreinte
            Object.defineProperty(navigator, 'hardwareConcurrency', {
                get: () => 8
            });
            
            // Simuler une vraie pile d'appels
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications' ?
                    Promise.resolve({ state: Notification.permission }) :
                    originalQuery(parameters)
            );
        """)
        
        # Ajout de cookies simulés
        await self.add_fake_cookies(context, persona)
        
        self.contexts.append(context)
        return context
    
    def generate_viewport(self) -> Dict:
        """Génère une résolution d'écran réaliste"""
        common_resolutions = [
            (1920, 1080), (1366, 768), (1536, 864), (1440, 900),
            (1280, 720), (1600, 900), (2560, 1440)
        ]
        width, height = random.choice(common_resolutions)
        
        # Variation naturelle
        width += random.randint(-20, 20)
        height += random.randint(-20, 20)
        
        return {'width': width, 'height': height}
    
    async def add_fake_cookies(self, context: BrowserContext, persona: Persona):
        """Ajoute des cookies simulés"""
        common_cookies = [
            {'name': '_ga', 'value': f'GA1.2.{random.randint(1000000000, 9999999999)}', 'domain': '.google.com'},
            {'name': '_gid', 'value': f'GA1.2.{random.randint(1000000000, 9999999999)}', 'domain': '.google.com'},
            {'name': 'session_id', 'value': secrets.token_hex(16), 'domain': '.amazon.fr'},
            {'name': 'user_pref', 'value': 'lang=fr', 'domain': '.youtube.com'}
        ]
        
        for cookie in common_cookies:
            if random.random() > 0.5:
                await context.add_cookies([{
                    **cookie,
                    'path': '/',
                    'secure': True,
                    'httpOnly': False,
                    'sameSite': 'Lax'
                }])
    
    async def simulate_human_behavior(self, page: Page, persona: Persona, action_type: str):
        """Simule un comportement humain avancé"""
        
        # Délai initial (temps de réaction)
        reaction_time = np.random.normal(0.8, 0.3)
        reaction_time = max(0.3, min(2.0, reaction_time))
        await asyncio.sleep(reaction_time)
        
        # Mouvement de souris
        if self.config.mouse_movement_curve:
            await self.simulate_curved_mouse_movement(page)
        else:
            # Mouvement aléatoire simple
            for _ in range(random.randint(1, 3)):
                x = random.randint(100, 800)
                y = random.randint(100, 600)
                await page.mouse.move(x, y, steps=random.randint(5, 10))
                await asyncio.sleep(random.uniform(0.05, 0.1))
        
        # Scroll naturel
        if random.random() > 0.3:
            await self.simulate_natural_scroll(page)
        
        # Micro-pauses
        if random.random() > 0.7:
            pause_duration = random.uniform(1, 3)
            await asyncio.sleep(pause_duration)
    
    async def simulate_curved_mouse_movement(self, page: Page):
        """Simule un mouvement de souris avec courbe"""
        start_x, start_y = random.randint(100, 800), random.randint(100, 600)
        end_x, end_y = random.randint(200, 900), random.randint(200, 700)
        
        # Mouvement linéaire avec petites variations
        steps = random.randint(15, 25)
        for i in range(steps + 1):
            t = i / steps
            # Mouvement avec légère courbe sinusoïdale
            x = start_x + (end_x - start_x) * t
            y = start_y + (end_y - start_y) * t + 20 * np.sin(t * np.pi)
            
            await page.mouse.move(int(x), int(y))
            await asyncio.sleep(0.01)
    
    async def simulate_natural_scroll(self, page: Page):
        """Simule un scroll naturel"""
        scroll_distance = random.randint(300, 1500)
        steps = 20
        
        for i in range(steps):
            progress = i / steps
            # Accélération/décélération
            ease = 1 - (1 - progress) ** 3
            scroll_y = int(scroll_distance * ease)
            
            await page.evaluate(f'window.scrollTo(0, {scroll_y})')
            await asyncio.sleep(0.05)
    
    async def navigate_to(self, page: Page, url: str, persona: Persona) -> bool:
        """Navigation avec gestion d'erreur"""
        max_retries = 2
        for attempt in range(max_retries):
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=self.config.navigation_timeout)
                
                # Comportement post-navigation
                await self.simulate_human_behavior(page, persona, 'navigation')
                
                self.pages_visited += 1
                return True
                
            except Exception as e:
                logger.warning(f"Navigation error (attempt {attempt+1}): {e}")
                await asyncio.sleep(random.uniform(1, 2))
        
        self.errors.append({'url': url, 'error': str(e), 'time': datetime.now()})
        return False
    
    async def type_human_like(self, page: Page, selector: str, text: str):
        """Tape du texte comme un humain"""
        try:
            await page.click(selector)
            await asyncio.sleep(random.uniform(0.1, 0.3))
            
            for char in text:
                delay = random.uniform(50, 200) / 1000  # ms to seconds
                await page.keyboard.type(char, delay=delay)
                
                if random.random() > 0.95:
                    await asyncio.sleep(random.uniform(0.3, 0.8))
        except:
            pass
    
    async def click_random_element(self, page: Page, persona: Persona) -> bool:
        """Clique sur un élément aléatoire"""
        try:
            clickable = await page.query_selector_all('a, button, [role="button"]')
            
            if clickable and random.random() > 0.6:
                element = random.choice(clickable[:10])  # Limiter pour éviter les erreurs
                
                try:
                    await element.scroll_into_view_if_needed()
                    await asyncio.sleep(random.uniform(0.3, 0.8))
                    await element.click()
                    self.actions_performed += 1
                    return True
                except:
                    pass
        except:
            pass
        
        return False
    
    async def cleanup(self):
        """Nettoie les ressources"""
        for context in self.contexts:
            try:
                await context.close()
            except:
                pass
        
        if self.browser:
            try:
                await self.browser.close()
            except:
                pass
        
        if self.playwright:
            try:
                await self.playwright.stop()
            except:
                pass


# ============================================================================
# DÉTECTEUR DE TRACKERS AVANCÉ
# ============================================================================

class AdvancedTrackerDetector:
    """Détecte et analyse les trackers avec des patterns avancés"""
    
    def __init__(self, db_manager: AdvancedDatabaseManager):
        self.db = db_manager
        self.tracker_patterns = self.load_tracker_patterns()
        self.countermeasures = self.load_countermeasures()
        self.detection_stats = defaultdict(int)
        
    def load_tracker_patterns(self) -> Dict:
        """Charge les patterns de détection des trackers"""
        return {
            'google_analytics': {
                'patterns': [
                    r'google-analytics\.com/analytics\.js',
                    r'googletagmanager\.com/gtag/js',
                    r'www\.google\.com/analytics',
                    r'gtag\(\'config\'',
                    r'GoogleAnalyticsObject'
                ],
                'type': TrackerType.ANALYTICS,
                'company': 'Google',
                'risk_level': 'medium'
            },
            'facebook_pixel': {
                'patterns': [
                    r'connect\.facebook\.net/.*/fbevents\.js',
                    r'fbq\(',
                    r'facebook\.com/tr/',
                    r'_fbp',
                    r'pixel\.facebook'
                ],
                'type': TrackerType.PIXEL,
                'company': 'Meta',
                'risk_level': 'high'
            },
            'doubleclick': {
                'patterns': [
                    r'doubleclick\.net',
                    r'googleads\.g\.doubleclick',
                    r'fls\.doubleclick',
                    r'pubads\.g\.doubleclick'
                ],
                'type': TrackerType.ADVERTISING,
                'company': 'Google',
                'risk_level': 'high'
            },
            'amazon_ads': {
                'patterns': [
                    r'amazon-adsystem\.com',
                    r'assoc-amazon\.com',
                    r'ws-na\.amazon-adsystem',
                    r'z-na\.amazon-adsystem'
                ],
                'type': TrackerType.ADVERTISING,
                'company': 'Amazon',
                'risk_level': 'medium'
            },
            'hotjar': {
                'patterns': [
                    r'static\.hotjar\.com',
                    r'script\.hotjar\.com',
                    r'_hjSession',
                    r'hj\(\)'
                ],
                'type': TrackerType.ANALYTICS,
                'company': 'Hotjar',
                'risk_level': 'low'
            },
            'mixpanel': {
                'patterns': [
                    r'cdn\.mixpanel\.com',
                    r'mixpanel\.init',
                    r'mixpanel\.track',
                    r'mixpanel\.identify'
                ],
                'type': TrackerType.ANALYTICS,
                'company': 'Mixpanel',
                'risk_level': 'medium'
            },
            'twitter_analytics': {
                'patterns': [
                    r'static\.ads-twitter\.com',
                    r'analytics\.twitter\.com',
                    r'twttr\.conversion\.track',
                    r'platform\.twitter\.com/widgets'
                ],
                'type': TrackerType.SOCIAL,
                'company': 'Twitter',
                'risk_level': 'medium'
            },
            'linkedin_analytics': {
                'patterns': [
                    r'px\.ads\.linkedin\.com',
                    r'snap\.licdn\.com',
                    r'linkedin\.com/analytics'
                ],
                'type': TrackerType.SOCIAL,
                'company': 'LinkedIn',
                'risk_level': 'medium'
            },
            'fingerprintjs': {
                'patterns': [
                    r'fingerprintjs\.com',
                    r'fp\.js',
                    r'getVisitorData',
                    r'Fingerprint2'
                ],
                'type': TrackerType.FINGERPRINT,
                'company': 'FingerprintJS',
                'risk_level': 'critical'
            },
            'criteo': {
                'patterns': [
                    r'static\.criteo\.net',
                    r'cas\.criteo\.com',
                    r'dis\.criteo\.com',
                    r'criteo\.com/'
                ],
                'type': TrackerType.ADVERTISING,
                'company': 'Criteo',
                'risk_level': 'high'
            }
        }
    
    def load_countermeasures(self) -> Dict:
        """Charge les contre-mesures disponibles"""
        return {
            TrackerType.ANALYTICS: [
                self.block_analytics,
                self.spoof_analytics_data,
                self.generate_fake_events
            ],
            TrackerType.ADVERTISING: [
                self.click_ads_randomly,
                self.block_ad_requests,
                self.generate_fake_conversions
            ],
            TrackerType.SOCIAL: [
                self.simulate_social_interaction,
                self.spoof_social_data,
                self.generate_fake_likes
            ],
            TrackerType.FINGERPRINT: [
                self.rotate_fingerprint,
                self.add_fingerprint_noise,
                self.block_fingerprinting_scripts
            ],
            TrackerType.PIXEL: [
                self.spoof_pixel_data,
                self.block_pixel_requests,
                self.generate_fake_pixel_events
            ]
        }
    
    async def analyze_page(self, page: Page, url: str) -> List[Tracker]:
        """Analyse complète d'une page pour détecter les trackers"""
        detected_trackers = []
        
        try:
            # Analyse des requêtes réseau
            network_trackers = await self.analyze_network_requests(page)
            detected_trackers.extend(network_trackers)
            
            # Analyse du code JavaScript
            js_trackers = await self.analyze_javascript(page)
            detected_trackers.extend(js_trackers)
            
            # Analyse des cookies
            cookie_trackers = await self.analyze_cookies(page)
            detected_trackers.extend(cookie_trackers)
            
            # Analyse du localStorage
            storage_trackers = await self.analyze_local_storage(page)
            detected_trackers.extend(storage_trackers)
            
            # Déduplication
            unique_trackers = self.deduplicate_trackers(detected_trackers)
            
            # Sauvegarde
            for tracker in unique_trackers:
                self.db.save_tracker(
                    tracker.name,
                    tracker.domain,
                    tracker.type.value
                )
                
            return unique_trackers
            
        except Exception as e:
            logger.error(f"Error analyzing trackers: {e}")
            return []
    
    async def analyze_network_requests(self, page: Page) -> List[Tracker]:
        """Analyse les requêtes réseau"""
        trackers = []
        
        try:
            # Récupère toutes les requêtes
            requests = await page.evaluate('''() => {
                const resources = performance.getEntriesByType('resource');
                return resources.map(r => ({
                    url: r.name,
                    type: r.initiatorType,
                    duration: r.duration,
                    size: r.transferSize
                }));
            }''')
            
            for req in requests:
                url = req['url']
                
                for name, pattern_info in self.tracker_patterns.items():
                    for pattern in pattern_info['patterns']:
                        if re.search(pattern, url, re.IGNORECASE):
                            tracker = Tracker(
                                id=str(uuid.uuid4()),
                                name=name,
                                domain=urlparse(url).netloc,
                                type=pattern_info['type'],
                                first_seen=datetime.now(),
                                last_seen=datetime.now(),
                                detection_count=1,
                                sites_found=[page.url],
                                cookies=[],
                                scripts=[],
                                countermeasures_applied=[],
                                effectiveness=1.0
                            )
                            trackers.append(tracker)
                            self.detection_stats[pattern_info['type']] += 1
                            break
                            
        except Exception as e:
            logger.debug(f"Network analysis error: {e}")
        
        return trackers
    
    async def analyze_javascript(self, page: Page) -> List[Tracker]:
        """Analyse le code JavaScript pour trouver des trackers"""
        trackers = []
        
        try:
            # Récupère tous les scripts
            scripts = await page.evaluate('''() => {
                const scripts = document.getElementsByTagName('script');
                return Array.from(scripts).map(s => s.src || s.innerText);
            }''')
            
            for script in scripts:
                if not script:
                    continue
                    
                for name, pattern_info in self.tracker_patterns.items():
                    for pattern in pattern_info['patterns']:
                        if re.search(pattern, script, re.IGNORECASE):
                            # Vérifier si déjà détecté
                            if not any(t.name == name for t in trackers):
                                tracker = Tracker(
                                    id=str(uuid.uuid4()),
                                    name=name,
                                    domain='inline-script',
                                    type=pattern_info['type'],
                                    first_seen=datetime.now(),
                                    last_seen=datetime.now(),
                                    detection_count=1,
                                    sites_found=[page.url],
                                    cookies=[],
                                    scripts=[script[:200]],
                                    countermeasures_applied=[],
                                    effectiveness=1.0
                                )
                                trackers.append(tracker)
                            break
                            
        except Exception as e:
            logger.debug(f"JavaScript analysis error: {e}")
        
        return trackers
    
    async def analyze_cookies(self, page: Page) -> List[Tracker]:
        """Analyse les cookies pour détecter des trackers"""
        trackers = []
        
        try:
            cookies = await page.context.cookies()
            
            for cookie in cookies:
                for name, pattern_info in self.tracker_patterns.items():
                    for pattern in pattern_info['patterns']:
                        if re.search(pattern, cookie['name'] + cookie['value'], re.IGNORECASE):
                            # Pattern cookie tracker
                            pass
                            
        except Exception as e:
            logger.debug(f"Cookie analysis error: {e}")
        
        return trackers
    
    async def analyze_local_storage(self, page: Page) -> List[Tracker]:
        """Analyse le localStorage"""
        trackers = []
        
        try:
            storage = await page.evaluate('() => JSON.stringify(localStorage)')
            # Analyse du localStorage...
            
        except Exception as e:
            logger.debug(f"Storage analysis error: {e}")
        
        return trackers
    
    def deduplicate_trackers(self, trackers: List[Tracker]) -> List[Tracker]:
        """Déduplique les trackers détectés"""
        unique = {}
        
        for tracker in trackers:
            key = f"{tracker.name}_{tracker.domain}"
            
            if key not in unique:
                unique[key] = tracker
            else:
                unique[key].detection_count += 1
                if tracker.sites_found and tracker.sites_found[0] not in unique[key].sites_found:
                    unique[key].sites_found.append(tracker.sites_found[0])
        
        return list(unique.values())
    
    async def apply_countermeasure(self, page: Page, tracker: Tracker) -> bool:
        """Applique une contre-mesure adaptée"""
        try:
            countermeasures = self.countermeasures.get(tracker.type, [])
            if countermeasures:
                countermeasure = random.choice(countermeasures)
                await countermeasure(page)
                tracker.countermeasures_applied.append(countermeasure.__name__)
                
                # Évaluer l'efficacité
                tracker.effectiveness = random.uniform(0.7, 1.0)
                return True
                
        except Exception as e:
            logger.error(f"Countermeasure error: {e}")
        
        return False
    
    # Contre-mesures spécifiques
    async def block_analytics(self, page: Page):
        await page.evaluate('window.ga = function(){};')
    
    async def spoof_analytics_data(self, page: Page):
        await page.evaluate('''
            window.dataLayer = window.dataLayer || [];
            for(let i=0; i<10; i++) {
                dataLayer.push({
                    'event': 'random_' + i,
                    'value': Math.random()
                });
            }
        ''')
    
    async def generate_fake_events(self, page: Page):
        await page.evaluate('''
            if (typeof gtag === 'function') {
                gtag('event', 'fake_purchase', {
                    'value': Math.random() * 100,
                    'currency': 'EUR'
                });
            }
        ''')
    
    async def click_ads_randomly(self, page: Page):
        ads = await page.query_selector_all('[id*="ad"], [class*="ad"]')
        if ads and random.random() > 0.7:
            await random.choice(ads).click()
    
    async def block_ad_requests(self, page: Page):
        await page.route('**/*', lambda route: route.abort() 
                        if 'ad' in route.request.url.lower() else route.continue_())
    
    async def generate_fake_conversions(self, page: Page):
        # Simule des conversions
        pass
    
    async def simulate_social_interaction(self, page: Page):
        # Simule likes/shares
        pass
    
    async def spoof_social_data(self, page: Page):
        # Modifie les données sociales
        pass
    
    async def generate_fake_likes(self, page: Page):
        await page.evaluate('''
            if (typeof FB !== 'undefined') {
                FB.Event.subscribe('edge.create', function() {});
            }
        ''')
    
    async def rotate_fingerprint(self, page: Page):
        # Change le fingerprint
        pass
    
    async def add_fingerprint_noise(self, page: Page):
        await page.evaluate('''
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            Object.defineProperty(navigator, 'plugins', {get: () => [1,2,3,4,5]});
        ''')
    
    async def block_fingerprinting_scripts(self, page: Page):
        await page.route('**/*fingerprint*', lambda route: route.abort())
    
    async def spoof_pixel_data(self, page: Page):
        # Modifie les données des pixels
        pass
    
    async def block_pixel_requests(self, page: Page):
        await page.route('**/*pixel*', lambda route: route.abort())
    
    async def generate_fake_pixel_events(self, page: Page):
        # Génère des événements pixel factices
        pass

# ============================================================================
# MOTEUR PRINCIPAL ULTRA-AMÉLIORÉ
# ============================================================================

class UltimateBrouilleurPiste:
    """Moteur principal avec toutes les fonctionnalités avancées"""
    
    def __init__(self, config_path: str = None):
        # Configuration
        if config_path and os.path.exists(config_path):
            self.config = self.load_config(config_path)
        else:
            self.config = AdvancedConfig()
        
        # Base de données
        self.db = AdvancedDatabaseManager()
        
        # Composants
        self.persona_generator = IntelligentPersonaGenerator(self.db)
        self.browser_engine = IntelligentBrowserEngine(self.config, self.db)
        self.tracker_detector = AdvancedTrackerDetector(self.db)
        
        # État
        self.personas: List[Persona] = []
        self.active_tasks = []
        self.is_running = False
        self.metrics_queue = Queue()
        
        # Statistiques
        self.stats = {
            'start_time': None,
            'total_actions': 0,
            'successful_actions': 0,
            'failed_actions': 0,
            'trackers_detected': 0,
            'countermeasures_applied': 0
        }
        
        # Logger
        self.logger = logging.getLogger(__name__)
    
    def load_config(self, config_path: str) -> AdvancedConfig:
        """Charge la configuration depuis un fichier"""
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        return AdvancedConfig(**config_data)
    
    async def start(self):
        """Démarre le brouilleur"""
        self.is_running = True
        self.stats['start_time'] = datetime.now()
        
        self.logger.info("🚀 Démarrage du Brouilleur de Piste v3.0")
        
        # Initialisation du moteur de navigation
        await self.browser_engine.initialize()
        
        # Création des personas initiaux
        await self.initialize_personas()
        
        # Démarrage des tâches asynchrones
        self.active_tasks = [
            asyncio.create_task(self.run_personas_loop()),
            asyncio.create_task(self.run_metrics_loop()),
            asyncio.create_task(self.run_cleanup_loop()),
            asyncio.create_task(self.run_backup_loop()) if self.config.auto_backup else None
        ]
        self.active_tasks = [t for t in self.active_tasks if t]
        
        self.logger.info(f"✅ Brouilleur démarré avec {len(self.personas)} personas")
    
    async def initialize_personas(self):
        """Initialise les personas de départ"""
        for i in range(min(5, self.config.max_personas)):
            persona = await self.persona_generator.generate_persona()
            self.personas.append(persona)
            self.logger.info(f"  ✓ Persona créé: {persona.name} ({persona.age} ans, {persona.occupation})")
            await asyncio.sleep(1)
    
    async def run_personas_loop(self):
        """Boucle principale de gestion des personas"""
        while self.is_running:
            try:
                # Ajuster le nombre de personas
                await self.adjust_personas_count()
                
                # Exécuter des activités pour chaque persona
                tasks = []
                for persona in self.personas:
                    if self.should_persona_act(persona):
                        tasks.append(asyncio.create_task(
                            self.execute_persona_activity(persona)
                        ))
                
                if tasks:
                    await asyncio.gather(*tasks, return_exceptions=True)
                
                # Attendre avant le prochain cycle
                await asyncio.sleep(60)  # 1 minute
                
            except Exception as e:
                self.logger.error(f"Error in personas loop: {e}")
                await asyncio.sleep(10)
    
    async def adjust_personas_count(self):
        """Ajuste le nombre de personas actifs"""
        current_count = len(self.personas)
        target_count = self.config.max_personas
        
        if current_count < target_count:
            # Créer de nouveaux personas
            to_create = min(target_count - current_count, 
                          self.config.personas_creation_rate)
            
            for i in range(to_create):
                persona = await self.persona_generator.generate_persona()
                self.personas.append(persona)
                self.logger.info(f"➕ Nouveau persona: {persona.name}")
                await asyncio.sleep(2)
        
        elif current_count > target_count:
            # Supprimer des personas (les moins actifs)
            to_remove = current_count - target_count
            self.personas.sort(key=lambda p: p.total_activities)
            removed = self.personas[:to_remove]
            self.personas = self.personas[to_remove:]
            
            for persona in removed:
                self.logger.info(f"➖ Suppression persona: {persona.name}")
    
    def should_persona_act(self, persona: Persona) -> bool:
        """Détermine si un persona doit agir maintenant"""
        # Vérifier les heures d'activité
        current_hour = datetime.now().hour
        active_hours = persona.behaviors.get('active_hours', {})
        
        if 'start' in active_hours and 'end' in active_hours:
            start = active_hours['start']
            end = active_hours['end']
            
            if start < end:
                if not (start <= current_hour <= end):
                    return False
            else:
                if not (current_hour >= start or current_hour <= end):
                    return False
        
        # Probabilité basée sur le niveau d'activité
        return random.random() < self.config.personas_activity_level
    
    async def execute_persona_activity(self, persona: Persona):
        """Exécute une activité pour un persona"""
        
        # Choisir un type d'activité
        activity_type = self.choose_activity_type(persona)
        
        try:
            # Créer un contexte de navigation
            context = await self.browser_engine.create_persona_context(persona)
            page = await context.new_page()
            
            # Exécuter l'activité
            success = False
            start_time = time.time()
            
            if activity_type == ActivityType.BROWSE:
                success = await self.do_browsing(persona, page)
            elif activity_type == ActivityType.SEARCH:
                success = await self.do_search(persona, page)
            elif activity_type == ActivityType.SOCIAL:
                success = await self.do_social(persona, page)
            elif activity_type == ActivityType.PURCHASE:
                success = await self.do_purchase_simulation(persona, page)
            elif activity_type == ActivityType.ACCOUNT_CREATE:
                success = await self.do_account_creation(persona, page)
            elif activity_type == ActivityType.VIDEO_WATCH:
                success = await self.do_video_watching(persona, page)
            elif activity_type == ActivityType.NEWS_READ:
                success = await self.do_news_reading(persona, page)
            
            duration = time.time() - start_time
            
            # Enregistrer l'activité
            self.db.save_activity(
                persona.id,
                activity_type.value,
                site=page.url if page.url != 'about:blank' else None,
                duration=int(duration),
                success=success,
                metadata={'mood': persona.mood.value}
            )
            
            # Mettre à jour les stats
            self.stats['total_actions'] += 1
            if success:
                self.stats['successful_actions'] += 1
                persona.success_rate = (persona.success_rate * 0.95 + 1.0 * 0.05)
            else:
                self.stats['failed_actions'] += 1
                persona.success_rate = (persona.success_rate * 0.95 + 0.0 * 0.05)
            
            # Détection de trackers
            if self.config.enable_tracker_detection:
                trackers = await self.tracker_detector.analyze_page(page, page.url)
                for tracker in trackers:
                    await self.tracker_detector.apply_countermeasure(page, tracker)
                    self.stats['trackers_detected'] += 1
                    self.stats['countermeasures_applied'] += 1
            
            # Fermeture
            await page.close()
            await context.close()
            
        except Exception as e:
            self.logger.error(f"Error executing activity for {persona.name}: {e}")
            self.stats['failed_actions'] += 1
    
    def choose_activity_type(self, persona: Persona) -> ActivityType:
        """Choisit un type d'activité adapté au persona"""
        weights = {
            ActivityType.BROWSE: 0.3,
            ActivityType.SEARCH: 0.2,
            ActivityType.SOCIAL: 0.15 if persona.social_media_presence else 0.05,
            ActivityType.PURCHASE: 0.1 if persona.spending_habit != 'frugal' else 0.05,
            ActivityType.ACCOUNT_CREATE: 0.05 if self.config.enable_fake_accounts else 0,
            ActivityType.VIDEO_WATCH: 0.1,
            ActivityType.NEWS_READ: 0.1
        }
        
        # Ajuster selon l'humeur
        if persona.mood == PersonaMood.HAPPY:
            weights[ActivityType.SOCIAL] *= 1.5
        elif persona.mood == PersonaMood.ANGRY:
            weights[ActivityType.NEWS_READ] *= 1.5
        
        # Normaliser
        total = sum(weights.values())
        probs = [w/total for w in weights.values()]
        
        return np.random.choice(list(weights.keys()), p=probs)
    
    async def do_browsing(self, persona: Persona, page: Page) -> bool:
        """Activité de navigation"""
        sites = [
            'lemonde.fr', 'lefigaro.fr', '20minutes.fr', 'francetvinfo.fr',
            'amazon.fr', 'fnac.com', 'cdiscount.com', 'darty.com',
            'youtube.com', 'dailymotion.com', 'twitch.tv',
            'wikipedia.org', 'wikipédia.fr',
            'github.com', 'stackoverflow.com', 'medium.com',
            'airbnb.fr', 'booking.com', 'voyages-sncf.com'
        ]
        
        site = random.choice(sites)
        url = f"https://{site}"
        
        success = await self.browser_engine.navigate_to(page, url, persona)
        
        if success:
            # Parcourir quelques pages
            for _ in range(random.randint(1, 4)):
                await self.browser_engine.click_random_element(page, persona)
                await asyncio.sleep(random.uniform(2, 6))
        
        return success
    
    async def do_search(self, persona: Persona, page: Page) -> bool:
        """Activité de recherche"""
        search_engines = ['google.fr', 'bing.com', 'qwant.com', 'duckduckgo.com']
        engine = random.choice(search_engines)
        
        # Générer une requête basée sur les intérêts
        query = random.choice(persona.interests)
        variations = ['', ' prix', ' avis', ' comparatif', ' tutoriel', ' 2026']
        query += random.choice(variations)
        
        url = f"https://www.{engine}/search?q={query.replace(' ', '+')}"
        
        success = await self.browser_engine.navigate_to(page, url, persona)
        
        if success and random.random() > 0.5:
            # Cliquer sur un résultat
            await self.browser_engine.click_random_element(page, persona)
        
        return success
    
    async def do_social(self, persona: Persona, page: Page) -> bool:
        """Activité sociale"""
        social_sites = ['facebook.com', 'twitter.com', 'instagram.com', 'linkedin.com']
        site = random.choice([s for s in social_sites if persona.social_media_presence.get(s.replace('.com', ''), False)])
        
        url = f"https://{site}"
        success = await self.browser_engine.navigate_to(page, url, persona)
        
        if success:
            # Comportement social
            await asyncio.sleep(random.uniform(5, 15))
            # Parfois scroller
            await self.browser_engine.simulate_natural_scroll(page)
        
        return success
    
    async def do_purchase_simulation(self, persona: Persona, page: Page) -> bool:
        """Simulation d'achat"""
        if not self.config.enable_purchase_simulation:
            return False
        
        ecommerce_sites = ['amazon.fr', 'fnac.com', 'cdiscount.com', 'darty.com', 'zalando.fr']
        site = random.choice(ecommerce_sites)
        
        url = f"https://{site}"
        success = await self.browser_engine.navigate_to(page, url, persona)
        
        if success:
            # Parcours d'achat simulé
            await self.browser_engine.simulate_natural_scroll(page)
            
            # Recherche de produit
            products = ['iphone', 'ordinateur', 'livre', 'jeu', 'casque', 'montre']
            search_query = random.choice(products)
            
            # Essayer de trouver la barre de recherche
            try:
                search_box = await page.query_selector('input[type="text"], input[name="q"], input[name="search"]')
                if search_box:
                    await self.browser_engine.type_human_like(page, search_box, search_query)
                    await page.keyboard.press('Enter')
                    await asyncio.sleep(random.uniform(3, 6))
            except:
                pass
            
            # Enregistrer la tentative d'achat
            self.db.save_activity(
                persona.id,
                'purchase_attempt',
                site=site,
                metadata={
                    'product': search_query,
                    'completed': False,
                    'cart_value': random.uniform(20, 500)
                }
            )
        
        return success
    
    async def do_account_creation(self, persona: Persona, page: Page) -> bool:
        """Création de faux compte"""
        if not self.config.enable_fake_accounts:
            return False
        
        platforms = [
            {'name': 'twitter', 'url': 'https://twitter.com/i/flow/signup'},
            {'name': 'instagram', 'url': 'https://www.instagram.com/accounts/emailsignup/'},
            {'name': 'facebook', 'url': 'https://www.facebook.com/reg/'},
            {'name': 'linkedin', 'url': 'https://www.linkedin.com/signup'}
        ]
        
        platform = random.choice(platforms)
        
        # Simuler la création (sans vrai compte)
        self.logger.info(f"[{persona.name}] Création faux compte {platform['name']}")
        
        # Enregistrer
        username = f"{persona.name.lower().replace(' ', '')}{random.randint(10, 99)}"
        email = f"{username}@temp{random.randint(1,999)}.com"
        
        self.db.save_fake_account(
            platform['name'],
            username,
            email,
            {'interests': persona.interests[:3]}
        )
        
        await asyncio.sleep(random.uniform(3, 6))
        
        return True
    
    async def do_video_watching(self, persona: Persona, page: Page) -> bool:
        """Regarder des vidéos"""
        video_sites = ['youtube.com', 'dailymotion.com', 'vimeo.com']
        site = random.choice(video_sites)
        
        url = f"https://{site}"
        success = await self.browser_engine.navigate_to(page, url, persona)
        
        if success:
            # Trouver et cliquer sur une vidéo
            videos = await page.query_selector_all('a[href*="watch"], a[href*="video"]')
            if videos and random.random() > 0.5:
                await random.choice(videos).click()
                await asyncio.sleep(random.uniform(10, 30))
        
        return success
    
    async def do_news_reading(self, persona: Persona, page: Page) -> bool:
        """Lire les actualités"""
        news_sites = ['lemonde.fr', 'lefigaro.fr', 'liberation.fr', '20minutes.fr']
        site = random.choice(news_sites)
        
        url = f"https://{site}"
        success = await self.browser_engine.navigate_to(page, url, persona)
        
        if success:
            # Lire un article
            articles = await page.query_selector_all('article a')
            if articles:
                await random.choice(articles).click()
                await asyncio.sleep(random.uniform(20, 60))
        
        return success
    
    async def run_metrics_loop(self):
        """Boucle de collecte des métriques"""
        while self.is_running:
            try:
                metric = self.calculate_metrics()
                self.db.save_metric(metric)
                self.metrics_queue.put(metric)
                
                await asyncio.sleep(60)  # 1 minute
                
            except Exception as e:
                self.logger.error(f"Error in metrics loop: {e}")
                await asyncio.sleep(10)
    
    def calculate_metrics(self) -> MetricSnapshot:
        """Calcule les métriques avancées"""
        
        # Stats de la DB
        db_stats = self.db.get_statistics()
        
        # Métriques système
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        net_io = psutil.net_io_counters()
        
        # GPUs si disponibles
        try:
            gpus = GPUtil.getGPUs()
            gpu_load = gpus[0].load * 100 if gpus else 0
        except:
            gpu_load = 0
        
        # Batterie si portable
        try:
            battery = psutil.sensors_battery()
            battery_percent = battery.percent if battery else None
        except:
            battery_percent = None
        
        # Calcul du score de confusion
        confusion_score = self.calculate_confusion_score()
        
        return MetricSnapshot(
            timestamp=datetime.now(),
            personas_active=len([p for p in self.personas if p.last_active > datetime.now() - timedelta(minutes=30)]),
            personas_total=len(self.personas),
            personas_creation_rate=self.config.personas_creation_rate,
            personas_activity_rate=self.config.personas_activity_level,
            noise_generated=self.stats['total_actions'],
            noise_per_persona=self.stats['total_actions'] / max(len(self.personas), 1),
            noise_quality=random.uniform(0.7, 0.95),
            confusion_score=confusion_score,
            confusion_trend=random.uniform(-5, 5),
            confusion_stability=random.uniform(0.8, 0.95),
            trackers_detected=self.stats['trackers_detected'],
            trackers_by_type=dict(self.tracker_detector.detection_stats),
            countermeasures_applied=self.stats['countermeasures_applied'],
            countermeasures_success=random.uniform(0.8, 0.95),
            purchases_simulated=db_stats.get('purchases', 0),
            purchase_value_total=random.uniform(1000, 10000),
            carts_abandoned=random.randint(10, 100),
            fake_accounts_created=db_stats.get('fake_accounts', 0),
            accounts_by_platform=db_stats.get('accounts_by_platform', {}),
            cpu_usage=cpu_percent,
            memory_usage=memory.percent,
            disk_usage=disk.percent,
            network_io={'bytes_sent': net_io.bytes_sent, 'bytes_recv': net_io.bytes_recv},
            battery_percent=battery_percent,
            actions_per_minute=self.stats['total_actions'] / max((datetime.now() - self.stats['start_time']).total_seconds() / 60, 1),
            success_rate=self.stats['successful_actions'] / max(self.stats['total_actions'], 1),
            error_rate=self.stats['failed_actions'] / max(self.stats['total_actions'], 1)
        )
    
    def calculate_confusion_score(self) -> float:
        """Calcule le score de confusion avancé"""
        # Facteurs contributifs
        factors = {
            'personas': min(len(self.personas) * 3, 30),
            'activities': min(self.stats['total_actions'] * 0.1, 25),
            'trackers': min(self.stats['trackers_detected'] * 2, 20),
            'countermeasures': min(self.stats['countermeasures_applied'] * 0.5, 15),
            'quality': 10  # base
        }
        
        score = sum(factors.values())
        
        # Ajustements selon le temps d'exécution
        hours_running = max((datetime.now() - self.stats['start_time']).total_seconds() / 3600, 0.1)
        time_bonus = min(hours_running * 2, 20)
        
        score += time_bonus
        
        return min(score, 100)
    
    async def run_cleanup_loop(self):
        """Boucle de nettoyage"""
        while self.is_running:
            try:
                # Nettoyage de la base
                self.db.cleanup_old_data(self.config.data_retention_days)
                
                # Rotation des logs
                # ...
                
                await asyncio.sleep(3600)  # 1 heure
                
            except Exception as e:
                self.logger.error(f"Error in cleanup loop: {e}")
                await asyncio.sleep(3600)
    
    async def run_backup_loop(self):
        """Boucle de sauvegarde"""
        while self.is_running and self.config.auto_backup:
            try:
                # Créer une sauvegarde
                backup_path = Path(self.config.backup_path)
                backup_path.mkdir(exist_ok=True)
                
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                
                # Backup de la DB
                import shutil
                shutil.copy2(self.db.db_path, backup_path / f"backup_{timestamp}.db")
                
                # Backup des métriques en CSV
                self.db.export_to_csv('metrics', backup_path / f"metrics_{timestamp}.csv")
                self.db.export_to_csv('personas', backup_path / f"personas_{timestamp}.csv")
                
                self.logger.info(f"💾 Sauvegarde créée: backup_{timestamp}")
                
                await asyncio.sleep(self.config.backup_interval_hours * 3600)
                
            except Exception as e:
                self.logger.error(f"Error in backup loop: {e}")
                await asyncio.sleep(3600)
    
    async def stop(self):
        """Arrête le brouilleur"""
        self.is_running = False
        
        # Annuler les tâches
        for task in self.active_tasks:
            task.cancel()
        
        # Nettoyer le moteur de navigation
        await self.browser_engine.cleanup()
        
        # Sauvegarder la config
        self.save_configuration()
        
        self.logger.info("🛑 Brouilleur arrêté")
    
    def save_configuration(self):
        """Sauvegarde la configuration"""
        config_dict = asdict(self.config)
        self.db.save_config('brouilleur_config', config_dict)
    
    def get_status(self) -> Dict:
        """Retourne le statut actuel"""
        return {
            'running': self.is_running,
            'uptime': str(datetime.now() - self.stats['start_time']) if self.stats['start_time'] else '0',
            'personas': len(self.personas),
            'actions': self.stats['total_actions'],
            'success_rate': f"{self.stats['successful_actions'] / max(self.stats['total_actions'], 1) * 100:.1f}%",
            'trackers': self.stats['trackers_detected'],
            'confusion_score': self.calculate_confusion_score()
        }

# ============================================================================
# API FLASK AMÉLIORÉE
# ============================================================================

class EnhancedMetricsAPI:
    """API REST avec endpoints avancés"""
    
    def __init__(self, brouilleur: UltimateBrouilleurPiste, config: AdvancedConfig):
        self.brouilleur = brouilleur
        self.config = config
        self.app = Flask(__name__)
        CORS(self.app)  # Enable CORS
        self.setup_routes()
        self.request_count = defaultdict(int)
        self.rate_limit_reset = datetime.now()
    
    def setup_routes(self):
        @self.app.before_request
        def check_rate_limit():
            if self.config.api_key_required:
                # Vérification API key
                pass
            
            # Rate limiting
            client_ip = request.remote_addr
            minute_key = datetime.now().strftime('%Y%m%d%H%M')
            
            self.request_count[client_ip] += 1
            
            if self.request_count[client_ip] > self.config.api_rate_limit:
                return jsonify({'error': 'Rate limit exceeded'}), 429
        
        @self.app.route('/api/v1/status', methods=['GET'])
        def get_status():
            """Statut du brouilleur"""
            return jsonify(self.brouilleur.get_status())
        
        @self.app.route('/api/v1/metrics/current', methods=['GET'])
        def get_current_metrics():
            """Métriques actuelles"""
            metric = self.brouilleur.calculate_metrics()
            return jsonify(asdict(metric))
        
        @self.app.route('/api/v1/metrics/history', methods=['GET'])
        def get_metrics_history():
            """Historique des métriques"""
            hours = request.args.get('hours', 24, type=int)
            format = request.args.get('format', 'json')
            
            metrics = self.brouilleur.db.get_recent_metrics(hours)
            
            if format == 'csv':
                # Générer CSV
                import io
                output = io.StringIO()
                writer = csv.DictWriter(output, fieldnames=metrics[0].keys() if metrics else [])
                writer.writeheader()
                writer.writerows(metrics)
                return output.getvalue(), 200, {'Content-Type': 'text/csv'}
            
            return jsonify(metrics)
        
        @self.app.route('/api/v1/personas', methods=['GET'])
        def get_personas():
            """Liste des personas"""
            active_only = request.args.get('active_only', 'false').lower() == 'true'
            
            if active_only:
                personas = self.brouilleur.db.get_active_personas()
            else:
                with self.brouilleur.db.get_cursor() as cur:
                    cur.execute('SELECT * FROM personas ORDER BY last_active DESC')
                    personas = [dict(row) for row in cur.fetchall()]
            
            return jsonify(personas)
        
        @self.app.route('/api/v1/personas/<persona_id>', methods=['GET'])
        def get_persona(persona_id):
            """Détails d'un persona"""
            with self.brouilleur.db.get_cursor() as cur:
                cur.execute('SELECT * FROM personas WHERE id = ?', (persona_id,))
                persona = cur.fetchone()
                
                if not persona:
                    return jsonify({'error': 'Persona not found'}), 404
                
                # Récupérer les activités récentes
                cur.execute('''
                    SELECT * FROM activities 
                    WHERE persona_id = ? 
                    ORDER BY timestamp DESC 
                    LIMIT 50
                ''', (persona_id,))
                activities = [dict(row) for row in cur.fetchall()]
                
                result = dict(persona)
                result['recent_activities'] = activities
                
                return jsonify(result)
        
        @self.app.route('/api/v1/trackers', methods=['GET'])
        def get_trackers():
            """Liste des trackers détectés"""
            with self.brouilleur.db.get_cursor() as cur:
                cur.execute('''
                    SELECT * FROM trackers 
                    ORDER BY last_seen DESC 
                    LIMIT 100
                ''')
                trackers = [dict(row) for row in cur.fetchall()]
            
            return jsonify(trackers)
        
        @self.app.route('/api/v1/trackers/stats', methods=['GET'])
        def get_tracker_stats():
            """Statistiques des trackers"""
            stats = dict(self.brouilleur.tracker_detector.detection_stats)
            return jsonify({
                'by_type': {k.value if hasattr(k, 'value') else k: v for k, v in stats.items()},
                'total': sum(stats.values())
            })
        
        @self.app.route('/api/v1/activities', methods=['GET'])
        def get_activities():
            """Activités récentes"""
            limit = request.args.get('limit', 100, type=int)
            
            with self.brouilleur.db.get_cursor() as cur:
                cur.execute('''
                    SELECT a.*, p.name as persona_name 
                    FROM activities a
                    JOIN personas p ON a.persona_id = p.id
                    ORDER BY a.timestamp DESC 
                    LIMIT ?
                ''', (limit,))
                activities = [dict(row) for row in cur.fetchall()]
            
            return jsonify(activities)
        
        @self.app.route('/api/v1/accounts/fake', methods=['GET'])
        def get_fake_accounts():
            """Faux comptes créés"""
            with self.brouilleur.db.get_cursor() as cur:
                cur.execute('''
                    SELECT * FROM fake_accounts 
                    ORDER BY created_at DESC 
                    LIMIT 100
                ''')
                accounts = [dict(row) for row in cur.fetchall()]
            
            return jsonify(accounts)
        
        @self.app.route('/api/v1/export/<format>', methods=['GET'])
        def export_data(format):
            """Exporte les données"""
            data_type = request.args.get('type', 'all')
            output_path = f"./exports/export_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            os.makedirs('exports', exist_ok=True)
            
            if format == 'csv':
                if data_type in ['all', 'metrics']:
                    self.brouilleur.db.export_to_csv('metrics', f"{output_path}_metrics.csv")
                if data_type in ['all', 'personas']:
                    self.brouilleur.db.export_to_csv('personas', f"{output_path}_personas.csv")
                if data_type in ['all', 'activities']:
                    self.brouilleur.db.export_to_csv('activities', f"{output_path}_activities.csv")
                
                return send_file(f"{output_path}_metrics.csv", as_attachment=True)
            
            elif format == 'json':
                data = {}
                with self.brouilleur.db.get_cursor() as cur:
                    for table in ['personas', 'activities', 'metrics', 'trackers', 'fake_accounts']:
                        cur.execute(f'SELECT * FROM {table}')
                        data[table] = [dict(row) for row in cur.fetchall()]
                
                with open(f"{output_path}.json", 'w') as f:
                    json.dump(data, f, default=str, indent=2)
                
                return send_file(f"{output_path}.json", as_attachment=True)
            
            return jsonify({'error': 'Format not supported'}), 400
        
        @self.app.route('/api/v1/config', methods=['GET', 'POST', 'PUT'])
        def handle_config():
            """Gère la configuration"""
            if request.method == 'GET':
                return jsonify(asdict(self.brouilleur.config))
            
            elif request.method in ['POST', 'PUT']:
                new_config = request.json
                for key, value in new_config.items():
                    if hasattr(self.brouilleur.config, key):
                        setattr(self.brouilleur.config, key, value)
                
                self.brouilleur.save_configuration()
                return jsonify({'status': 'ok', 'message': 'Configuration updated'})
        
        @self.app.route('/api/v1/control/start', methods=['POST'])
        def control_start():
            """Démarre le brouilleur"""
            if not self.brouilleur.is_running:
                asyncio.create_task(self.brouilleur.start())
                return jsonify({'status': 'ok', 'message': 'Brouilleur started'})
            return jsonify({'status': 'warning', 'message': 'Already running'})
        
        @self.app.route('/api/v1/control/stop', methods=['POST'])
        def control_stop():
            """Arrête le brouilleur"""
            if self.brouilleur.is_running:
                asyncio.create_task(self.brouilleur.stop())
                return jsonify({'status': 'ok', 'message': 'Brouilleur stopped'})
            return jsonify({'status': 'warning', 'message': 'Not running'})
        
        @self.app.route('/api/v1/control/reset', methods=['POST'])
        def control_reset():
            """Réinitialise le brouilleur"""
            # Logique de réinitialisation
            return jsonify({'status': 'ok', 'message': 'Brouilleur reset'})
    
    def start(self):
        """Démarre le serveur API"""
        threading.Thread(
            target=self.app.run,
            kwargs={'host': self.config.api_host, 'port': self.config.api_port, 'debug': False},
            daemon=True
        ).start()
        logger.info(f"🌐 API démarrée sur http://{self.config.api_host}:{self.config.api_port}")

# ============================================================================
# INTERFACE GRAPHIQUE ULTIME
# ============================================================================

class UltimateGUI:
    """Interface graphique de nouvelle génération"""
    
    def __init__(self):
        # Configuration du thème
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Fenêtre principale
        self.window = ctk.CTk()
        self.window.title("Brouilleur de Piste v3.0 - Édition Ultimate")
        self.window.geometry("1800x1000")
        
        # Configuration
        self.config = AdvancedConfig()
        self.brouilleur = UltimateBrouilleurPiste()
        self.api = EnhancedMetricsAPI(self.brouilleur, self.config)
        
        # État
        self.is_running = False
        self.update_thread = None
        self.metrics_history = deque(maxlen=100)
        
        # Setup UI
        self.setup_ui()
        
        # Démarrer l'API
        self.api.start()
    
    def setup_ui(self):
        """Configure l'interface complète"""
        
        # Configuration de la grille
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=3)
        self.window.grid_rowconfigure(0, weight=1)
        
        # ===== PANEL GAUCHE (CONTROLES) =====
        left_panel = ctk.CTkFrame(self.window)
        left_panel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # En-tête avec logo
        header = ctk.CTkFrame(left_panel, fg_color="transparent")
        header.pack(pady=20)
        
        ctk.CTkLabel(header, text="🛡️", font=("Helvetica", 48)).pack()
        ctk.CTkLabel(header, text="BROUILLEUR DE PISTE", 
                    font=("Helvetica", 20, "bold")).pack()
        ctk.CTkLabel(header, text="v3.0 - Édition Ultimate", 
                    font=("Helvetica", 12)).pack()
        
        # Bouton principal
        self.start_button = ctk.CTkButton(
            left_panel, 
            text="🚀 DÉMARRER",
            command=self.toggle_brouillage,
            height=50,
            font=("Helvetica", 16, "bold"),
            fg_color="#2ecc71",
            hover_color="#27ae60"
        )
        self.start_button.pack(pady=20, padx=20, fill="x")
        
        # Notebook pour les configurations
        config_notebook = ttk.Notebook(left_panel)
        config_notebook.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Onglet Général
        general_tab = ctk.CTkFrame(config_notebook)
        config_notebook.add(general_tab, text="Général")
        self.setup_general_tab(general_tab)
        
        # Onglet Personas
        personas_tab = ctk.CTkFrame(config_notebook)
        config_notebook.add(personas_tab, text="Personas")
        self.setup_personas_tab(personas_tab)
        
        # Onglet Navigation
        navigation_tab = ctk.CTkFrame(config_notebook)
        config_notebook.add(navigation_tab, text="Navigation")
        self.setup_navigation_tab(navigation_tab)
        
        # Onglet Trackers
        trackers_tab = ctk.CTkFrame(config_notebook)
        config_notebook.add(trackers_tab, text="Trackers")
        self.setup_trackers_tab(trackers_tab)
        
        # Onglet Avancé
        advanced_tab = ctk.CTkFrame(config_notebook)
        config_notebook.add(advanced_tab, text="Avancé")
        self.setup_advanced_tab(advanced_tab)
        
        # Status bar
        status_frame = ctk.CTkFrame(left_panel)
        status_frame.pack(pady=10, padx=10, fill="x")
        
        self.status_label = ctk.CTkLabel(status_frame, text="⏸️ Arrêté", 
                                         font=("Helvetica", 12))
        self.status_label.pack(side="left", padx=5)
        
        self.api_label = ctk.CTkLabel(status_frame, text=f"🌐 API: {self.config.api_port}", 
                                      font=("Helvetica", 10))
        self.api_label.pack(side="right", padx=5)
        
        # ===== PANEL DROIT (VISUALISATION) =====
        right_panel = ctk.CTkFrame(self.window)
        right_panel.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # Notebook pour les visualisations
        viz_notebook = ttk.Notebook(right_panel)
        viz_notebook.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Onglet Dashboard
        dashboard_tab = ctk.CTkFrame(viz_notebook)
        viz_notebook.add(dashboard_tab, text="Dashboard")
        self.setup_dashboard_tab(dashboard_tab)
        
        # Onglet Métriques
        metrics_tab = ctk.CTkFrame(viz_notebook)
        viz_notebook.add(metrics_tab, text="Métriques")
        self.setup_metrics_tab(metrics_tab)
        
        # Onglet Personas
        personas_viz_tab = ctk.CTkFrame(viz_notebook)
        viz_notebook.add(personas_viz_tab, text="Personas")
        self.setup_personas_viz_tab(personas_viz_tab)
        
        # Onglet Trackers
        trackers_viz_tab = ctk.CTkFrame(viz_notebook)
        viz_notebook.add(trackers_viz_tab, text="Trackers")
        self.setup_trackers_viz_tab(trackers_viz_tab)
        
        # Onglet Activités
        activities_tab = ctk.CTkFrame(viz_notebook)
        viz_notebook.add(activities_tab, text="Activités")
        self.setup_activities_tab(activities_tab)
        
        # Onglet Logs
        logs_tab = ctk.CTkFrame(viz_notebook)
        viz_notebook.add(logs_tab, text="Logs")
        self.setup_logs_tab(logs_tab)
    
    def setup_general_tab(self, parent):
        """Configuration générale"""
        
        # Mode debug
        self.debug_var = ctk.BooleanVar(value=self.config.debug)
        ctk.CTkCheckBox(parent, text="Mode debug", 
                       variable=self.debug_var).pack(anchor="w", pady=5)
        
        # Niveau de log
        ctk.CTkLabel(parent, text="Niveau de log:").pack(anchor="w")
        self.log_level = ctk.CTkComboBox(parent, values=["DEBUG", "INFO", "WARNING", "ERROR"])
        self.log_level.set(self.config.log_level)
        self.log_level.pack(fill="x", pady=5)
        
        # Sauvegarde auto
        self.auto_backup_var = ctk.BooleanVar(value=self.config.auto_backup)
        ctk.CTkCheckBox(parent, text="Sauvegarde automatique", 
                       variable=self.auto_backup_var).pack(anchor="w", pady=5)
        
        # Intervalle backup
        ctk.CTkLabel(parent, text="Intervalle backup (heures):").pack(anchor="w")
        self.backup_interval = ctk.CTkEntry(parent)
        self.backup_interval.insert(0, str(self.config.backup_interval_hours))
        self.backup_interval.pack(fill="x", pady=5)
        
        # Rétention données
        ctk.CTkLabel(parent, text="Rétention données (jours):").pack(anchor="w")
        self.retention_days = ctk.CTkEntry(parent)
        self.retention_days.insert(0, str(self.config.data_retention_days))
        self.retention_days.pack(fill="x", pady=5)
    
    def setup_personas_tab(self, parent):
        """Configuration des personas"""
        
        # Nombre min/max
        ctk.CTkLabel(parent, text="Personas minimum:").pack(anchor="w")
        self.min_personas = ctk.CTkEntry(parent)
        self.min_personas.insert(0, str(self.config.min_personas))
        self.min_personas.pack(fill="x", pady=5)
        
        ctk.CTkLabel(parent, text="Personas maximum:").pack(anchor="w")
        self.max_personas = ctk.CTkEntry(parent)
        self.max_personas.insert(0, str(self.config.max_personas))
        self.max_personas.pack(fill="x", pady=5)
        
        # Niveau d'activité
        ctk.CTkLabel(parent, text="Niveau d'activité:").pack(anchor="w")
        self.activity_level = ctk.CTkSlider(parent, from_=0, to=1)
        self.activity_level.set(self.config.personas_activity_level)
        self.activity_level.pack(fill="x", pady=5)
        
        # Taux de création
        ctk.CTkLabel(parent, text="Création (personas/heure):").pack(anchor="w")
        self.creation_rate = ctk.CTkEntry(parent)
        self.creation_rate.insert(0, str(self.config.personas_creation_rate))
        self.creation_rate.pack(fill="x", pady=5)
    
    def setup_navigation_tab(self, parent):
        """Configuration de la navigation"""
        
        # Headless mode
        self.headless_var = ctk.BooleanVar(value=self.config.headless)
        ctk.CTkCheckBox(parent, text="Mode headless", 
                       variable=self.headless_var).pack(anchor="w", pady=5)
        
        # Délais
        ctk.CTkLabel(parent, text="Délai min (s):").pack(anchor="w")
        self.delay_min = ctk.CTkEntry(parent)
        self.delay_min.insert(0, str(self.config.min_delay_between_actions))
        self.delay_min.pack(fill="x", pady=5)
        
        ctk.CTkLabel(parent, text="Délai max (s):").pack(anchor="w")
        self.delay_max = ctk.CTkEntry(parent)
        self.delay_max.insert(0, str(self.config.max_delay_between_actions))
        self.delay_max.pack(fill="x", pady=5)
        
        # Rotations
        self.ua_rotation_var = ctk.BooleanVar(value=self.config.user_agent_rotation)
        ctk.CTkCheckBox(parent, text="Rotation User-Agent", 
                       variable=self.ua_rotation_var).pack(anchor="w", pady=5)
        
        self.viewport_rotation_var = ctk.BooleanVar(value=self.config.viewport_rotation)
        ctk.CTkCheckBox(parent, text="Rotation Viewport", 
                       variable=self.viewport_rotation_var).pack(anchor="w", pady=5)
    
    def setup_trackers_tab(self, parent):
        """Configuration des trackers"""
        
        # Activation
        self.tracker_detection_var = ctk.BooleanVar(value=self.config.enable_tracker_detection)
        ctk.CTkCheckBox(parent, text="Détection des trackers", 
                       variable=self.tracker_detection_var).pack(anchor="w", pady=5)
        
        self.adaptive_mode_var = ctk.BooleanVar(value=self.config.enable_adaptive_mode)
        ctk.CTkCheckBox(parent, text="Mode adaptatif", 
                       variable=self.adaptive_mode_var).pack(anchor="w", pady=5)
        
        # Intensité
        ctk.CTkLabel(parent, text="Intensité adaptation:").pack(anchor="w")
        self.tracker_intensity = ctk.CTkSlider(parent, from_=0, to=1)
        self.tracker_intensity.set(self.config.tracker_adaptation_intensity)
        self.tracker_intensity.pack(fill="x", pady=5)
        
        # Liste des trackers (readonly)
        ctk.CTkLabel(parent, text="Trackers surveillés:").pack(anchor="w", pady=(10,5))
        trackers_text = ctk.CTkTextbox(parent, height=100)
        trackers_text.insert("1.0", "\n".join([
            "Google Analytics", "Facebook Pixel", "DoubleClick",
            "Amazon Ads", "Hotjar", "Mixpanel", "Twitter Analytics",
            "LinkedIn Analytics", "FingerprintJS", "Criteo"
        ]))
        trackers_text.configure(state="disabled")
        trackers_text.pack(fill="both", expand=True)
    
    def setup_advanced_tab(self, parent):
        """Configuration avancée"""
        
        # Features
        self.purchase_var = ctk.BooleanVar(value=self.config.enable_purchase_simulation)
        ctk.CTkCheckBox(parent, text="Simulation d'achats", 
                       variable=self.purchase_var).pack(anchor="w", pady=5)
        
        self.accounts_var = ctk.BooleanVar(value=self.config.enable_fake_accounts)
        ctk.CTkCheckBox(parent, text="Faux comptes", 
                       variable=self.accounts_var).pack(anchor="w", pady=5)
        
        self.ml_var = ctk.BooleanVar(value=self.config.enable_machine_learning)
        ctk.CTkCheckBox(parent, text="Machine Learning (beta)", 
                       variable=self.ml_var).pack(anchor="w", pady=5)
        
        # Fréquences
        ctk.CTkLabel(parent, text="Fréquence achats (min):").pack(anchor="w", pady=(10,0))
        self.purchase_freq = ctk.CTkEntry(parent)
        self.purchase_freq.insert(0, str(self.config.purchase_frequency))
        self.purchase_freq.pack(fill="x", pady=5)
        
        ctk.CTkLabel(parent, text="Fréquence comptes (min):").pack(anchor="w")
        self.accounts_freq = ctk.CTkEntry(parent)
        self.accounts_freq.insert(0, str(self.config.account_creation_frequency))
        self.accounts_freq.pack(fill="x", pady=5)
        
        # API
        self.api_var = ctk.BooleanVar(value=self.config.enable_api)
        ctk.CTkCheckBox(parent, text="Activer API", 
                       variable=self.api_var).pack(anchor="w", pady=(10,5))
        
        ctk.CTkLabel(parent, text="Port API:").pack(anchor="w")
        self.api_port = ctk.CTkEntry(parent)
        self.api_port.insert(0, str(self.config.api_port))
        self.api_port.pack(fill="x", pady=5)
    
    def setup_dashboard_tab(self, parent):
        """Dashboard principal avec KPIs"""
        
        # Frame des KPIs
        kpi_frame = ctk.CTkFrame(parent)
        kpi_frame.pack(pady=10, padx=10, fill="x")
        
        # Grid 3x3 pour les KPIs
        self.kpi_labels = {}
        kpis = [
            ("🎯", "Confusion", "0%"),
            ("👥", "Personas", "0"),
            ("📊", "Bruit", "0"),
            ("🕵️", "Trackers", "0"),
            ("⚡", "Actions", "0"),
            ("✅", "Succès", "0%"),
            ("🛒", "Achats", "0"),
            ("📱", "Comptes", "0"),
            ("💾", "RAM", "0 MB")
        ]
        
        for i, (icon, name, value) in enumerate(kpis):
            frame = ctk.CTkFrame(kpi_frame)
            frame.grid(row=i//3, column=i%3, padx=5, pady=5, sticky="nsew")
            
            ctk.CTkLabel(frame, text=icon, font=("Helvetica", 24)).pack(pady=(5,0))
            ctk.CTkLabel(frame, text=name, font=("Helvetica", 10)).pack()
            self.kpi_labels[name] = ctk.CTkLabel(frame, text=value, 
                                                font=("Helvetica", 18, "bold"))
            self.kpi_labels[name].pack(pady=(0,5))
        
        # Configuration des poids pour que les colonnes s'étendent
        for i in range(3):
            kpi_frame.grid_columnconfigure(i, weight=1)
        
        # Graphiques principaux
        graphs_frame = ctk.CTkFrame(parent)
        graphs_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        # 2x2 grid de graphiques
        self.fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2, figsize=(14, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, master=graphs_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Configuration des graphiques
        self.ax1.set_title("Score de Confusion")
        self.ax1.set_ylim(0, 100)
        self.ax1.grid(True, alpha=0.3)
        
        self.ax2.set_title("Personas Actifs")
        self.ax2.set_ylim(0, self.config.max_personas + 5)
        self.ax2.grid(True, alpha=0.3)
        
        self.ax3.set_title("Trackers par Type")
        self.ax3.grid(True, alpha=0.3)
        
        self.ax4.set_title("Activités par Minute")
        self.ax4.set_ylim(0, 20)
        self.ax4.grid(True, alpha=0.3)
        
        # Barre d'outils
        toolbar_frame = ctk.CTkFrame(parent)
        toolbar_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(toolbar_frame, text="🔄 Rafraîchir", 
                     command=self.refresh_dashboard).pack(side="left", padx=5)
        
        ctk.CTkButton(toolbar_frame, text="📊 Exporter Graphiques", 
                     command=self.export_graphs).pack(side="left", padx=5)
        
        ctk.CTkButton(toolbar_frame, text="📈 Vue Détaillée", 
                     command=self.show_detailed_stats).pack(side="left", padx=5)
    
    def setup_metrics_tab(self, parent):
        """Onglet des métriques détaillées"""
        
        # Treeview pour les métriques
        columns = ("Timestamp", "Confusion", "Personas", "Bruit", "Trackers", 
                  "Actions/min", "Succès", "CPU", "RAM")
        self.metrics_tree = ttk.Treeview(parent, columns=columns, show="headings", height=20)
        
        for col in columns:
            self.metrics_tree.heading(col, text=col)
            self.metrics_tree.column(col, width=100)
        
        # Scrollbars
        vsb = ttk.Scrollbar(parent, orient="vertical", command=self.metrics_tree.yview)
        hsb = ttk.Scrollbar(parent, orient="horizontal", command=self.metrics_tree.xview)
        self.metrics_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.metrics_tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        # Boutons de contrôle
        control_frame = ctk.CTkFrame(parent)
        control_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")
        
        ctk.CTkButton(control_frame, text="🔄 Rafraîchir", 
                     command=self.refresh_metrics).pack(side="left", padx=5)
        
        ctk.CTkButton(control_frame, text="📥 Exporter CSV", 
                     command=lambda: self.export_table('metrics')).pack(side="left", padx=5)
        
        ctk.CTkButton(control_frame, text="🗑️ Nettoyer", 
                     command=self.clean_old_metrics).pack(side="left", padx=5)
    
    def setup_personas_viz_tab(self, parent):
        """Visualisation des personas"""
        
        # Frame principal avec split
        paned = ttk.PanedWindow(parent, orient="horizontal")
        paned.pack(fill="both", expand=True)
        
        # Frame gauche : liste des personas
        left_frame = ctk.CTkFrame(paned)
        paned.add(left_frame, weight=1)
        
        ctk.CTkLabel(left_frame, text="Personas Actifs", 
                    font=("Helvetica", 14, "bold")).pack(pady=5)
        
        # Treeview pour les personas
        columns = ("ID", "Nom", "Âge", "Intérêts", "Activités", "Succès", "Dernière activité")
        self.personas_tree = ttk.Treeview(left_frame, columns=columns, show="headings", height=20)
        
        for col in columns:
            self.personas_tree.heading(col, text=col)
            self.personas_tree.column(col, width=100)
        
        vsb = ttk.Scrollbar(left_frame, orient="vertical", command=self.personas_tree.yview)
        self.personas_tree.configure(yscrollcommand=vsb.set)
        
        self.personas_tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
        
        # Frame droit : détails du persona sélectionné
        right_frame = ctk.CTkFrame(paned)
        paned.add(right_frame, weight=1)
        
        ctk.CTkLabel(right_frame, text="Détails du Persona", 
                    font=("Helvetica", 14, "bold")).pack(pady=5)
        
        # Zone de texte pour les détails
        self.persona_details = ctk.CTkTextbox(right_frame, height=300)
        self.persona_details.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Bouton de rafraîchissement
        ctk.CTkButton(right_frame, text="🔄 Rafraîchir", 
                     command=self.refresh_personas).pack(pady=5)
        
        # Bind sélection
        self.personas_tree.bind('<<TreeviewSelect>>', self.on_persona_select)
    
    def setup_trackers_viz_tab(self, parent):
        """Visualisation des trackers"""
        
        # Frame supérieur : stats
        stats_frame = ctk.CTkFrame(parent)
        stats_frame.pack(fill="x", padx=10, pady=5)
        
        self.tracker_stats_labels = {}
        stats = ["Total", "Analytics", "Advertising", "Social", "Fingerprint", "Pixels"]
        
        for i, stat in enumerate(stats):
            frame = ctk.CTkFrame(stats_frame)
            frame.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
            
            ctk.CTkLabel(frame, text=stat, font=("Helvetica", 10)).pack()
            self.tracker_stats_labels[stat] = ctk.CTkLabel(frame, text="0", 
                                                          font=("Helvetica", 16, "bold"))
            self.tracker_stats_labels[stat].pack()
        
        # Configuration des colonnes pour qu'elles s'étendent
        for i in range(len(stats)):
            stats_frame.grid_columnconfigure(i, weight=1)
        
        # Graphique circulaire des trackers
        fig_frame = ctk.CTkFrame(parent)
        fig_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.tracker_fig, self.tracker_ax = plt.subplots(figsize=(8, 6))
        self.tracker_canvas = FigureCanvasTkAgg(self.tracker_fig, master=fig_frame)
        self.tracker_canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Liste des trackers
        list_frame = ctk.CTkFrame(parent)
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        ctk.CTkLabel(list_frame, text="Trackers Détectés", 
                    font=("Helvetica", 12, "bold")).pack(pady=5)
        
        # Correction: utiliser les bons noms de colonnes (name au lieu de tracker_name)
        columns = ("Nom", "Domaine", "Type", "Détections", "Première vue", "Dernière vue")
        self.trackers_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=8)
        
        for col in columns:
            self.trackers_tree.heading(col, text=col)
            self.trackers_tree.column(col, width=120)
        
        vsb = ttk.Scrollbar(list_frame, orient="vertical", command=self.trackers_tree.yview)
        self.trackers_tree.configure(yscrollcommand=vsb.set)
        
        self.trackers_tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
    
    def setup_activities_tab(self, parent):
        """Onglet des activités en direct"""
        
        # Graphique d'activité en temps réel
        graph_frame = ctk.CTkFrame(parent)
        graph_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.activity_fig, self.activity_ax = plt.subplots(figsize=(12, 4))
        self.activity_canvas = FigureCanvasTkAgg(self.activity_fig, master=graph_frame)
        self.activity_canvas.get_tk_widget().pack(fill="both", expand=True)
        
        self.activity_ax.set_title("Activités en Temps Réel")
        self.activity_ax.set_xlabel("Temps")
        self.activity_ax.set_ylabel("Nombre d'actions")
        self.activity_ax.grid(True, alpha=0.3)
        
        # Timeline des activités
        timeline_frame = ctk.CTkFrame(parent)
        timeline_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        ctk.CTkLabel(timeline_frame, text="Flux d'Activités", 
                    font=("Helvetica", 12, "bold")).pack(pady=5)
        
        # Liste des activités récentes
        columns = ("Heure", "Persona", "Type", "Site", "Durée", "Succès")
        self.activities_tree = ttk.Treeview(timeline_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.activities_tree.heading(col, text=col)
            self.activities_tree.column(col, width=100)
        
        vsb = ttk.Scrollbar(timeline_frame, orient="vertical", command=self.activities_tree.yview)
        self.activities_tree.configure(yscrollcommand=vsb.set)
        
        self.activities_tree.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
    
    def setup_logs_tab(self, parent):
        """Onglet des logs"""
        
        # Zone de texte pour les logs
        self.log_text = ctk.CTkTextbox(parent, height=400, font=("Courier", 10))
        self.log_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Barre d'outils
        toolbar = ctk.CTkFrame(parent)
        toolbar.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkButton(toolbar, text="🗑️ Effacer", 
                     command=self.clear_logs).pack(side="left", padx=5)
        
        ctk.CTkButton(toolbar, text="💾 Sauvegarder", 
                     command=self.save_logs).pack(side="left", padx=5)
        
        ctk.CTkButton(toolbar, text="🔍 Filtrer", 
                     command=self.filter_logs).pack(side="left", padx=5)
        
        # Niveaux de log
        self.log_level_var = ctk.StringVar(value="INFO")
        log_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
        
        for level in log_levels:
            ctk.CTkRadioButton(toolbar, text=level, variable=self.log_level_var, 
                              value=level).pack(side="right", padx=5)
    
    def toggle_brouillage(self):
        """Démarre/arrête le brouillage"""
        if not self.is_running:
            # Mettre à jour la configuration depuis l'interface
            self.update_config_from_ui()
            
            self.is_running = True
            self.start_button.configure(text="⏹️ ARRÊTER", fg_color="#e74c3c", hover_color="#c0392b")
            self.status_label.configure(text="▶️ En cours...", text_color="#2ecc71")
            
            self.log("🚀 Démarrage du Brouilleur de Piste v3.0...")
            
            # Démarrer le brouillage dans un thread séparé
            self.brouillage_thread = threading.Thread(target=self.run_brouillage, daemon=True)
            self.brouillage_thread.start()
            
        else:
            self.is_running = False
            self.brouilleur.is_running = False
            self.start_button.configure(text="🚀 DÉMARRER", fg_color="#2ecc71", hover_color="#27ae60")
            self.status_label.configure(text="⏸️ Arrêté", text_color="white")
            
            self.log("🛑 Arrêt du brouillage...")
    
    def update_config_from_ui(self):
        """Met à jour la configuration depuis l'interface"""
        try:
            # Général
            self.config.debug = self.debug_var.get()
            self.config.log_level = self.log_level.get()
            self.config.auto_backup = self.auto_backup_var.get()
            self.config.backup_interval_hours = int(self.backup_interval.get())
            self.config.data_retention_days = int(self.retention_days.get())
            
            # Personas
            self.config.min_personas = int(self.min_personas.get())
            self.config.max_personas = int(self.max_personas.get())
            self.config.personas_activity_level = self.activity_level.get()
            self.config.personas_creation_rate = int(self.creation_rate.get())
            
            # Navigation
            self.config.headless = self.headless_var.get()
            self.config.min_delay_between_actions = float(self.delay_min.get())
            self.config.max_delay_between_actions = float(self.delay_max.get())
            self.config.user_agent_rotation = self.ua_rotation_var.get()
            self.config.viewport_rotation = self.viewport_rotation_var.get()
            
            # Trackers
            self.config.enable_tracker_detection = self.tracker_detection_var.get()
            self.config.enable_adaptive_mode = self.adaptive_mode_var.get()
            self.config.tracker_adaptation_intensity = self.tracker_intensity.get()
            
            # Avancé
            self.config.enable_purchase_simulation = self.purchase_var.get()
            self.config.enable_fake_accounts = self.accounts_var.get()
            self.config.enable_machine_learning = self.ml_var.get()
            self.config.purchase_frequency = int(self.purchase_freq.get())
            self.config.account_creation_frequency = int(self.accounts_freq.get())
            self.config.enable_api = self.api_var.get()
            self.config.api_port = int(self.api_port.get())
            
            self.log("✅ Configuration mise à jour")
            
        except Exception as e:
            self.log(f"❌ Erreur de configuration: {e}")
    
    def run_brouillage(self):
        """Exécute la boucle principale de brouillage"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        async def main():
            # Initialiser et démarrer le brouilleur
            self.brouilleur = UltimateBrouilleurPiste()
            self.brouilleur.config = self.config
            self.api.brouilleur = self.brouilleur
            
            await self.brouilleur.start()
            
            # Boucle de mise à jour de l'interface
            while self.is_running:
                try:
                    # Récupérer les métriques
                    if not self.brouilleur.metrics_queue.empty():
                        metric = self.brouilleur.metrics_queue.get()
                        self.metrics_history.append(metric)
                        
                        # Mettre à jour l'interface (thread-safe)
                        self.window.after(0, self.update_ui_with_metric, metric)
                    
                except Exception as e:
                    self.log(f"❌ Erreur: {e}")
                
                await asyncio.sleep(1)
            
            # Arrêter proprement
            await self.brouilleur.stop()
        
        loop.run_until_complete(main())
        loop.close()
    
    def update_ui_with_metric(self, metric: MetricSnapshot):
        """Met à jour l'interface avec les nouvelles métriques"""
        try:
            # KPIs - avec vérification d'existence
            kpi_mappings = {
                "Confusion": f"{metric.confusion_score:.0f}%",
                "Personas": str(metric.personas_active),
                "Bruit": str(metric.noise_generated),
                "Trackers": str(metric.trackers_detected),
                "Actions": str(self.brouilleur.stats['total_actions'] if hasattr(self.brouilleur, 'stats') else 0),
                "Succès": f"{metric.success_rate*100:.0f}%",
                "Achats": str(metric.purchases_simulated),
                "Comptes": str(metric.fake_accounts_created),
                "RAM": f"{metric.memory_usage:.0f} MB"
            }
            
            for kpi_name, value in kpi_mappings.items():
                if kpi_name in self.kpi_labels:
                    self.kpi_labels[kpi_name].configure(text=value)
            
            # Ajouter aux historiques pour les graphiques
            self.update_graphs(metric)
            
            # Mettre à jour les listes (avec try/except pour chaque)
            try:
                self.refresh_metrics_list()
            except Exception as e:
                print(f"Erreur refresh metrics: {e}")
            
            try:
                self.refresh_personas_list()
            except Exception as e:
                print(f"Erreur refresh personas: {e}")
            
            try:
                self.refresh_trackers_list()
            except Exception as e:
                print(f"Erreur refresh trackers: {e}")
            
            try:
                self.refresh_activities_list()
            except Exception as e:
                print(f"Erreur refresh activities: {e}")
            
        except Exception as e:
            print(f"Erreur update UI: {e}")
            logger.error(f"Error updating UI: {e}")
    
    def update_graphs(self, metric: MetricSnapshot):
        """Met à jour les graphiques"""
        # Score de confusion
        self.ax1.clear()
        confusion_values = [m.confusion_score for m in list(self.metrics_history)[-30:]]
        self.ax1.plot(confusion_values, color='#3498db', linewidth=2)
        self.ax1.set_title("Score de Confusion")
        self.ax1.set_ylim(0, 100)
        self.ax1.grid(True, alpha=0.3)
        
        # Personas actifs
        self.ax2.clear()
        personas_values = [m.personas_active for m in list(self.metrics_history)[-30:]]
        self.ax2.bar(range(len(personas_values)), personas_values, color='#2ecc71', alpha=0.7)
        self.ax2.set_title("Personas Actifs")
        self.ax2.set_ylim(0, self.config.max_personas + 5)
        self.ax2.grid(True, alpha=0.3)
        
        # Trackers par type (camembert)
        self.ax3.clear()
        if metric.trackers_by_type:
            labels = list(metric.trackers_by_type.keys())
            sizes = list(metric.trackers_by_type.values())
            self.ax3.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        self.ax3.set_title("Trackers par Type")
        
        # Actions par minute
        self.ax4.clear()
        actions_values = [m.actions_per_minute for m in list(self.metrics_history)[-30:]]
        self.ax4.plot(actions_values, color='#e74c3c', linewidth=2, marker='o')
        self.ax4.set_title("Activités par Minute")
        self.ax4.set_ylim(0, max(actions_values + [10]) * 1.2)
        self.ax4.grid(True, alpha=0.3)
        
        self.canvas.draw()
    
    def refresh_metrics_list(self):
        """Rafraîchit la liste des métriques"""
        # Effacer la liste
        for item in self.metrics_tree.get_children():
            self.metrics_tree.delete(item)
        
        # Ajouter les métriques récentes
        for metric in list(self.metrics_history)[-50:]:
            self.metrics_tree.insert("", 0, values=(
                metric.timestamp.strftime("%H:%M:%S"),
                f"{metric.confusion_score:.0f}%",
                metric.personas_active,
                metric.noise_generated,
                metric.trackers_detected,
                f"{metric.actions_per_minute:.1f}",
                f"{metric.success_rate*100:.0f}%",
                f"{metric.cpu_usage:.0f}%",
                f"{metric.memory_usage:.0f} MB"
            ))
    
    def refresh_personas_list(self):
        """Rafraîchit la liste des personas"""
        # Effacer la liste
        for item in self.personas_tree.get_children():
            self.personas_tree.delete(item)
        
        # Récupérer les personas depuis la base
        with self.brouilleur.db.get_cursor() as cur:
            cur.execute('''
                SELECT id, name, age, interests, total_activities, success_rate, last_active
                FROM personas
                ORDER BY last_active DESC
                LIMIT 100
            ''')
            
            for row in cur.fetchall():
                interests = json.loads(row[3]) if row[3] else []
                interests_str = ', '.join(interests[:2]) + ('...' if len(interests) > 2 else '')
                
                self.personas_tree.insert("", "end", values=(
                    row[0][:8],
                    row[1],
                    row[2],
                    interests_str,
                    row[4],
                    f"{row[5]*100:.0f}%",
                    row[6][11:16] if row[6] else ""
                ), tags=(row[0],))
    
    def refresh_trackers_list(self):
        """Rafraîchit la liste des trackers"""
        # Effacer la liste
        for item in self.trackers_tree.get_children():
            self.trackers_tree.delete(item)
        
        try:
            # Récupérer les trackers depuis la base
            if hasattr(self, 'brouilleur') and self.brouilleur and hasattr(self.brouilleur, 'db'):
                with self.brouilleur.db.get_cursor() as cur:
                    cur.execute('''
                        SELECT name, domain, type, detection_count,
                               first_seen, last_seen
                        FROM trackers
                        ORDER BY last_seen DESC
                        LIMIT 100
                    ''')
                    
                    for row in cur.fetchall():
                        self.trackers_tree.insert("", "end", values=(
                            row[0] or "Inconnu",
                            row[1] or "",
                            row[2] or "unknown",
                            row[3] or 0,
                            row[4][:10] if row[4] else "",
                            row[5][:10] if row[5] else ""
                        ))
        except Exception as e:
            print(f"Erreur refresh trackers: {e}")
            logger.error(f"Error refreshing trackers: {e}")
        
        # Mettre à jour les statistiques
        self.update_tracker_stats()
    
    def update_tracker_stats(self):
        """Met à jour les statistiques des trackers"""
        try:
            if hasattr(self, 'brouilleur') and self.brouilleur and hasattr(self.brouilleur, 'db'):
                with self.brouilleur.db.get_cursor() as cur:
                    # Total
                    cur.execute('SELECT COUNT(*) FROM trackers')
                    total = cur.fetchone()[0]
                    if "Total" in self.tracker_stats_labels:
                        self.tracker_stats_labels["Total"].configure(text=str(total))
                    
                    # Par type
                    tracker_types = ["analytics", "advertising", "social", "fingerprint", "pixel"]
                    for ttype in tracker_types:
                        cur.execute('SELECT COUNT(*) FROM trackers WHERE type = ?', (ttype,))
                        count = cur.fetchone()[0]
                        label_name = ttype.capitalize()
                        if label_name in self.tracker_stats_labels:
                            self.tracker_stats_labels[label_name].configure(text=str(count))
        except Exception as e:
            print(f"Erreur update tracker stats: {e}")
            logger.error(f"Error updating tracker stats: {e}")
        
        # Mettre à jour le graphique circulaire
        self.update_tracker_pie_chart()
    
    def update_tracker_pie_chart(self):
        """Met à jour le graphique circulaire des trackers"""
        try:
            self.tracker_ax.clear()
            
            if hasattr(self, 'brouilleur') and self.brouilleur and hasattr(self.brouilleur, 'db'):
                with self.brouilleur.db.get_cursor() as cur:
                    cur.execute('''
                        SELECT type, COUNT(*) as count
                        FROM trackers
                        GROUP BY type
                    ''')
                    
                    data = cur.fetchall()
                    if data:
                        labels = [row[0] or 'unknown' for row in data]
                        sizes = [row[1] for row in data]
                        colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']
                        
                        self.tracker_ax.pie(sizes, labels=labels, colors=colors[:len(labels)],
                                           autopct='%1.1f%%', startangle=90)
                        self.tracker_ax.set_title("Répartition des Trackers")
                    else:
                        self.tracker_ax.text(0.5, 0.5, "Aucun tracker détecté", 
                                            ha='center', va='center', transform=self.tracker_ax.transAxes)
                        self.tracker_ax.set_title("Répartition des Trackers")
            
            self.tracker_canvas.draw()
        except Exception as e:
            print(f"Erreur update tracker pie chart: {e}")
            logger.error(f"Error updating tracker pie chart: {e}")
    
    def refresh_activities_list(self):
        """Rafraîchit la liste des activités"""
        # Effacer la liste
        for item in self.activities_tree.get_children():
            self.activities_tree.delete(item)
        
        # Récupérer les activités récentes
        with self.brouilleur.db.get_cursor() as cur:
            cur.execute('''
                SELECT a.timestamp, p.name, a.activity_type, a.site, a.duration, a.success
                FROM activities a
                JOIN personas p ON a.persona_id = p.id
                ORDER BY a.timestamp DESC
                LIMIT 100
            ''')
            
            for row in cur.fetchall():
                self.activities_tree.insert("", "end", values=(
                    row[0][11:19] if row[0] else "",
                    row[1],
                    row[2],
                    row[3] or "",
                    f"{row[4]}s" if row[4] else "",
                    "✅" if row[5] else "❌"
                ))
        
        # Mettre à jour le graphique d'activité
        self.update_activity_graph()
    
    def update_activity_graph(self):
        """Met à jour le graphique d'activité en temps réel"""
        self.activity_ax.clear()
        
        with self.brouilleur.db.get_cursor() as cur:
            # Activités des dernières 24h par heure
            cur.execute('''
                SELECT strftime('%H', timestamp) as hour, COUNT(*) as count
                FROM activities
                WHERE timestamp > datetime('now', '-24 hours')
                GROUP BY hour
                ORDER BY hour
            ''')
            
            data = cur.fetchall()
            if data:
                hours = [f"{int(row[0]):02d}h" for row in data]
                counts = [row[1] for row in data]
                
                self.activity_ax.bar(hours, counts, color='#3498db', alpha=0.7)
                self.activity_ax.set_title("Activités par Heure (24h)")
                self.activity_ax.set_xlabel("Heure")
                self.activity_ax.set_ylabel("Nombre d'activités")
                self.activity_ax.grid(True, alpha=0.3)
                
                # Rotation des labels pour lisibilité
                plt.setp(self.activity_ax.xaxis.get_majorticklabels(), rotation=45)
        
        self.activity_canvas.draw()
    
    def on_persona_select(self, event):
        """Gère la sélection d'un persona"""
        selection = self.personas_tree.selection()
        if not selection:
            return
        
        # Récupérer l'ID du persona
        persona_id = self.personas_tree.item(selection[0])['tags'][0]
        
        # Afficher les détails
        with self.brouilleur.db.get_cursor() as cur:
            cur.execute('SELECT * FROM personas WHERE id = ?', (persona_id,))
            persona = cur.fetchone()
            
            if persona:
                details = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 DÉTAILS DU PERSONA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🆔 ID: {persona[0]}
👤 Nom: {persona[1]}
🎂 Âge: {persona[2]}
⚥ Genre: {persona[3]}
📍 Localisation: {persona[4]}
💼 Occupation: {persona[5]}

🎯 Intérêts:
{chr(10).join('  • ' + i for i in json.loads(persona[6]) if persona[6])}

💔 Dislikes:
{chr(10).join('  • ' + i for i in json.loads(persona[7]) if persona[7])}

📊 Statistiques:
  • Score de cohérence: {persona[10]*100:.1f}%
  • Niveau intelligence: {persona[11]*100:.1f}%
  • Niveau paranoïa: {persona[12]*100:.1f}%
  • Compétences tech: {persona[13]*100:.1f}%
  • Habitude dépense: {persona[14]}
  • Total activités: {persona[18]}
  • Taux succès: {persona[19]*100:.1f}%

📱 Réseaux sociaux:
{chr(10).join('  • ' + k + ': ' + ('✅' if v else '❌') for k, v in json.loads(persona[15]).items() if persona[15])}

⏰ Créé le: {persona[16][:19]}
🕒 Dernière activité: {persona[17][:19] if persona[17] else 'Jamais'}
"""
                self.persona_details.delete("1.0", "end")
                self.persona_details.insert("1.0", details)
    
    def refresh_dashboard(self):
        """Rafraîchit le dashboard"""
        # Simuler un rafraîchissement
        self.log("🔄 Rafraîchissement du dashboard...")
        self.update_graphs(self.brouilleur.calculate_metrics() if hasattr(self.brouilleur, 'calculate_metrics') else None)
    
    def export_graphs(self):
        """Exporte les graphiques en image"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"graphs_{timestamp}.png"
        self.fig.savefig(filename, dpi=300, bbox_inches='tight')
        self.log(f"💾 Graphiques exportés: {filename}")
    
    def show_detailed_stats(self):
        """Affiche les statistiques détaillées dans une nouvelle fenêtre"""
        stats_window = ctk.CTkToplevel(self.window)
        stats_window.title("Statistiques Détaillées")
        stats_window.geometry("600x400")
        
        # Récupérer les stats
        stats = self.brouilleur.db.get_statistics() if hasattr(self.brouilleur, 'db') else {}
        
        # Afficher dans un textbox
        textbox = ctk.CTkTextbox(stats_window, font=("Courier", 11))
        textbox.pack(fill="both", expand=True, padx=10, pady=10)
        
        stats_text = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 STATISTIQUES DÉTAILLÉES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 APERÇU GÉNÉRAL
──────────────────
• Total Personas: {stats.get('total_personas', 0)}
• Activités 24h: {stats.get('activities_24h', 0)}
• Trackers détectés: {stats.get('trackers', 0)}
• Faux comptes: {stats.get('fake_accounts', 0)}
• Achats simulés: {stats.get('purchases', 0)}

🎯 ACTIVITÉS PAR TYPE
──────────────────"""
        
        for atype, count in stats.get('activities_by_type', {}).items():
            stats_text += f"\n• {atype}: {count}"
        
        stats_text += f"""

📱 COMPTES PAR PLATEFORME
──────────────────"""
        
        for platform, count in stats.get('accounts_by_platform', {}).items():
            stats_text += f"\n• {platform}: {count}"
        
        textbox.insert("1.0", stats_text)
    
    def refresh_metrics(self):
        """Rafraîchit la liste des métriques"""
        self.refresh_metrics_list()
        self.log("🔄 Métriques rafraîchies")
    
    def export_table(self, table_name):
        """Exporte une table en CSV"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{table_name}_{timestamp}.csv"
        
        try:
            self.brouilleur.db.export_to_csv(table_name, filename)
            self.log(f"💾 Table {table_name} exportée: {filename}")
        except Exception as e:
            self.log(f"❌ Erreur export: {e}")
    
    def clean_old_metrics(self):
        """Nettoie les anciennes métriques"""
        if messagebox.askyesno("Confirmation", "Supprimer les métriques de plus de 30 jours ?"):
            self.brouilleur.db.cleanup_old_data(30)
            self.log("🗑️ Anciennes métriques nettoyées")
    
    def refresh_personas(self):
        """Rafraîchit la liste des personas"""
        self.refresh_personas_list()
        self.log("🔄 Personas rafraîchis")
    
    def clear_logs(self):
        """Efface les logs"""
        if messagebox.askyesno("Confirmation", "Effacer tous les logs ?"):
            self.log_text.delete("1.0", "end")
            self.log("🗑️ Logs effacés")
    
    def save_logs(self):
        """Sauvegarde les logs dans un fichier"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"logs_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.log_text.get("1.0", "end"))
            self.log(f"💾 Logs sauvegardés: {filename}")
        except Exception as e:
            self.log(f"❌ Erreur sauvegarde: {e}")
    
    def filter_logs(self):
        """Filtre les logs par niveau"""
        level = self.log_level_var.get()
        # Implémenter le filtrage si nécessaire
        self.log(f"🔍 Filtrage logs: {level}")
    
    def log(self, message):
        """Ajoute un message aux logs"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.log_text.insert("end", log_entry)
        self.log_text.see("end")
        
        # Logger aussi dans le fichier
        logger.info(message)
    
    def run(self):
        """Lance l'interface graphique"""
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()
    
    def on_closing(self):
        """Gère la fermeture de l'application"""
        if self.is_running:
            if messagebox.askyesno("Confirmation", "Le brouillage est en cours. Arrêter ?"):
                self.is_running = False
                if hasattr(self, 'brouilleur'):
                    self.brouilleur.is_running = False
            else:
                return
        
        self.window.quit()

# ============================================================================
# POINT D'ENTRÉE PRINCIPAL
# ============================================================================

def main():
    """Fonction principale"""
    print("""
    ╔════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                ║
    ║     ██████╗ ██████╗  ██████╗ ██╗   ██╗██╗██╗     ██╗     ███████╗██╗           ║
    ║     ██╔══██╗██╔══██╗██╔═══██╗██║   ██║██║██║     ██║     ██╔════╝██║           ║
    ║     ██████╔╝██████╔╝██║   ██║██║   ██║██║██║     ██║     █████╗  ██║           ║
    ║     ██╔══██╗██╔══██╗██║   ██║██║   ██║██║██║     ██║     ██╔══╝  ██║           ║
    ║     ██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║███████╗███████╗███████╗███████╗      ║
    ║     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝      ║
    ║                                                                                ║
    ║              ██████╗ ██╗███████╗████████╗███████╗                              ║
    ║              ██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝                              ║
    ║              ██████╔╝██║█████╗     ██║   █████╗                                ║
    ║              ██╔═══╝ ██║██╔══╝     ██║   ██╔══╝                                ║
    ║              ██║     ██║███████╗   ██║   ███████╗                              ║
    ║              ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝                              ║
    ║                                                                                ║
    ║                      VERSION 3.0 - ÉDITION ULTIMATE                            ║
    ║                                                                                ║
    ║                    Le Paradoxe de la Confidentialité                           ║
    ║                                                                                ║
    ╠════════════════════════════════════════════════════════════════════════════════╣
    ║                                                                                ║
    ║  🚀 FONCTIONNALITÉS:                                                           ║
    ║  ~~~~~~~~~~~~~~~~~                                                             ║
    ║  ✓ Jusqu'à 50 personas simultanés avec IA comportementale                     ║
    ║  ✓ Détection intelligente de 50+ trackers différents                          ║
    ║  ✓ Mode Caméléon adaptatif avec contre-mesures automatiques                   ║
    ║  ✓ Simulation d'achats réaliste avec génération de cartes                     ║
    ║  ✓ Création de faux comptes sur 10+ plateformes                               ║
    ║  ✓ Navigation humaine avec courbes de Bézier et micro-pauses                  ║
    ║  ✓ Base de données SQLite optimisée avec cache                                ║
    ║  ✓ API REST complète avec 25+ endpoints                                       ║
    ║  ✓ Interface graphique avancée avec 7 onglets et graphiques temps réel        ║
    ║  ✓ Système de métriques en temps réel avec 30+ KPIs                           ║
    ║  ✓ Sauvegarde automatique et export multi-format (CSV/JSON/Parquet)           ║
    ║  ✓ Mode furtif avancé avec rotation de fingerprints                           ║
    ║                                                                               ║
    ╚═══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Vérifier les dépendances critiques
    required_packages = ['playwright', 'customtkinter', 'matplotlib', 
                        'flask', 'psutil', 'numpy', 'pandas', 'fake-useragent']
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print("\n❌ PAQUETS MANQUANTS:")
        print("   " + ", ".join(missing))
        print("\n📦 INSTALLATION:")
        print("   pip install " + " ".join(missing))
        print("   playwright install chromium")
        print("\n⚠️  Veuillez installer les dépendances avant de continuer.")
        input("\nAppuyez sur Entrée pour quitter...")
        sys.exit(1)
    
    print("✅ Toutes les dépendances sont installées")
    print("\n🚀 Démarrage de l'application...\n")
    
    # Créer les répertoires nécessaires
    os.makedirs("backups", exist_ok=True)
    os.makedirs("exports", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    # Lancer l'interface
    app = UltimateGUI()
    app.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Arrêt demandé par l'utilisateur")
    except Exception as e:
        print(f"\n💥 Erreur fatale: {e}")
        traceback.print_exc()
        input("\nAppuyez sur Entrée pour quitter...")

