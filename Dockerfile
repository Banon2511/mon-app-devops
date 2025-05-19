# Utilisez une image Python officielle
FROM python:3.9-slim

# Copiez les fichiers dans le conteneur
COPY . /app
WORKDIR /app

# Exposez le port 8000
EXPOSE 8000

# Lancez le serveur Python
CMD ["python", "app.py"]