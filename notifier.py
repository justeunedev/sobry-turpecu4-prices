import sys
import requests
import json
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# --- CONFIGURATION DES CANAUX NTFY ---
# Remplace par tes vrais noms de canaux
TOPIC_HOURLY = "justeunedev-sobrynotif-horaire"
TOPIC_3H = "justeunedev-sobrynotif-3heures"
TOPIC_RECAPS = "justeunedev-sobrynotif-general"

DATA_DIR = "data/"
TZ = ZoneInfo("Europe/Paris")

def send_ntfy(topic, message, title, priority=3):
    requests.post(f"https://ntfy.sh/{topic}",
                  data=message.encode('utf-8'),
                  headers={"Title": title.encode('utf-8'), "Priority": str(priority), "Tags": "zap"})

def get_prices(date_obj):
    path = os.path.join(DATA_DIR, f"tarifs_{date_obj.strftime('%Y-%m-%d')}.json")
    if os.path.exists(path):
        with open(path, 'r') as f:
            d = json.load(f)
            return d.get('prices') or d.get('data')
    return []

def get_avg(prices, start_h, end_h):
    relevant = [p['price_ttc_eur_kwh'] * 100 for p in prices 
                if start_h <= datetime.fromisoformat(p['timestamp']).hour < end_h]
    return sum(relevant) / len(relevant) if relevant else 0

now = datetime.now(TZ)
prices_today = get_prices(now)
prices_tomorrow = get_prices(now + timedelta(days=1))

mode = sys.argv[1] if len(sys.argv) > 1 else "none"

# ==========================================
# CANAL 1 : NOTIFICATIONS HORAIRES (HH:45)
# ==========================================
if mode == "hourly" and prices_today:
    target_hour = (now + timedelta(hours=1)).hour
    next_prices = [p['price_ttc_eur_kwh'] * 100 for p in prices_today 
                   if datetime.fromisoformat(p['timestamp']).hour == target_hour]
    
    msg = "\n".join([f"• {target_hour}h{i*15:02d} : {val:.2f} c€" for i, val in enumerate(next_prices)])
    send_ntfy(TOPIC_HOURLY, msg, f"Tarifs {target_hour}h - {target_hour+1}h")

# ==========================================
# CANAL 2 : TOUTES LES 3 HEURES
# ==========================================
elif mode == "3h" and prices_today:
    target_hour = (now + timedelta(hours=1)).hour
    avg_3h = get_avg(prices_today, target_hour, target_hour + 3)
    send_ntfy(TOPIC_3H, f"Moyenne de {target_hour}h à {target_hour+3}h : {avg_3h:.2f} c€", "Prévision 3 Heures")

# ==========================================
# CANAL 3 : LES RECAPS
# ==========================================
elif mode == "recap_matin" and prices_today:
    # 7h30 : Moyenne Journée + Matinée
    moy_jour = get_avg(prices_today, 0, 24)
    moy_matin = get_avg(prices_today, 8, 13)
    msg = f"🌅 Moyenne de la journée : {moy_jour:.2f} c€\n☕ Moyenne Matinée (8h-13h) : {moy_matin:.2f} c€"
    send_ntfy(TOPIC_RECAPS, msg, "Récap Matin")

elif mode == "recap_midi" and prices_today:
    # 12h30 : Après-midi
    moy_aprem = get_avg(prices_today, 13, 18)
    send_ntfy(TOPIC_RECAPS, f"☀️ Moyenne Après-midi (13h-18h) : {moy_aprem:.2f} c€", "Récap Midi")

elif mode == "recap_demain" and prices_tomorrow:
    # 13h15 : Arrivée des prix de demain
    # Pour la nuit de demain, on prend 00h-06h et 22h-24h du même jour (représentatif des 8h de nuit)
    moy_jour_demain = get_avg(prices_tomorrow, 6, 22)
    
    nuit_matin = [p['price_ttc_eur_kwh'] * 100 for p in prices_tomorrow if datetime.fromisoformat(p['timestamp']).hour < 6]
    nuit_soir = [p['price_ttc_eur_kwh'] * 100 for p in prices_tomorrow if datetime.fromisoformat(p['timestamp']).hour >= 22]
    nuit_complete = nuit_matin + nuit_soir
    moy_nuit_demain = sum(nuit_complete) / len(nuit_complete) if nuit_complete else 0

    msg = f"📅 Moyenne Jour (06h-22h) : {moy_jour_demain:.2f} c€\n🌙 Moyenne Nuit (22h-06h) : {moy_nuit_demain:.2f} c€"
    send_ntfy(TOPIC_RECAPS, msg, "Prix de Demain Disponibles !")

elif mode == "recap_soir" and prices_today:
    # 16h30 : Soirée
    moy_soir = get_avg(prices_today, 18, 22)
    send_ntfy(TOPIC_RECAPS, f"🌆 Moyenne Soirée (18h-22h) : {moy_soir:.2f} c€", "Récap Soir")

elif mode == "recap_nuit":
    # 21h30 : Nuit (Mixte aujourd'hui et demain)
    nuit_ce_soir = [p['price_ttc_eur_kwh'] * 100 for p in prices_today if datetime.fromisoformat(p['timestamp']).hour >= 22] if prices_today else []
    nuit_demain_matin = [p['price_ttc_eur_kwh'] * 100 for p in prices_tomorrow if datetime.fromisoformat(p['timestamp']).hour < 6] if prices_tomorrow else []
    
    nuit_totale = nuit_ce_soir + nuit_demain_matin
    moy_nuit = sum(nuit_totale) / len(nuit_totale) if nuit_totale else 0
    send_ntfy(TOPIC_RECAPS, f"🛌 Moyenne Nuit (22h-06h) : {moy_nuit:.2f} c€", "Récap Nuit")
