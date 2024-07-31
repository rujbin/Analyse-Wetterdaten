import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Daten laden
data = pd.read_csv('wetterdaten.csv')

# Daten aufbereiten
data['Datum'] = pd.to_datetime(data['Datum'])
data.set_index('Datum', inplace=True)

# Durchschnittstemperatur berechnen
monthly_avg_temp = data['Temperatur'].resample('M').mean()

# Niederschlagsmenge berechnen
monthly_total_precip = data['Niederschlag'].resample('M').sum()

# Visualisierung
plt.figure(figsize=(14, 7))

# Durchschnittstemperatur
plt.subplot(2, 1, 1)
sns.lineplot(data=monthly_avg_temp)
plt.title('Durchschnittstemperatur pro Monat')
plt.xlabel('Monat')
plt.ylabel('Temperatur (°C)')

# Niederschlagsmenge
plt.subplot(2, 1, 2)
sns.barplot(x=monthly_total_precip.index, y=monthly_total_precip.values)
plt.title('Niederschlagsmenge pro Monat')
plt.xlabel('Monat')
plt.ylabel('Niederschlag (mm)')

plt.tight_layout()
plt.show()
