import pandas as pd

CSV_FILE = "data/healthcare_dataset.csv"

df = pd.read_csv(CSV_FILE)

print("Colonnes du CSV :", df.columns.tolist())

duplicates = df.duplicated().sum()
print("Nombre de doublons :", duplicates)

missing = df.isnull().sum().sum()
print("Nombre de valeurs manquantes :", missing)