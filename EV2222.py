import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración para caracteres en español
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# Cargar los datos (asumiendo que ya tienes un CSV o DataFrame preparado)
# Si no tienes los datos, deberás ajustar esta parte
try:
    df_guarderias = pd.read_csv('datos_guarderias.csv')
except FileNotFoundError:
    # Datos de ejemplo si no existe el archivo
    data = {
        'Estado': ['Chihuahua', 'CDMX', 'Jalisco', 'Nuevo León', 'Puebla'],
        'Num_Guarderias': [45, 120, 78, 65, 52],
        'Participacion_Padres': [78, 65, 82, 75, 68],
        'Calificacion_Servicio': [8.5, 7.9, 8.2, 8.7, 7.8]
    }
    df_guarderias = pd.DataFrame(data)

# 1. Gráfico de barras: Número de guarderías por estado
plt.figure(figsize=(12, 6))
sns.barplot(x='Estado', y='Num_Guarderias', data=df_guarderias)
plt.title('Número de Guarderías por Estado')
plt.xlabel('Estado')
plt.ylabel('Número de Guarderías')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('guarderias_por_estado.png')
plt.close()

# 2. Gráfico de líneas: Participación de padres por estado
plt.figure(figsize=(12, 6))
sns.lineplot(x='Estado', y='Participacion_Padres', data=df_guarderias, marker='o')
plt.title('Nivel de Participación de Padres por Estado')
plt.xlabel('Estado')
plt.ylabel('Porcentaje de Participación')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('participacion_padres.png')
plt.close()

# 3. Gráfico de pastel: Distribución de guarderías
plt.figure(figsize=(10, 10))
plt.pie(df_guarderias['Num_Guarderias'], labels=df_guarderias['Estado'], autopct='%1.1f%%')
plt.title('Distribución de Guarderías por Estado')
plt.axis('equal')
plt.tight_layout()
plt.savefig('distribucion_guarderias.png')
plt.close()

# 4. Gráfico de dispersión: Relación entre participación y calificación
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Participacion_Padres', y='Calificacion_Servicio', 
                data=df_guarderias, s=100, hue='Estado')
plt.title('Relación entre Participación de Padres y Calificación del Servicio')
plt.xlabel('Porcentaje de Participación de Padres')
plt.ylabel('Calificación del Servicio (1-10)')
plt.tight_layout()
plt.savefig('relacion_participacion_calificacion.png')
plt.close()

print("Visualizaciones del proyecto de guarderías generadas correctamente.")