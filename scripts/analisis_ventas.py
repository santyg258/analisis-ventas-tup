# PROY-2: Script de análisis de ventas
# Importamos las librerías necesarias para el análisis y visualización
import pandas as pd
import matplotlib.pyplot as plt
import os

# Creamos el dataset de ventas simulado
data = {
    'fecha': [
        '2024-01-05', '2024-01-15', '2024-02-03', '2024-02-20',
        '2024-03-10', '2024-03-25', '2024-04-08', '2024-04-22',
        '2024-05-05', '2024-05-18', '2024-06-01', '2024-06-30'
    ],
    'producto': [
        'Laptop', 'Mouse', 'Laptop', 'Teclado',
        'Mouse', 'Laptop', 'Teclado', 'Mouse',
        'Laptop', 'Teclado', 'Mouse', 'Laptop'
    ],
    'cantidad': [2, 5, 1, 3, 8, 2, 4, 6, 3, 2, 7, 1],
    'precio_unitario': [1500, 25, 1500, 45, 25, 1500, 45, 25, 1500, 45, 25, 1500]
}

df = pd.DataFrame(data)
df['fecha'] = pd.to_datetime(df['fecha'])
df['venta_total'] = df['cantidad'] * df['precio_unitario']
df.to_csv('datos/ventas.csv', index=False)
print("Dataset guardado en datos/ventas.csv")

ventas_totales = df['venta_total'].sum()
print(f"\nVentas totales: ${ventas_totales:,.2f}")

producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
print(f"Producto más vendido: {producto_mas_vendido}")

df['mes'] = df['fecha'].dt.to_period('M')
ventas_por_mes = df.groupby('mes')['venta_total'].sum()
print(f"\nVentas por mes:\n{ventas_por_mes}")

plt.figure(figsize=(10, 5))
ventas_por_mes.plot(kind='bar', color='steelblue')
plt.title('Evolución de Ventas por Mes - 2024')
plt.xlabel('Mes')
plt.ylabel('Ventas ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('resultados/grafico_ventas.png')
plt.show()
print("\nGráfico guardado en resultados/grafico_ventas.png")
