# ⚡ Sobry Dashboard des prix TURPE CU4 (TTC)
![Status](https://img.shields.io/badge/Status-En_ligne-success?style=for-the-badge&logo=server)
![Made by](https://img.shields.io/badge/Made_by-Juste_Une_Dev-blueviolet?style=for-the-badge&logo=python)
![Device](https://img.shields.io/badge/Optimisé_pour-Mobile-4CAF50?style=for-the-badge&logo=android)

Une application Python/Streamlit conçue pour suivre en temps réel les prix dynamiques de l'électricité en France, en intégrant automatiquement les prix Spot, le TURPE (CU4) et toutes les taxes (TTC).
Les données sont fournies par l'API publique du fournisseur d'électricité Sobry, afin d'être utiliser avec un de leur contrat.
L'API utilisée affich le tarif particulier TTC et utilise le TURPE CU4.

## 🔗 Accès direct
Vous pouvez directement accéder aux données en version TURPE CU4 TTC sur le serveur d'Arniael à **(sobry-cu4.arniael.eu)[https://sobry-cu4.arniael.eu]**.

## 🔔 Notifications en direct
Nous proposons différents types de notifications en passant par l'app ntfy.sh sur le serveur (notif.arniael.eu)[https://notif.arniael.eu :
- **Notifs Générales** : 5 notifications dans la journée. La première à 7h30 avec la moyenne du jour (00h à 23h59) et de la matinée (8h - 13h), une deuxième à 12h30 pour la moyenne de l'après midi (13h - 18h), une troisième à 17h30 pour la moyenne de la soirée (18h - 22h) et une quatrième à 21h30 pour la moyenne de la nuit (22h - 06h). La cinquième ? Tout simplement pour vous avertir de la disponibilité des prix du lendemain dans l'app directement à 13h15, avec la moyenne de la journée du lendemain (6h - 22h) ainsi que de la nuit (00h - 06h + 22h - 00h). Et tout ça sur le canal (jud-sobry-general)[https://notif.arniael.eu/jud-sobry-general].
- **Toutes les 15 minutes** : Une notification vous alerte à chaque changement de prix toutes les 15 minutes sur le canal (jud-sobry-15minutes)[https://notif.arniael.eu/jud-sobry-15minutes].
- **Moyenne Horaire** : Quinze minutes avant le prochain créneaux horaire, une notification vous alerte du tarif moyen de la prochaine heure sur le canal (jud-sobry-hourly)[https://notif.arniael.eu/jud-sobry-hourly].
- **Moyenne des 3 prochaines heures** : Comme la moyenne horaire, mais rassemblant le bloc des 3 prochaines heures en indiquant le montant moyen de chaque heure sur le canal (jud-sobry-3hours)[https://notif.arniael.eu/jud-sobry-3hours].

## 🛠️ Structure du Projet
- `app.py` : Interface utilisateur (Streamlit).
- `fetch_data.py` : Script backend pour récupérer les données de l'API et gérer la rétention des fichiers.
- `data/` : Dossier contenant les fichiers JSON quotidiens (historique glissant de 30 jours).
- `.github/workflows/update_tarifs.yml` : GitHub Action pour l'automatisation quotidienne de la récupération des prix.

## 🚀 Fonctionnalités
- **Zéro Maintenance** : GitHub Actions récupère automatiquement les prix du lendemain tous les jours.
- **Dispo direct comme une app** : Installez la webapp pour avoir un raccourcis comme si vous aviez installé l'application de sobry (qui n'existe pas...).
- **Des notifs comme jamais** : Grâce à l'instance ntfy d'Arniael, recevez des notifs pour le tarif TURPE CU4 TTC directement sur votre mobile !
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
Logo de (Freepik via Flaticon)[https://www.flaticon.com/fr/icones-gratuites/eclat]
