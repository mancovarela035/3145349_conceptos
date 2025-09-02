import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("usuarios_limpiesa.csv")

# Eliminar filas donde la edad está vacía
df = df.dropna(subset=["edad"])

# Convertir edad a numérica
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
df = df.dropna(subset=["edad"])

# Crear boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x="pais", y="edad", data=df, palette="pastel")

# Personalizar gráfico
plt.title("Distribución de edades por país", fontsize=14)
plt.xlabel("País")
plt.ylabel("Edad")
plt.xticks(rotation=45)


plt.show()
