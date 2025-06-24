import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="Tableau de Bord Avicole",
    page_icon="🐔",
    layout="wide"
)

# CSS simple pour le style
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1rem;
    }
    .metric-value {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Données
@st.cache_data
def charger_donnees():
    """Charger les données avicoles"""
    
    # Données de consommation
    consommation_data = {
        'Période': ['J1-J7', 'J8-J14', 'J15-J21', 'J22-J28', 'J29-J35'],
        'Témoin': [21.7052, 56.5248, 105.58301, 133.072, 191.2561],
        'Expérimental': [21.6918, 56.4047, 104.7441, 131.1144, 202.19]
    }

    # Données d'indice de consommation
    ic_data = {
        'Période': ['J1-J7', 'J8-J14', 'J15-J21', 'J22-J28', 'J29-J35'],
        'Témoin': [1.216, 1.269, 1.9449, 1.901, 3.3554],
        'Expérimental': [1.1909, 1.1716, 1.5237, 1.765, 3.1113]
    }

    # Données d'indice de production
    ip_data = {
        'Groupe': ['Témoin', 'Expérimental'],
        'Indice_Production': [339.2795496, 421.4806928]
    }

    return pd.DataFrame(consommation_data), pd.DataFrame(ic_data), pd.DataFrame(ip_data)

# Charger les données
df_consommation, df_ic, df_ip = charger_donnees()

# Calculer les KPIs
def calculer_kpis():
    """Calculer les indicateurs clés de performance"""
    
    # Consommation finale
    cons_finale_t = df_consommation.iloc[-1]['Témoin']
    cons_finale_e = df_consommation.iloc[-1]['Expérimental']
    diff_cons = ((cons_finale_e - cons_finale_t) / cons_finale_t) * 100

    # Indice de consommation moyen
    ic_moyen_t = df_ic['Témoin'].mean()
    ic_moyen_e = df_ic['Expérimental'].mean()
    amelioration_ic = ((ic_moyen_t - ic_moyen_e) / ic_moyen_t) * 100

    # Indice de production
    ip_t = df_ip.iloc[0]['Indice_Production']
    ip_e = df_ip.iloc[1]['Indice_Production']
    amelioration_ip = ((ip_e - ip_t) / ip_t) * 100
    
    return {
        'cons_finale_t': cons_finale_t,
        'cons_finale_e': cons_finale_e,
        'diff_cons': diff_cons,
        'ic_moyen_t': ic_moyen_t,
        'ic_moyen_e': ic_moyen_e,
        'amelioration_ic': amelioration_ic,
        'ip_t': ip_t,
        'ip_e': ip_e,
        'amelioration_ip': amelioration_ip
    }

kpis = calculer_kpis()

# Titre principal
st.markdown('<h1 class="main-header">🐔 Tableau de Bord Avicole</h1>', unsafe_allow_html=True)

# Indicateurs clés
st.subheader("📊 Indicateurs Clés de Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f'''
    <div class="metric-container">
        <div class="metric-value">+{kpis['amelioration_ip']:.1f}%</div>
        <div>Amélioration Indice de Production</div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <div class="metric-container">
        <div class="metric-value">+{kpis['amelioration_ic']:.1f}%</div>
        <div>Amélioration Efficacité Alimentaire</div>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
    <div class="metric-container">
        <div class="metric-value">{kpis['diff_cons']:+.1f}%</div>
        <div>Évolution Consommation Finale</div>
    </div>
    ''', unsafe_allow_html=True)

with col4:
    st.markdown(f'''
    <div class="metric-container">
        <div class="metric-value">{kpis['ip_e']:.0f}</div>
        <div>Indice de Production Expérimental</div>
    </div>
    ''', unsafe_allow_html=True)

# Onglets
tab1, tab2, tab3 = st.tabs(["📈 Graphiques", "📋 Données", "📊 Résumé"])

with tab1:
    st.subheader("📈 Graphiques de Performance")
    
    # Graphique 1: Consommation alimentaire
    st.markdown("### Consommation Alimentaire (g/poulet/jour)")
    
    fig_cons = go.Figure()
    fig_cons.add_trace(go.Bar(
        x=df_consommation['Période'],
        y=df_consommation['Témoin'],
        name='Témoin',
        marker_color='#2E86C1'
    ))
    fig_cons.add_trace(go.Bar(
        x=df_consommation['Période'],
        y=df_consommation['Expérimental'],
        name='Expérimental',
        marker_color='#E74C3C'
    ))
    
    fig_cons.update_layout(
        title="Évolution de la Consommation Alimentaire",
        xaxis_title="Période",
        yaxis_title="Consommation (g/jour)",
        height=400
    )
    
    st.plotly_chart(fig_cons, use_container_width=True)
    
    # Graphique 2: Indice de consommation
    st.markdown("### Indice de Consommation (g aliment/g poids)")
    
    fig_ic = go.Figure()
    fig_ic.add_trace(go.Scatter(
        x=df_ic['Période'],
        y=df_ic['Témoin'],
        name='Témoin',
        line=dict(color='#2E86C1', width=3),
        mode='lines+markers'
    ))
    fig_ic.add_trace(go.Scatter(
        x=df_ic['Période'],
        y=df_ic['Expérimental'],
        name='Expérimental',
        line=dict(color='#E74C3C', width=3),
        mode='lines+markers'
    ))
    
    fig_ic.update_layout(
        title="Évolution de l'Indice de Consommation",
        xaxis_title="Période",
        yaxis_title="Indice de Consommation",
        height=400
    )
    
    st.plotly_chart(fig_ic, use_container_width=True)
    
    # Graphique 3: Indice de production
    st.markdown("### Indice de Production")
    
    fig_ip = go.Figure()
    fig_ip.add_trace(go.Bar(
        x=df_ip['Groupe'],
        y=df_ip['Indice_Production'],
        marker_color=['#2E86C1', '#E74C3C']
    ))
    
    fig_ip.update_layout(
        title="Comparaison des Indices de Production",
        xaxis_title="Groupe",
        yaxis_title="Indice de Production",
        height=400
    )
    
    # Ajouter annotation d'amélioration
    fig_ip.add_annotation(
        x=0.5,
        y=df_ip['Indice_Production'].max() + 20,
        text=f"Amélioration: +{kpis['amelioration_ip']:.1f}%",
        showarrow=False,
        font=dict(size=14, color='green'),
        bgcolor='lightgreen'
    )
    
    st.plotly_chart(fig_ip, use_container_width=True)

with tab2:
    st.subheader("📋 Données Détaillées")
    
    # Tableau de consommation
    st.markdown("### Consommation Alimentaire")
    st.dataframe(df_consommation, use_container_width=True)
    
    # Tableau d'indice de consommation
    st.markdown("### Indice de Consommation")
    st.dataframe(df_ic, use_container_width=True)
    
    # Tableau d'indice de production
    st.markdown("### Indice de Production")
    st.dataframe(df_ip, use_container_width=True)

with tab3:
    st.subheader("📊 Résumé Exécutif")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Performances Clés")
        st.markdown(f"""
        **Indice de Production:**
        - Témoin: {kpis['ip_t']:.1f}
        - Expérimental: {kpis['ip_e']:.1f}
        - Amélioration: **+{kpis['amelioration_ip']:.1f}%**
        
        **Efficacité Alimentaire:**
        - IC moyen Témoin: {kpis['ic_moyen_t']:.3f}
        - IC moyen Expérimental: {kpis['ic_moyen_e']:.3f}
        - Amélioration: **+{kpis['amelioration_ic']:.1f}%**
        """)
    
    with col2:
        st.markdown("### 📈 Consommation")
        st.markdown(f"""
        **Consommation Finale (J29-J35):**
        - Témoin: {kpis['cons_finale_t']:.1f} g/jour
        - Expérimental: {kpis['cons_finale_e']:.1f} g/jour
        - Évolution: **{kpis['diff_cons']:+.1f}%**
        
        **Analyse:**
        - Performance globale positive
        - Amélioration significative de la production
        - Meilleure efficacité alimentaire
        """)
    
    # Tableau récapitulatif
    st.markdown("### 📋 Tableau Récapitulatif")
    
    resume_data = {
        'Indicateur': [
            'Consommation Finale (J29-J35)',
            'Indice de Consommation Moyen',
            'Indice de Production'
        ],
        'Témoin': [
            f"{kpis['cons_finale_t']:.1f} g/j",
            f"{kpis['ic_moyen_t']:.3f}",
            f"{kpis['ip_t']:.1f}"
        ],
        'Expérimental': [
            f"{kpis['cons_finale_e']:.1f} g/j",
            f"{kpis['ic_moyen_e']:.3f}",
            f"{kpis['ip_e']:.1f}"
        ],
        'Évolution': [
            f"{kpis['diff_cons']:+.1f}%",
            f"{kpis['amelioration_ic']:+.1f}%",
            f"{kpis['amelioration_ip']:+.1f}%"
        ]
    }
    
    df_resume = pd.DataFrame(resume_data)
    st.dataframe(df_resume, use_container_width=True)

# Pied de page
st.markdown("---")
st.markdown("🐔 Tableau de Bord Avicole - Créé avec Streamlit") 