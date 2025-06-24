# 🐔 Tableau de Bord Avicole

Dashboard interactif pour l'analyse des performances avicoles.

## 📊 Fonctionnalités

- **Indicateurs de Performance**: Production, efficacité alimentaire, consommation
- **Graphiques Interactifs**: Visualisations comparatives Témoin vs Expérimental
- **Données Détaillées**: Tableaux de données brutes
- **Résumé Exécutif**: Synthèse des améliorations

## 🚀 Déploiement

### Option 1: Streamlit Cloud (Recommandé)

1. **Créer un compte** sur [share.streamlit.io](https://share.streamlit.io)
2. **Connecter votre GitHub** et sélectionner ce repository
3. **Configurer le déploiement**:
   - Main file path: `dashboard_avicole_simple.py`
   - Python version: 3.9+
4. **Déployer** en un clic

### Option 2: Heroku

1. **Installer Heroku CLI**
2. **Créer un Procfile**:
   ```
   web: streamlit run dashboard_avicole_simple.py --server.port=$PORT --server.address=0.0.0.0
   ```
3. **Déployer**:
   ```bash
   heroku create votre-app-name
   git push heroku main
   ```

### Option 3: Local avec Docker

1. **Créer un Dockerfile**:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 8501
   CMD ["streamlit", "run", "dashboard_avicole_simple.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Construire et exécuter**:
   ```bash
   docker build -t dashboard-avicole .
   docker run -p 8501:8501 dashboard-avicole
   ```

## 📦 Installation Locale

```bash
pip install -r requirements.txt
streamlit run dashboard_avicole_simple.py
```

## 📁 Structure du Projet

```
├── dashboard_avicole_simple.py    # Application principale
├── requirements.txt               # Dépendances Python
├── .streamlit/config.toml        # Configuration Streamlit
└── README.md                     # Documentation
```

## 🔧 Configuration

Le dashboard utilise les données avicoles suivantes:
- Consommation alimentaire par période
- Indice de consommation (FCR)
- Indice de production

## 📞 Support

Pour toute question ou problème, consultez la documentation Streamlit ou ouvrez une issue. 