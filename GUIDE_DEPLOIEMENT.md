# 🚀 Guide de Déploiement - Dashboard Avicole

## 📁 Structure du Projet

```
dashboard-avicole/
├── dashboard_avicole_simple.py    # Application principale
├── requirements.txt               # Dépendances Python
├── README.md                     # Documentation
├── .gitignore                    # Fichiers à ignorer
├── Procfile                      # Configuration Heroku
├── runtime.txt                   # Version Python
├── Dockerfile                    # Configuration Docker
├── DEPLOYMENT_GUIDE.md           # Guide complet
├── GUIDE_DEPLOIEMENT.md          # Ce guide
└── .streamlit/
    └── config.toml              # Configuration Streamlit
```

## 🎯 Déploiement sur Streamlit Cloud (RECOMMANDÉ)

### Étape 1: Créer le Repository GitHub

1. **Aller sur GitHub.com** et se connecter
2. **Créer un nouveau repository**:
   - Nom: `dashboard-avicole`
   - Description: `Tableau de bord avicole interactif`
   - Public (recommandé)
   - **Ne PAS** cocher "Add a README file"

### Étape 2: Initialiser Git dans ce dossier

```bash
# Naviguer vers le dossier
cd dashboard-avicole

# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit - Dashboard Avicole"

# Ajouter le remote (remplacez YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/dashboard-avicole.git

# Renommer la branche
git branch -M main

# Pousser vers GitHub
git push -u origin main
```

### Étape 3: Déployer sur Streamlit Cloud

1. **Aller sur [share.streamlit.io](https://share.streamlit.io)**
2. **Se connecter avec GitHub**
3. **Cliquer "New app"**
4. **Configurer**:
   - Repository: `YOUR_USERNAME/dashboard-avicole`
   - Branch: `main`
   - Main file path: `dashboard_avicole_simple.py`
5. **Cliquer "Deploy"**

## 🐳 Déploiement avec Docker

```bash
# Construire l'image
docker build -t dashboard-avicole .

# Exécuter le container
docker run -p 8501:8501 dashboard-avicole
```

## ☁️ Déploiement sur Heroku

```bash
# Installer Heroku CLI
winget install --id=Heroku.HerokuCLI

# Se connecter
heroku login

# Créer l'application
heroku create votre-app-name

# Déployer
git push heroku main

# Ouvrir l'application
heroku open
```

## 📊 Vérification

Après le déploiement, votre dashboard sera accessible via :
- **Streamlit Cloud**: `https://votre-app.streamlit.app`
- **Heroku**: `https://votre-app-name.herokuapp.com`
- **Local**: `http://localhost:8501`

## 🔧 Mise à Jour

Pour mettre à jour l'application :

```bash
# Modifier le code
git add .
git commit -m "Update dashboard"
git push origin main

# Streamlit Cloud se met à jour automatiquement
```

## 📞 Support

- **Problèmes Git**: Vérifiez que Git est installé
- **Erreur de déploiement**: Vérifiez le nom du fichier principal
- **Port occupé**: Changez le port dans la configuration

## 🎉 Félicitations !

Votre tableau de bord avicole est maintenant déployé et accessible en ligne ! 