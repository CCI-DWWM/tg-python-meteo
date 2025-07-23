# tg-python-meteo

Application web FastAPI permettant à un utilisateur de connaître **le nom d'une commune et la météo actuelle** à partir de son **code postal**.

## Fonctionnalités

- Saisie d’un code postal via un formulaire HTML
- Récupération du nom de la commune depuis une base de données MySQL
- Appel à une API météo publique pour afficher les conditions actuelles
- Utilisation de fichiers `.env` pour sécuriser les informations de connexion
- Résultat affiché proprement dans une page HTML avec Bootstrap


## Installation

1. Créer un environnement virtuel Python :
    ```bash
    py -m venv .venv
    ```

2. Activer l’environnement virtuel :
    ```bash
    .venv\Scripts\activate.bat # Windows CMD
    ```

3. Installer les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
   
4. Créer la base de données et importer les données :
    ```
   #/datas/communes-cp.sql
   ```
   
5. Créer un fichier `.env` à la racine du projet :

   Exemple de contenu :
   ```
   DB_USER=root
   DB_PASSWORD=motdepasse
   DB_HOST=localhost
   DB_DATABASE=meteo
   ```
## Lancer l'application

Lancer le serveur
```bash
fastapi dev main.py
```

Ensuite, accéder à l'app dans un navigateur
[http://127.0.0.1:8000](http://127.0.0.1:8000)

## Structure du projet
- `main.py` : point d'entrée de l'application FastAPI
- `database.py` : connexion à la base de données
- `model.py` : gestion des requêtes
- `weatherAPI.py` : appel à l'API météo externe
- `/templates/cp.html` : template HTML principal (formulaire + résultat)
- `.env` : configuration (non versionné)
- `/datas/communes-cp.sql` : fichier SQL contenant les codes postaux et villes

## Fichiers non utilisés

Les fichiers et dossiers suivants ont été utilisés **pour les exercices 
d’introduction à FastAPI**, mais ne sont pas utilisés dans l’application finale :

- `getAPI.py`
- `test_weather.py`
- `/static/`
- `/templates/item.html`
- la deuxième partie de `main.py` (indiqué en commentaire)

Ils peuvent être ignorés dans le cadre du projet principal.

## Documentation (Swagger UI)

Une documentation de l’API est générée automatiquement par FastAPI :
 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)