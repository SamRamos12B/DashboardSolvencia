# Dashboard de Análisis Financiero

Este dashboard de Streamlit proporciona un análisis interactivo de datos financieros de empresas, permitiendo a los usuarios explorar y comparar ratios financieros clave a través de diferentes industrias, países y tamaños de empresa.

## Características

- **Carga de datos dinámica**: Los datos se cargan automáticamente desde un archivo CSV alojado en GitHub.
- **Filtros interactivos**: Los usuarios pueden filtrar los datos por industria, país y tamaño de empresa.
- **Métricas generales**: Muestra el número de empresas, ingresos totales promedio y ratio de deuda a patrimonio promedio.
- **Visualizaciones interactivas**:
  - Gráfico de dispersión: Current Ratio vs Debt to Equity Ratio
  - Gráfico de barras: Interest Coverage Ratio promedio por Industria
  - Gráfico de caja: Distribución de Current Ratio por Tamaño de Empresa
- **Tabla de Top 10**: Muestra las 10 mejores empresas según el Interest Coverage Ratio
- **Matriz de Correlación**: Visualiza la correlación entre diferentes ratios financieros

## Requisitos

- Python 3.7+
- Streamlit
- Pandas
- Plotly
- Requests

## Instalación

1. Clone este repositorio:
   ```
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Instale las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Asegúrese de que su archivo CSV esté alojado en GitHub y actualice la URL en la función `load_data()` del script.

2. Ejecute el dashboard con:
   ```
   streamlit run main.py
   ```

3. Abra su navegador y vaya a `https://dashboardsolvenciasam.streamlit.app/` para ver el dashboard.

## Estructura de datos

El dashboard espera un archivo CSV con las siguientes columnas:

- Company_ID
- Total_Revenue
- Short_Term_Debt
- Long_Term_Debt
- Current_Assets
- Current_Liabilities
- Equity
- Financial_Expenses
- Current_Ratio
- Debt_to_Equity_Ratio
- Interest_Coverage_Ratio
- Industry
- Country
- Company_Size

## Personalización

Puede personalizar el dashboard modificando el script `main.py`. Algunas ideas para extender la funcionalidad incluyen:

- Agregar más visualizaciones o métricas financieras
- Implementar la capacidad de descargar datos filtrados
- Añadir análisis de tendencias temporales si los datos lo permiten

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de enviar un pull request.

## Intehgración con ChatGPT

Se pueden hacer preguntas sobre análisis financiero.
