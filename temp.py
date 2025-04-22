import pandas as pd
from scipy import stats


#datei einlesen
dateipfad = "wetter.csv"
df = pd.read_csv(dateipfad)
print(df.head()) #ersten Zeilen sehen

#sicherstellen, dass datum-spalte im datumsformat ist
df['Datum'] = pd.to_datetime(df['Datum'])
#durschchnittstemperatur berechnen, über gesamten zeitraum
durchschnitt_temp = df['Temperatur'].mean()
print(f"Durchschnittstemperatur über den gesamten Zeitraum: {durchschnitt_temp:.2f}°C")

#nur durschnittstemperatur für juli
df_juli = df[df['Datum'].dt.month == 7] #alle zeilen aus df, bei denen monat in datum-spalte 7
durchschnitt_temp_juli = df_juli['Temperatur'].mean()
print(f"Durchschnittstemperatur im Juli: {durchschnitt_temp_juli:.2f}°C")

#durschnittstemperatur für mai
df_mai = df[df['Datum'].dt.month == 5 ] 
durchschnitt_temp_mai = df_mai['Temperatur'].mean()
print(f"Durchschnittstemperatur im Mai: {durchschnitt_temp_mai:.2f}°C")

#führe t-test durch
t_stat, p_value = stats.ttest_ind(df_juli['Temperatur'], df_mai['Temperatur'])
print(f"T-Statistik: {t_stat:.2f}")
print(f"P-Wert: {p_value:.5f}")

alpha = 0.05# Signifikanzniveau
#intperpretation des p-wertes
if p_value < alpha: #p wert kleiner als alpha bedeutet, dass wkeit, dass unterschiede zufällig sind, kleiner ist als 5%, sehr gering
    
    print("Die Durchschnittstemperaturen im Juli und Mai sind signifikant unterschiedlich.")
else:#p wert größer als alpha bedeutet, dass unterschied zufällig sein könnte
    print("Die Durchschnittstemperaturen im Juli und Mai sind nicht signifikant unterschiedlich.")
    
    
# signifikant heißt, dass die Differenz zwischen den Mittelwerten der beiden Gruppen (Juli und Mai) nicht zufällig ist und dass es einen echten Unterschied zwischen den beiden Gruppen gibt.