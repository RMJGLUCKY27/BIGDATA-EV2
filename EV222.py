import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.ticker import FormatStrFormatter

# Configuración para caracteres en español
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# Cargar los datos (asumiendo que ya tienes un CSV o DataFrame preparado)
# Si no tienes los datos, deberás ajustar esta parte
try:
    df_gas = pd.read_csv('tarifas_gas.csv')
except FileNotFoundError:
    # Datos de ejemplo si no existe el archivo
    # Creamos datos simulados para dos años
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    
    # Tarifas para 2021 y 2022 (simuladas)
    np.random.seed(42)  # Para reproducibilidad
    tarifas_2021 = np.random.uniform(18, 25, 12)  # Valores entre 18 y 25
    tarifas_2022 = tarifas_2021 * np.random.uniform(1.05, 1.15, 12)  # Incremento del 5-15%
    
    # Crear DataFrame
    data = {
        'Mes': meses * 2,
        'Año': [2021] * 12 + [2022] * 12,
        'Tarifa': np.concatenate([tarifas_2021, tarifas_2022])
    }
    df_gas = pd.DataFrame(data)

# 1. Gráfico de línea: Variación de tarifas contra el tiempo para los dos años
plt.figure(figsize=(14, 7))
sns.lineplot(data=df_gas, x='Mes', y='Tarifa', hue='Año', marker='o', linewidth=2.5)
plt.title('Variación de Tarifas de Gas (2021-2022)')
plt.xlabel('Mes')
plt.ylabel('Tarifa (MXN/m³)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Año')
plt.tight_layout()
plt.savefig('variacion_tarifas_gas.png')
plt.close()

# 2. Gráfico de barras: Máximos y mínimos de tarifas por mes para cada año
# Primero calculamos máximos y mínimos por mes
max_min_por_mes = df_gas.groupby(['Año', 'Mes'])['Tarifa'].agg(['min', 'max']).reset_index()

# Crear figura con dos subplots (uno para cada año)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)

# Filtrar datos para cada año
data_2021 = max_min_por_mes[max_min_por_mes['Año'] == 2021]
data_2022 = max_min_por_mes[max_min_por_mes['Año'] == 2022]

# Gráfico para 2021
bar_width = 0.35
x = np.arange(len(data_2021['Mes']))
ax1.bar(x - bar_width/2, data_2021['max'], bar_width, label='Máximo', color='indianred')
ax1.bar(x + bar_width/2, data_2021['min'], bar_width, label='Mínimo', color='skyblue')
ax1.set_title('Tarifas Máximas y Mínimas de Gas por Mes (2021)')
ax1.set_ylabel('Tarifa (MXN/m³)')
ax1.set_xticks(x)
ax1.set_xticklabels(data_2021['Mes'])
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.7, axis='y')
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# Gráfico para 2022
x = np.arange(len(data_2022['Mes']))
ax2.bar(x - bar_width/2, data_2022['max'], bar_width, label='Máximo', color='indianred')
ax2.bar(x + bar_width/2, data_2022['min'], bar_width, label='Mínimo', color='skyblue')
ax2.set_title('Tarifas Máximas y Mínimas de Gas por Mes (2022)')
ax2.set_xlabel('Mes')
ax2.set_ylabel('Tarifa (MXN/m³)')
ax2.set_xticks(x)
ax2.set_xticklabels(data_2022['Mes'])
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.7, axis='y')
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

plt.tight_layout()
plt.savefig('max_min_tarifas_gas.png')
plt.close()

# 3. Gráfico adicional: Comparación de incremento porcentual entre años
# Calcular promedio mensual por año
promedios = df_gas.groupby(['Mes', 'Año'])['Tarifa'].mean().unstack()
# Calcular incremento porcentual
incremento = ((promedios[2022] - promedios[2021]) / promedios[2021] * 100)

plt.figure(figsize=(14, 7))
sns.barplot(x=incremento.index, y=incremento.values, palette='viridis')
plt.title('Incremento Porcentual en Tarifas de Gas (2021 vs 2022)')
plt.xlabel('Mes')
plt.ylabel('Incremento Porcentual (%)')
plt.axhline(y=0, color='r', linestyle='-', alpha=0.3)
plt.grid(True, linestyle='--', alpha=0.7, axis='y')
plt.tight_layout()
plt.savefig('incremento_porcentual_tarifas.png')
plt.close()

print("Visualizaciones del proyecto de tarifas de gas generadas correctamente.")
