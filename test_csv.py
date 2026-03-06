import pandas as pd

# Chemin du CSV
CSV_FILE = "data/healthcare_dataset.csv"

# Lire le CSV
df = pd.read_csv(CSV_FILE)

# Afficher les colonnes
print("Colonnes du CSV :", df.columns.tolist())