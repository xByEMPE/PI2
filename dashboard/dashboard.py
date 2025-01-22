import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde archivos
def load_data():
    coverage_data = pd.read_excel("C:/PI2/datasets/mapa_conectividad.xlsx", sheet_name="Hoja3")
    internet_data = pd.read_excel("C:/PI2/datasets/Internet.xlsx", sheet_name="Penetracion-hogares")
    telefonia_data = pd.read_excel("C:/PI2/datasets/Telefonia_movil.xlsx", sheet_name="Ingresos")
    tv_data_access = pd.read_excel("C:/PI2/datasets/Television.xlsx", sheet_name="Accesos_totales_TV")
    tv_data_revenue = pd.read_excel("C:/PI2/datasets/Television.xlsx", sheet_name="Ingresos_TV")
    return coverage_data, internet_data, telefonia_data, tv_data_access, tv_data_revenue

# Procesar datos para KPIs
def process_kpis(coverage_data, internet_data, telefonia_data, tv_data_access, tv_data_revenue):
    # Índice de Cobertura
    advanced_technologies = ['Fibra óptica', '4G']
    coverage_data['Provincia'] = coverage_data['Provincia'].astype(str)
    for tech in advanced_technologies:
        coverage_data[f'{tech} Access'] = coverage_data[tech] == 'SI'
    coverage_kpi = coverage_data.groupby('Provincia')[
        [f'{tech} Access' for tech in advanced_technologies]
    ].mean() * 100

    # Proyección de Internet
    internet_data['Projected Access (Next Quarter)'] = internet_data['Accesos por cada 100 hogares'] * 1.02
    internet_data['KPI Actual'] = (
        (internet_data['Projected Access (Next Quarter)'] - internet_data['Accesos por cada 100 hogares']) /
        internet_data['Accesos por cada 100 hogares']
    ) * 100

    # Telefonía Móvil
    telefonia_data['Crecimiento (%)'] = telefonia_data['Ingresos (miles de $)'].pct_change() * 100

    # Datos de TV
    avg_subscription_access = tv_data_access['Accesos TV por suscripción'].mean()
    avg_satelital_access = tv_data_access['Accesos TV satelital'].mean()
    revenue_growth = (
        tv_data_revenue.iloc[-1]['Ingresos TV por suscripción  (miles de $)'] -
        tv_data_revenue.iloc[0]['Ingresos TV por suscripción  (miles de $)']
    ) / tv_data_revenue.iloc[0]['Ingresos TV por suscripción  (miles de $)'] * 100

    tv_kpi = {
        'average_subscription_access': avg_subscription_access,
        'average_satelital_access': avg_satelital_access,
        'revenue_growth': revenue_growth
    }

    return coverage_kpi, internet_data, telefonia_data, tv_kpi

# Dashboard
st.title("Dashboard Interactivo de KPIs")

# Cargar y procesar datos
coverage_data, internet_data, telefonia_data, tv_data_access, tv_data_revenue = load_data()
coverage_kpi, internet_data, telefonia_data, tv_kpi = process_kpis(
    coverage_data, internet_data, telefonia_data, tv_data_access, tv_data_revenue
)

# Índice de Cobertura
st.header("Índice de Cobertura por Provincia")
st.write("Esta sección muestra el índice de cobertura para tecnologías avanzadas (Fibra Óptica y 4G) por provincia.")
bottom_values = [0] * len(coverage_kpi)
colors = ['#1f77b4', '#ff7f0e']
labels = ['Fibra óptica', '4G']
fig, ax = plt.subplots(figsize=(10, 6))
for idx, tech in enumerate(labels):
    ax.barh(coverage_kpi.index, coverage_kpi[f'{tech} Access'],
            left=bottom_values, color=colors[idx], label=tech, edgecolor='black', height=0.7)
    bottom_values = [i + j for i, j in zip(bottom_values, coverage_kpi[f'{tech} Access'])]
ax.set_xlabel('Coverage Index (%)')
ax.set_ylabel('Provincia')
ax.set_title('Coverage Index by Province (Fiber Optic and 4G)')
ax.legend(title='Technology')
ax.grid(axis='x', linestyle='--', alpha=0.5)
st.pyplot(fig)
st.write("""
## Puntos a destacar del KPI
* Provincias con más del 100% en cobertura pueden tener mayor urbanización o inversiones en infraestructura digital.
* Provincias con bajo porcentaje de cobertura podrían ser zonas rurales con baja inversión en infraestructura.

## Posibles acciones
* Identificar regiones prioritarias para expandir tecnologías avanzadas.
* Analizar políticas públicas o inversiones privadas en provincias con altos índices.
* Implementar programas de conectividad en localidades críticas.
""")

# Proyección de Acceso a Internet
st.header("Proyección de Acceso a Internet")
st.write("Proyección del acceso a internet para el próximo trimestre.")
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(internet_data['Provincia'], internet_data['Projected Access (Next Quarter)'], label='Acceso proyectado', color='blue')
ax.barh(internet_data['Provincia'], internet_data['Accesos por cada 100 hogares'], label='Acceso actual', color='orange', alpha=0.7)
ax.set_xlabel('Acceso por cada 100 hogares')
ax.set_ylabel('Provincia')
ax.set_title('Proyectado vs Acceso actual por cada 100 hogares por provincia')
ax.legend()
ax.grid(axis='x', linestyle='--', alpha=0.7)
st.pyplot(fig)
st.write("""
- Este gráfico muestra la comparación entre el acceso actual y el proyectado con un aumento del 2% para el próximo trimestre.
""")

# Crecimiento de Ingresos en Telefonía Móvil
st.header("Crecimiento de Ingresos en Telefonía Móvil")
st.write("Crecimiento trimestral de ingresos para telefonía móvil.")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(telefonia_data['Periodo'], telefonia_data['Crecimiento (%)'], marker='o', label="Crecimiento (%)")
ax.axhline(0, color='red', linestyle='--', label='Crecimiento = 0%')
ax.set_title("Evolución trimestral del crecimiento de ingresos (%)")
ax.set_xlabel("Periodo")
ax.set_ylabel("Crecimiento (%)")
ax.legend()
ax.grid(True)
st.pyplot(fig)
st.write("""
## Análisis del KPI
- Los valores negativos indican una disminución en los ingresos respecto al trimestre anterior.

### Posibles causas:
* Estacionalidad.
* Factores económicos.
* Competencia.
* Inconsistencias o errores en los datos.
""")

# KPIs de Televisión
st.header("KPIs de Televisión")
st.write("Indicadores clave de desempeño para los servicios de televisión.")
kpi_names = ['Promedio Accesos Suscripción', 'Promedio Accesos Satelital']
kpi_values = [
    tv_kpi['average_subscription_access'],
    tv_kpi['average_satelital_access']
]
growth_value = tv_kpi['revenue_growth']
fig, ax1 = plt.subplots(figsize=(8, 5))
# Gráfica de barras
bars = ax1.bar(kpi_names, kpi_values, color=['blue', 'green'], label="Accesos Promedio")
ax1.set_ylabel('Accesos Promedio')
ax1.set_title('Indicadores Clave de Desempeño (KPI)')
# Línea de crecimiento
ax2 = ax1.twinx()
ax2.plot(['Crecimiento Ingresos (%)'], [growth_value], color='orange', marker='o', markersize=10, label="Crecimiento Ingresos (%)")
ax2.set_ylabel('Crecimiento Ingresos (%)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
st.pyplot(fig)
st.write("""
## Puntos clave en este KPI:

### Promedio de acceso TV por suscripción:
* Un número alto indica alta adopción de este servicio.
* Estrategias podrían enfocarse en retener clientes mediante promociones o mejoras en el servicio.

### Promedio de accesos TV satelital:
* Un número más bajo puede reflejar un mercado limitado, especialmente en áreas rurales.

### Posibles acciones:
* Desarrollar estrategias específicas para áreas rurales con servicios satelitales.
""")
