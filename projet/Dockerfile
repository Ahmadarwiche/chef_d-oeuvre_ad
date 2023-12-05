# Utiliser une image officielle de Python comme base
FROM python:3.9

# Créer et définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur à /app/
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copier tout le reste dans le conteneur à /app/
COPY . /app/

# Exposer le port 8000 pour Django
EXPOSE 8000

# Lancer la commande pour démarrer l'application Django
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


#CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "mysite.wsgi:application"]

# Lancer la commande pour démarrer l'application Django avec Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "projet.wsgi:application"]
