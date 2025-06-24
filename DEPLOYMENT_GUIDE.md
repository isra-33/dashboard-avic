# 🚀 Guide de Déploiement - Tableau de Bord Avicole

## 📋 Prérequis

- Compte GitHub
- Python 3.9+ installé localement
- Git installé

## 🎯 Option 1: Streamlit Cloud (RECOMMANDÉ)

### Étape 1: Préparer le Repository
```bash
# Initialiser Git si pas déjà fait
git init
git add .
git commit -m "Initial commit - Dashboard Avicole"
```

### Étape 2: Pousser vers GitHub
```bash
# Créer un nouveau repository sur GitHub
# Puis pousser votre code
git remote add origin https://github.com/votre-username/votre-repo.git
git branch -M main
git push -u origin main
```

### Étape 3: Déployer sur Streamlit Cloud
1. Aller sur [share.streamlit.io](https://share.streamlit.io)
2. Se connecter avec GitHub
3. Cliquer "New app"
4. Configurer:
   - **Repository**: Sélectionner votre repo
   - **Branch**: `main`
   - **Main file path**: `dashboard_avicole_simple.py`
5. Cliquer "Deploy"

✅ **Avantages**: Gratuit, automatique, facile

## 🐳 Option 2: Docker

### Étape 1: Construire l'Image
```bash
docker build -t dashboard-avicole .
```

### Étape 2: Exécuter le Container
```bash
docker run -p 8501:8501 dashboard-avicole
```

### Étape 3: Accéder à l'Application
Ouvrir http://localhost:8501

## ☁️ Option 3: Heroku

### Étape 1: Installer Heroku CLI
```bash
# Windows
winget install --id=Heroku.HerokuCLI

# Ou télécharger depuis: https://devcenter.heroku.com/articles/heroku-cli
```

### Étape 2: Se Connecter
```bash
heroku login
```

### Étape 3: Créer l'Application
```bash
heroku create votre-app-name
```

### Étape 4: Déployer
```bash
git push heroku main
```

### Étape 5: Ouvrir l'Application
```bash
heroku open
```

## 🌐 Option 4: VPS (Serveur Privé Virtuel)

### Étape 1: Se Connecter au Serveur
```bash
ssh utilisateur@votre-serveur.com
```

### Étape 2: Installer les Dépendances
```bash
sudo apt update
sudo apt install python3 python3-pip nginx
```

### Étape 3: Cloner le Projet
```bash
git clone https://github.com/votre-username/votre-repo.git
cd votre-repo
pip3 install -r requirements.txt
```

### Étape 4: Configurer Nginx
```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Étape 5: Lancer l'Application
```bash
nohup streamlit run dashboard_avicole_simple.py --server.port=8501 --server.address=0.0.0.0 &
```

## 🔧 Configuration Avancée

### Variables d'Environnement
```bash
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true
```

### Configuration Streamlit
Le fichier `.streamlit/config.toml` contient:
```toml
[server]
headless = true
enableCORS = false
port = 8501

[browser]
gatherUsageStats = false
```

## 📊 Monitoring et Maintenance

### Vérifier les Logs
```bash
# Streamlit Cloud: Automatique
# Heroku
heroku logs --tail

# Docker
docker logs container-name

# VPS
tail -f /var/log/nginx/access.log
```

### Mettre à Jour l'Application
```bash
# Modifier le code
git add .
git commit -m "Update dashboard"
git push origin main

# Streamlit Cloud: Mise à jour automatique
# Heroku
git push heroku main

# Docker
docker build -t dashboard-avicole .
docker stop container-name
docker run -p 8501:8501 dashboard-avicole
```

## 🛠️ Dépannage

### Problèmes Courants

1. **Port déjà utilisé**
   ```bash
   # Changer le port
   streamlit run dashboard_avicole_simple.py --server.port=8502
   ```

2. **Dépendances manquantes**
   ```bash
   pip install -r requirements.txt
   ```

3. **Permissions**
   ```bash
   chmod +x dashboard_avicole_simple.py
   ```

### Support
- [Documentation Streamlit](https://docs.streamlit.io)
- [Streamlit Community](https://discuss.streamlit.io)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

## 🎉 Félicitations!

Votre tableau de bord avicole est maintenant déployé et accessible en ligne! 