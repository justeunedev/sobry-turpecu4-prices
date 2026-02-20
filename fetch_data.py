import requests
import json
import os
import time

# --- CONFIGURATION ---
API_URL = "https://api.sobry.co/api/prices/tomorrow?turpe=CU4&profil=particulier"
DATA_DIR = "data"
RETENTION_DAYS = 30

# 1. Initialize data directory
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# 2. Fetch new data
try:
    response = requests.get(API_URL)
    payload = response.json()
    
    if payload.get("success"):
        target_date = payload.get("date")
        filename = os.path.join(DATA_DIR, f"tarifs_{target_date}.json")
        
        with open(filename, "w") as file:
            json.dump(payload, file)
        print(f"✅ Success: Saved {filename}")
    else:
        print("⚠️ No data available for tomorrow yet.")
except Exception as error:
    print(f"❌ API Error: {error}")

# 3. Cleanup old files (Retention Policy)
current_time = time.time()
for filename in os.listdir(DATA_DIR):
    filepath = os.path.join(DATA_DIR, filename)
    
    if os.path.isfile(filepath):
        file_age_days = (current_time - os.path.getmtime(filepath)) / (24 * 3600)
        if file_age_days > RETENTION_DAYS:
            os.remove(filepath)
            print(f"🗑️ Deleted old file (>{RETENTION_DAYS} days): {filename}")
