# ⚡ Sobry Dashboard des prix TURPE CU4 (TTC)

Une application Python/Streamlit conçue pour suivre en temps réel les prix dynamiques de l'électricité en France, en intégrant automatiquement les prix Spot, le TURPE (CU4) et toutes les taxes (TTC).
Les données sont fournies par l'API publique du fournisseur d'électricité Sobry, afin d'être utiliser avec un de leur contrat.
L'API utilisée affich le tarif particulier TTC et utilise le TURPE CU4.

## 🛠️ Structure du Projet
- `app.py` : Interface utilisateur (Streamlit).
- `fetch_data.py` : Script backend pour récupérer les données de l'API et gérer la rétention des fichiers.
- `data/` : Dossier contenant les fichiers JSON quotidiens (historique glissant de 30 jours).
- `.github/workflows/update_tarifs.yml` : GitHub Action pour l'automatisation quotidienne de la récupération des prix.

## 🚀 Fonctionnalités
- **Zéro Maintenance** : GitHub Actions récupère automatiquement les prix du lendemain tous les jours.
- **Nettoyage Intelligent** : `fetch_data.py` supprime automatiquement les fichiers JSON vieux de plus de 30 jours pour garder un environnement propre.
- **Accessibilité Cognitive** : Les couleurs sont calquées sur le Tarif Bleu officiel d'EDF (Heures Pleines / Heures Creuses) pour une prise de décision visuelle rapide, limitant la charge mentale.

## 🎨 Code Couleur (Référence Tarif Bleu EDF)
- **🟢 Vert Foncé (< 12.00 c€)** : Exceptionnel. Le meilleur moment pour lancer les gros appareils énergivores.
- **🍏 Vert Clair (12.00 - 15.79 c€)** : Très avantageux (Moins cher que les Heures Creuses Tarif Bleu d'EDF).
- **🟡 Jaune (15.79 - 18.22 c€)** : Zone neutre.
- **🟠 Orange (18.22 - 20.65 c€)** : Vigilance (On se rapproche du tarif Heures Pleines Tarif Bleu d'EDF).
- **🔴 Rouge (> 20.65 c€)** : À éviter (Plus cher que les Heures Pleines Tarif Bleu d'EDF).

## ⚙️ Installation
1. Créer un dépôt GitHub et y pousser ces fichiers.
2. Autoriser l'écriture pour les Actions dans `Settings > Actions > General > Workflow permissions` (cocher **Read and write permissions**).
3. Déployer le dépôt gratuitement sur **Streamlit Community Cloud**.

---

## 👩‍💻 Crédits & Licence
Une app de **Juste Une Dev** - justeunedev(a)arniael.fr  
Distribué sous la **Licence MIT**.
