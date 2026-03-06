import pandas as pd
from pymongo import MongoClient

# Chemin du CSV
CSV_FILE = "data/healthcare_dataset.csv"

# Lire le CSV
df = pd.read_csv(CSV_FILE)

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Change si tu as un utilisateur/mot de passe
db = client["medical_db"]
collection = db["patients"]

# Nettoyer la collection si déjà existante
collection.delete_many({})

# Insérer les données du CSV
records = df.to_dict(orient="records")
collection.insert_many(records)

print("Migration terminée !")