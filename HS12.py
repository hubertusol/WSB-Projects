import pandas as pd

# Wczytaj dane
csv = input("Prosze wpisac nazwe pliku")
df = pd.read_csv(csv)

# Wyświetl pierwsze 5 wierszy
print(df.head())

# Oblicz podstawowe statystyki
print(df.describe())
