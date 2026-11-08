# MERISE & Django —  Systèmes d'Informations

## Présentation

Ce dépôt regroupe les travaux pratiques réalisés dans le cadre du module **Systèmes d'information**.

L'objectif de ces travaux est de mettre en pratique les différentes étapes de conception d'un système d'information selon la méthodologie **MERISE**, puis de passer à son implémentation à l'aide du framework web **Django**, basé sur Python.

Le dépôt centralise les supports pédagogiques, les travaux de conception et les développements réalisés au fil des séances de TP.

## Objectifs pédagogiques

- Comprendre les principes fondamentaux de la méthodologie MERISE.
- Analyser et modéliser les besoins d'un système d'information.
- Élaborer les différents modèles conceptuels et logiques.
- Comprendre le passage de la conception à l'implémentation.
- Développer des applications web avec Django.
- Manipuler les modèles de données et les interactions avec une base de données.

## Technologies et méthodologies

| Outil / Technologie | Utilisation |
|---|---|
| Python | Langage de programmation |
| Django | Framework de développement web |
| SQLite | Base de données |
| MERISE | Méthodologie de conception |
| Git & GitHub | Gestion du code source et versionnement |

## Organisation du dépôt

```text
merise-django-project/
│
├── pdf/
│   ├── Support_TP_1.pdf
│   ├── Support_TP_2-Fr.pdf
|   ├── Support_TP_3_FR.pdf
│   └── ...
│
├── tp1/
│   ├── app1/
│   ├── Product/
│   ├── tp1/
│   ├── manage.py
│   └── ...
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Environnement de développement

Le projet utilise un environnement virtuel Python afin d'isoler ses dépendances.

Pour installer les dépendances :

```bash
pip install -r requirements.txt
```

Pour lancer le serveur de développement Django, se placer dans le dossier du TP concerné :

```bash
cd tp1
python manage.py runserver
```

## Travaux pratiques

Les différents TP sont organisés séparément afin de faciliter leur consultation et leur évolution.

Chaque dossier de TP contient les éléments nécessaires à son développement : configuration Django, applications et fichiers associés.

## Contexte académique

Travaux réalisés dans le cadre du module **Systèmes d'information**.

Ce dépôt constitue un espace de centralisation et de suivi des apprentissages en conception et développement des systèmes d'information.

---

**Statut :** En cours de réalisation.