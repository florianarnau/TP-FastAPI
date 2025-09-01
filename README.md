# 🧀 Fromagerie DIGICHEESE - API FastAPI

Projet de refonte du système d’information de la **Fromagerie DIGICHEESE**.  
Cette application remplace une ancienne solution sous Access par une API moderne basée sur **FastAPI**, **SQLAlchemy** et **MySQL**.

---

## 🚀 Tech Stack

- **Python 3.13**
- **FastAPI** (framework web moderne)
- **SQLAlchemy** (ORM)
- **MySQL** (BDD)
- **Uvicorn** (serveur ASGI)
- **Pydantic v2** (validation des données)
- **Git & GitHub** (gestion de version)
- **Herd / phpMyAdmin** (gestion MySQL locale)

---

## 📂 Structure du projet

```
app/
│── main.py # Point d’entrée FastAPI
│── database.py # Connexion SQLAlchemy
│── models.py # Modèles ORM
│── schemas.py # Schémas Pydantic
│── routers/ # Routes CRUD organisées par ressource
│ ├── client.py
│ ├── commande.py
│ ├── objet.py
│ ├── conditionnement.py
│ ├── commune.py
│ ├── departement.py
│ ├── utilisateur.py
│ └── role.py
│── seed.py # Script de remplissage BDD (données de test)
```

---

## ⚙️ Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/florianarnau/TP-FastAPI.git
cd TP-FastAPI
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
```

### 3. Installer les dépendances
pip install -r requirements.txt

### 4. Configurer la base MySQL

Créer une base de données fromagerie_com dans phpMyAdmin / MySQL :

```SQL
CREATE DATABASE fromagerie_com CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

Configurer les identifiants dans app/database.py (ou .env) :

```SQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost/fromagerie_com"
```

### 5. Lancer le serveur

```
uvicorn app.main:app --reload
```

Accéder à la doc interactive :
👉 http://127.0.0.1:8000/docs

📦 Données de test (seed)

Pour remplir la base avec des exemples de départements, communes, clients, commandes, objets, etc. :

```bash
python -m app.seed
```

🔑 Fonctionnalités principales
📋 Administration (Admin)

- CRUD utilisateurs
- CRUD départements, communes, objets, conditionnements, poids & vignettes
- Impression au format papier (prévu)

📦 Gestion des colis (OP-colis)

- CRUD clients & commandes
- Gestion des colis + relation objets/conditionnements
- Statistiques par période
- Mailing clients + envoi d’emails
- Historique des colis

🏬 Gestion des stocks (OP-stock)

- Vue globale sur les stocks
- Mise à jour annuelle via un bouton d’action
- Impression au format papier

✅ Tests

Des tests unitaires et fonctionnels seront ajoutés avec pytest.
Exemple prévu :

```bash
pytest -v
```

👤 Auteur

Projet réalisé par Florian Arnau dans le cadre du TP Développement d’une application informatique.

---
