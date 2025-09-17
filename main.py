import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="Minha Viagem para Holambra",
    page_icon="🌷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado seguindo Material Design
st.markdown("""
<style>
    /* Material Design inspirado - cores e tipografia */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .section-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 0.5rem;
    }
    
    .image-placeholder {
        background: linear-gradient(45deg, #f0f2f6, #e1e5e9);
        border: 2px dashed #9aa0a6;
        border-radius: 8px;
        padding: 2rem;
        text-align: center;
        color: #5f6368;
        margin: 1rem 0;
    }
    
    .story-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid #e8eaed;
    }
    
    .highlight-text {
        color: #667eea;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("""
<div class="main-header">
    <h1>🌷 Nossa Viagem Inesquecível para Holambra</h1>
    <h3>Uma experiência única na Cidade das Flores</h3>
    <p>Descobrindo a cultura holandesa no coração de São Paulo</p>
</div>
""", unsafe_allow_html=True)

# Informações básicas da viagem (sidebar)
st.sidebar.markdown("### 📋 Informações da Viagem")
st.sidebar.info("""
**Destino:** Holambra, SP  
**Duração:** 3 dias  
**Estação:** Inverno -> Primavera  
**Companhia:** Minha namorada incrível e maravilhosa❤️  
**Tema:** Cultura holandesa e flores
""")

# Conteúdo principal da página inicial
# Seção de introdução
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="section-card">
        <h2>Por que Holambra?</h2>
        <p>Nossa escolha por Holambra não foi apenas pelo destino, mas pela experiência única que queríamos compartilhar juntos. 
        A <span class="highlight-text">Cidade das Flores</span> nos prometia uma imersão na cultura holandesa sem sair do Brasil, 
        e foi exatamente isso que encontramos!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Imagem principal da viagem
    st.image("holambra.jpeg", caption="Nossa experiência inesquecível em Holambra 🌷", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
            <h3>🎯 Objetivos da Viagem</h3>
            <ul>
                <li>Conhecer a cultura holandesa</li>
                <li>Relaxar em um ambiente único</li>
                <li>Criar memórias especiais juntos</li>
                <li>Fotografar paisagens incríveis</li>
                <li>Experimentar gastronomia local</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Métricas rápidas
        st.markdown("### 📊 Nossa Viagem em Números")
        
        # Métricas reais da viagem
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric("🚶‍♂️ Distância Caminhada", "36 KM", "por pessoa em 3 dias")
        with col_m2:
            st.metric("📸 Fotos Capturadas", "247", "memórias registradas")
        with col_m3:
            st.metric("📍 Pontos Visitados", "12", "locais especiais")

# Seção de gráficos e análises
st.markdown("---")
st.markdown("## 📊 Holambra em Dados: Nossa Experiência Quantificada")

# Primeiro conjunto de gráficos
col1, col2 = st.columns(2)

with col1:
    # Gráfico: Composição populacional (Turistas vs Nativos)
    st.markdown("### 👥 População da Cidade")
    pop_data = pd.DataFrame({
        'Categoria': ['Turistas', 'Moradores Locais'],
        'Porcentagem': [80, 20],
        'Pessoas': [4800, 1200]
    })
    
    fig_pop = px.pie(pop_data, values='Porcentagem', names='Categoria', 
                     title="Distribuição Populacional Durante Nossa Visita",
                     color_discrete_sequence=['#ff6b6b', '#4ecdc4'])
    fig_pop.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pop, use_container_width=True)

with col2:
    # Gráfico: Faixa etária da população
    st.markdown("### 👴 Perfil Etário da População")
    idade_data = pd.DataFrame({
        'Faixa Etária': ['0-17 anos', '18-39 anos', '40-59 anos', '60+ anos'],
        'Porcentagem': [8, 22, 25, 45]
    })
    
    fig_idade = px.bar(idade_data, x='Faixa Etária', y='Porcentagem',
                       title="Distribuição por Idade dos Moradores",
                       color='Porcentagem',
                       color_continuous_scale='Viridis')
    fig_idade.update_layout(showlegend=False)
    st.plotly_chart(fig_idade, use_container_width=True)

# Segunda linha de gráficos
col3, col4 = st.columns(2)

with col3:
    # Gráfico: Horários de funcionamento dos estabelecimentos
    st.markdown("### 🕐 Horários de Funcionamento")
    horarios_data = pd.DataFrame({
        'Tipo de Estabelecimento': ['Restaurantes', 'Cafés', 'Lojas de Souvenirs', 
                                  'Museus', 'Atrações Turísticas', 'Mercados'],
        'Fechamento': [19, 18, 17, 16, 18, 19],
        'Cor': ['#ff7675', '#fd79a8', '#fdcb6e', '#6c5ce7', '#74b9ff', '#00b894']
    })
    
    fig_horarios = px.bar(horarios_data, x='Tipo de Estabelecimento', y='Fechamento',
                         title="Horário de Fechamento dos Estabelecimentos",
                         color='Tipo de Estabelecimento',
                         color_discrete_sequence=horarios_data['Cor'])
    fig_horarios.update_layout(showlegend=False, xaxis_tickangle=-45)
    fig_horarios.add_hline(y=19, line_dash="dash", line_color="red", 
                          annotation_text="Maioria fecha antes das 19h")
    st.plotly_chart(fig_horarios, use_container_width=True)

with col4:
    # Gráfico: Influência cultural holandesa
    st.markdown("### 🇳🇱 Influência Cultural Holandesa")
    cultura_data = pd.DataFrame({
        'Aspecto Cultural': ['Arquitetura', 'Gastronomia', 'Festivais', 
                           'Idioma (Placas)', 'Decoração', 'Música/Arte'],
        'Intensidade (1-10)': [9, 8, 10, 7, 9, 6],
        'Observado': ['Moinhos, casas típicas', 'Stroopwafels, queijos', 
                     'Festival das Flores', 'Placas bilíngues', 
                     'Tulipas, cores típicas', 'Música tradicional']
    })
    
    fig_cultura = px.bar(cultura_data, x='Intensidade (1-10)', y='Aspecto Cultural',
                        orientation='h',
                        title="Intensidade da Influência Holandesa",
                        color='Intensidade (1-10)',
                        color_continuous_scale='RdYlBu_r')
    fig_cultura.update_layout(showlegend=False)
    st.plotly_chart(fig_cultura, use_container_width=True)

# Gráfico de caminhada ao longo dos dias
st.markdown("### 🚶‍♂️ Nossa Jornada de Caminhada")
caminhada_data = pd.DataFrame({
    'Dia': ['Dia 1 - Sexta', 'Dia 2 - Sábado', 'Dia 3 - Domingo'],
    'Casal (km)': [10, 15, 11],  # Variação mantendo total de 36km
    'Principais Locais': [
        'Centro histórico, Moinho Povos Unidos',
        'Campos de flores, Museu da Imigração, Parque',
        'Mercado de flores, Restaurantes, Despedida'
    ]
})

fig_caminhada = go.Figure()
fig_caminhada.add_trace(go.Scatter(x=caminhada_data['Dia'], y=caminhada_data['Casal (km)'],
                                  mode='lines+markers', name='Casal',
                                  line=dict(color='#667eea', width=4),
                                  marker=dict(size=12, color='#f093fb')))

fig_caminhada.update_layout(
    title="Quilômetros Caminhados por Dia pelo Casal",
    xaxis_title="Dias da Viagem",
    yaxis_title="Distância (km)",
    hovermode='x unified',
    showlegend=False
)

# Adicionar anotações com os locais visitados
for i, row in caminhada_data.iterrows():
    fig_caminhada.add_annotation(
        x=row['Dia'],
        y=row['Casal (km)'] + 1,
        text=row['Principais Locais'],
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=0,
        ay=-30,
        font=dict(size=10)
    )

st.plotly_chart(fig_caminhada, use_container_width=True)

# Mapa dos pontos visitados com rotas simuladas
st.markdown("### 🗺️ Nosso Roteiro por Holambra")
pontos_turisticos = pd.DataFrame({
    'Local': ['Centro Histórico', 'Moinho Povos Unidos', 'Campos de Flores', 
              'Museu da Imigração', 'Mercado de Flores', 'Parque Ecológico',
              'Restaurante Het Klooster', 'Casa do Chocolate'],
    'Lat': [-22.6317, -22.6300, -22.6280, -22.6335, -22.6290, -22.6350, -22.6310, -22.6295],
    'Lon': [-47.0530, -47.0520, -47.0500, -47.0540, -47.0515, -47.0560, -47.0525, -47.0535],
    'Tipo': ['Histórico', 'Atração', 'Natural', 'Cultural', 'Comercial', 'Lazer', 'Gastronomia', 'Gastronomia'],
    'Visitado_Dia': [1, 1, 2, 2, 3, 2, 1, 3],
    'Ordem_Visita': [1, 2, 4, 5, 8, 6, 3, 7]
})

# Criar o mapa com pontos
fig_mapa = go.Figure()

# Adicionar pontos por dia
cores_dias = {1: '#ff6b6b', 2: '#4ecdc4', 3: '#45b7d1'}
for dia in [1, 2, 3]:
    pontos_dia = pontos_turisticos[pontos_turisticos['Visitado_Dia'] == dia]
    fig_mapa.add_trace(go.Scattermapbox(
        lat=pontos_dia['Lat'],
        lon=pontos_dia['Lon'],
        mode='markers+text',
        marker=dict(size=15, color=cores_dias[dia]),
        text=pontos_dia['Local'],
        textposition="top center",
        name=f'Dia {dia}',
        hovertemplate='<b>%{text}</b><br>Tipo: %{customdata}<extra></extra>',
        customdata=pontos_dia['Tipo']
    ))

# Tentar simular rotas conectando pontos do mesmo dia
for dia in [1, 2, 3]:
    pontos_dia = pontos_turisticos[pontos_turisticos['Visitado_Dia'] == dia].sort_values('Ordem_Visita')
    if len(pontos_dia) > 1:
        # Adicionar linhas conectando os pontos na ordem de visita
        fig_mapa.add_trace(go.Scattermapbox(
            lat=pontos_dia['Lat'],
            lon=pontos_dia['Lon'],
            mode='lines',
            line=dict(width=3, color=cores_dias[dia]),
            name=f'Rota Dia {dia}',
            hoverinfo='skip'
        ))

fig_mapa.update_layout(
    mapbox=dict(
        style="open-street-map",
        center=dict(lat=-22.6317, lon=-47.0530),
        zoom=13
    ),
    height=500,
    margin={"r":0,"t":30,"l":0,"b":0},
    title="Pontos Turísticos Visitados com Rotas Aproximadas"
)

st.plotly_chart(fig_mapa, use_container_width=True)

# Adicionar legenda explicativa
st.markdown("""
**Legenda do Mapa:**
- 🔴 **Dia 1 (Sexta)**: Centro Histórico → Moinho Povos Unidos → Restaurante Het Klooster
- 🟢 **Dia 2 (Sábado)**: Campos de Flores → Museu da Imigração → Parque Ecológico  
- 🔵 **Dia 3 (Domingo)**: Casa do Chocolate → Mercado de Flores

*As linhas representam rotas aproximadas entre os pontos visitados em cada dia.*
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #5f6368; padding: 1rem;">
    <p>🌷 Holambra - Uma experiência inesquecível • Criado com ❤️ e Streamlit</p>
</div>
""", unsafe_allow_html=True)