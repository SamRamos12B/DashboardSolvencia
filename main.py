import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from io import StringIO

# Función para cargar los datos desde GitHub
@st.cache_data
def load_data():
    # URL del archivo CSV en GitHub (asegúrate de usar la URL del archivo raw)
    url = "https://raw.githubusercontent.com/SamRamos12B/DashboardSolvencia/refs/heads/main/Datos_proyecto_limpio.csv"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = StringIO(response.text)
        df = pd.read_csv(data)
        return df
    except requests.exceptions.RequestException as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame()

# Cargar datos
df = load_data()

# Verificar si el DataFrame está vacío
if df.empty:
    st.warning("No se pudieron cargar los datos. Por favor, verifica la conexión y la URL del archivo.")
    st.stop()

## Configuración de la página
#st.set_page_config(page_title="Dashboard Financiero", layout="wide")

# Título
st.title("Dashboard de Análisis Financiero")

# Filtros en la barra lateral
st.sidebar.header("Filtros")

# Filtro de Industria
industrias = ['Todas'] + sorted(df['Industry'].unique().tolist())
industria_seleccionada = st.sidebar.selectbox("Seleccionar Industria", industrias)

# Filtro de País
paises = ['Todos'] + sorted(df['Country'].unique().tolist())
pais_seleccionado = st.sidebar.selectbox("Seleccionar País", paises)

# Filtro de Tamaño de Empresa
tamaños = ['Todos'] + sorted(df['Company_Size'].unique().tolist())
tamaño_seleccionado = st.sidebar.selectbox("Seleccionar Tamaño de Empresa", tamaños)

# Aplicar filtros
df_filtered = df.copy()
if industria_seleccionada != 'Todas':
    df_filtered = df_filtered[df_filtered['Industry'] == industria_seleccionada]
if pais_seleccionado != 'Todos':
    df_filtered = df_filtered[df_filtered['Country'] == pais_seleccionado]
if tamaño_seleccionado != 'Todos':
    df_filtered = df_filtered[df_filtered['Company_Size'] == tamaño_seleccionado]

# Métricas generales
st.header("Métricas Generales")
col1, col2 = st.columns(2)
col1.metric("Número de Empresas", len(df_filtered))
col2.metric("Ingresos Totales Promedio", f"${df_filtered['Total_Revenue'].mean():,.0f}")

# Visualizaciones
st.header("Análisis de Ratios Financieros")

# Gráfico de dispersión: Current Ratio vs Debt to Equity Ratio
fig_scatter = px.scatter(df_filtered, x="Current_Assets", y="Current_Liabilities", 
                         color="Industry", hover_name="Company_ID", 
                         title="Current Ratio")
st.plotly_chart(fig_scatter, use_container_width=True)

# Gráfico de dispersión: Current Ratio vs Debt to Equity Ratio
fig_scatter = px.scatter(df_filtered, x="Current_Ratio", y="Debt_to_Equity_Ratio", 
                         color="Industry", hover_name="Company_ID", 
                         title="Current Ratio vs Debt to Equity Ratio")
st.plotly_chart(fig_scatter, use_container_width=True)

# Gráfico de barras: Interest Coverage Ratio promedio por Industria
avg_icr_by_industry = df_filtered.groupby('Industry')['Interest_Coverage_Ratio'].mean().sort_values(ascending=False)
fig_bar = px.bar(avg_icr_by_industry, x=avg_icr_by_industry.index, y=avg_icr_by_industry.values,
                 title="Interest Coverage Ratio Promedio por Industria",
                 labels={'y': ''})
st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico de barras: Interest Coverage Ratio promedio por País
avg_icr_by_industry = df_filtered.groupby('Country')['Interest_Coverage_Ratio'].mean().sort_values(ascending=False)
fig_bar = px.bar(avg_icr_by_industry, x=avg_icr_by_industry.index, y=avg_icr_by_industry.values,
                 title="Interest Coverage Ratio Promedio por Industria",
                 labels={'y': ''})
st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico de caja: Distribución de Current Ratio por Tamaño de Empresa
fig_box = px.box(df_filtered, x="Company_Size", y="Current_Ratio", 
                 title="Distribución de Current Ratio por Tamaño de Empresa")
st.plotly_chart(fig_box, use_container_width=True)

# Gráfico de caja: Distribución de Current Ratio por País
fig_box = px.box(df_filtered, x="Country", y="Current_Ratio", 
                 title="Distribución de Current Ratio por País")
st.plotly_chart(fig_box, use_container_width=True)

# Tabla de las 10 mejores empresas según el Interest Coverage Ratio
st.header("Top 10 Empresas por Interest Coverage Ratio")
top_10_icr = df_filtered.nlargest(10, 'Interest_Coverage_Ratio')[['Company_ID', 'Industry', 'Country', 'Interest_Coverage_Ratio']]
st.table(top_10_icr)

# Análisis de correlación
st.header("Matriz de Correlación")
correlation_matrix = df_filtered[['Current_Ratio', 'Debt_to_Equity_Ratio', 'Interest_Coverage_Ratio']].corr()
fig_heatmap = px.imshow(correlation_matrix, text_auto=True, aspect="auto",
                        title="Correlación entre Ratios Financieros")
st.plotly_chart(fig_heatmap, use_container_width=True)