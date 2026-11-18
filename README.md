# TP5 - MikroTik CHR REST API

Automatisation de la configuration d'un routeur MikroTik CHR (v7) avec Python.

## Prérequis
- Python 3
- `pip install requests python-dotenv flask`

## Configuration
Créer un fichier `.env` à la racine :

    DEVICE_SCHEME=http
    DEVICE_HOST=127.0.0.1:5000
    DEVICE_USER=api-user
    DEVICE_PASSWORD=motdepasse

Pour un vrai CHR : `DEVICE_SCHEME=https` et `DEVICE_HOST=<ip du routeur>`.

## Lancer les scripts
1. Démarrer le routeur simulé (laisser ce terminal ouvert) :

        python mock_routeros.py

2. Dans un second terminal :

        python crud_test.py          # GET, POST, PATCH, DELETE sur /ip/address
        python configure_router.py   # création idempotente de routes statiques
        python print_addresses.py    # affiche les adresses IP

## Capture
Voir `ip-address-print.png`

## Note
Faute de VM MikroTik CHR disponible, les scripts ont été testés contre un
serveur simulé (`mock_routeros.py`) qui reproduit l'API REST de RouterOS v7.

## Auteur
Soumou Selmi
