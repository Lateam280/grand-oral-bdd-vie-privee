# GestData — Grand Oral NSI Terminale

> **Problématique : Comment les bases de données permettent-elles de gérer efficacement les informations personnelles tout en respectant la vie privée des utilisateurs ?**

---

## Présentation du projet

GestData est une application web locale simulant la gestion d'une base de données d'utilisateurs. Elle a été conçue dans le cadre du Grand Oral de NSI (Terminale) pour illustrer concrètement les enjeux de la vie privée dans les systèmes informatiques modernes.

Le projet démontre deux états d'une même application :
- Une version **non sécurisée** où les données personnelles sont exposées
- Une version **sécurisée** conforme aux bonnes pratiques et au RGPD

---

## Architecture du projet
grand-oral-bdd-vie-privee/
│
├── app.py                  # Serveur Flask — routes et connexion BDD
├── init_db.py              # Initialisation de la base de données
├── faker_data.py           # Génération de 50 utilisateurs fictifs
├── schema.sql              # Structure des tables SQL
├── requetes.sql            # Requêtes SQL de démonstration
├── database.db             # Base de données SQLite (non versionnée)
├── requirements.txt        # Dépendances Python
│
└── templates/
├── base.html           # Template de base (navbar, style)
├── index.html          # Page d'accueil
├── utilisateurs.html   # Liste des utilisateurs (vue administrateur)
└── profil.html         # Profil d'un utilisateur

---

## Schéma de la base de données
┌─────────────────────┐       ┌─────────────────────┐       ┌─────────────────────┐
│     utilisateurs    │       │        posts         │       │      connexions      │
├─────────────────────┤       ├─────────────────────┤       ├─────────────────────┤
│ id (PK)             │◄──────│ id (PK)              │       │ id (PK)             │
│ nom                 │       │ id_utilisateurs (FK) │       │ id_utilisateurs (FK)│◄─── utilisateurs(id)
│ prenom              │       │ contenu              │       │ date_connexion      │
│ email               │       │ date_publication     │       │ adresse_ip          │
│ mot_de_passe        │       └─────────────────────┘       └─────────────────────┘
│ date_inscription    │
└─────────────────────┘

---

## Les deux branches du projet

### `version-non-securisee`
- Mots de passe stockés **en clair** dans la base
- Données personnelles entièrement visibles
- Aucune protection en cas de fuite

### `version-securisee`
- Mots de passe **hashés** avec `werkzeug`
- Données sensibles masquées dans l'interface
- **Droit à l'effacement** conforme au RGPD (suppression d'un compte)

---

## Stack technique

| Technologie | Rôle |
|---|---|
| Python + Flask | Serveur web et routes |
| SQLite | Base de données locale |
| Jinja2 | Templates HTML dynamiques |
| Tailwind CSS | Interface moderne |
| Faker | Génération de données fictives |
| Werkzeug | Hashage des mots de passe |

---

## Lancer le projet en local

### Prérequis
- Python 3.10+
- Git

### Installation

```bash
# 1. Cloner le repository
git clone https://github.com/Lateam280/grand-oral-bdd-vie-privee.git
cd grand-oral-bdd-vie-privee

# 2. Créer et activer l'environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Initialiser la base de données
python init_db.py

# 5. Générer les données fictives
python faker_data.py

# 6. Lancer le serveur
python app.py
```

Ouvre ensuite **http://127.0.0.1:5000** dans ton navigateur.

---

## Requêtes SQL de démonstration

### Afficher tous les utilisateurs
```sql
SELECT * FROM utilisateurs;
```

### Rechercher un utilisateur par email
```sql
SELECT * FROM utilisateurs WHERE email LIKE '%gmail%';
```

### Compter les utilisateurs inscrits
```sql
SELECT COUNT(*) FROM utilisateurs;
```

### Supprimer un utilisateur (droit à l'effacement RGPD)
```sql
DELETE FROM utilisateurs WHERE id = 1;
```

### Afficher les utilisateurs inscrits cette décennie
```sql
SELECT nom, prenom, date_inscription 
FROM utilisateurs 
ORDER BY date_inscription DESC;
```

---

## Notions NSI abordées

- **Modèle relationnel** : tables, clés primaires, clés étrangères
- **Langage SQL** : SELECT, INSERT, DELETE, WHERE, ORDER BY
- **Architecture web** : modèle client-serveur, requêtes HTTP
- **Sécurité** : hashage, exposition des données, injection SQL
- **RGPD** : droit à l'effacement, données sensibles

---

## Auteur

Projet réalisé par **Lateam280** dans le cadre du Grand Oral de Terminale — Spécialité NSI.