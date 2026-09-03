# Prudential Risk & Banking Surveillance Suite

> **Suite d'Économétrie Prudentielle & Surveillance Réglementaire (IFRS 9 • Bâle III/IV • AML/CFT)**  
> **Auteur :** Saubaber Longang Gamo (Ph.D. en Économie • Modélisation Économétrique)

[![Standards](https://img.shields.io/badge/Regulatory%20Standards-IFRS%209%20%7C%20Basel%20III--IV%20IRB-06b6d4)](https://www.bis.org/bcbs/basel3.htm)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)

---

## 📌 Présentation du Projet

La **Prudential Risk & Banking Surveillance Suite** (`prudential-dashboard`) est un terminal interactif combinant modélisation économétrique avancée et conformité bancaire internationale.

Conçu à l'intersection de la recherche académique, de l'expérience en banque centrale (ex-BEAC) et des meilleures pratiques d'ingénierie financière, ce système permet d'évaluer le risque de crédit en temps réel et de détecter les schémas complexes de criminalité financière.

---

## 🏛️ Architecture & Fonctionnalités Clés

### 1. Moteur de Risque de Crédit & Provisions IFRS 9
* **Modélisation Logistique de la Probabilité de Défaut (PD)** :
  $$PD = \frac{1}{1 + e^{-(1.8 + 3.2 \cdot DTI - 5.5 \cdot Score_{norm} + \Delta Macro)}}$$
* **Atténuation de la Perte en Cas de Défaut (LGD)** selon la qualité des garanties et du collatéral ($LGD_{final} = \max(0.45 - 0.35 \cdot Collat, 0.10)$).
* **Classification Dynamique IFRS 9** :
  - **Stage 1 (Actif Sain)** : Provision sur horizon de 12 mois.
  - **Stage 2 (Dégradation Significative du Risque - SICR)** : Surveillance renforcée et provisionnement sur la durée de vie (*Lifetime ECL*).
  - **Stage 3 (Actif Déprécié / Défaut)** : Provisionnement intégral pour créance douteuse.
* **Actifs Pondérés par les Risques (RWA) & Coussin CET1** : Calcul des exigences de fonds propres sous l'approche modèles internes (IRB) de Bâle IV avec coussin prudentiel à 10.5 %.
* **Graphique en Cascade (Waterfall Chart)** : Décomposition transparente des facteurs explicatifs de risque.

### 2. Surveillance Blanchiment d'Argent (AML / KYC Network Graph)
* **Visualisation Topologique des Flux** : Représentation sur canevas interactif des nœuds de transactions entre comptes émetteurs, compte pivot et comptes destinataires.
* **Algorithme de Détection du « Schtroumpfage » (Smurfing)** : Identification automatique des dépôts fractionnés sous le seuil légal de déclaration (10 000 $) à haute vélocité.
* **Générateur Automatique de Déclaration d'Opération Suspecte (DOS)** : Production d'un dossier d'investigation pré-rempli conforme aux directives des Unités de Renseignement Financier (CANAFE, COBAC, BEAC, Tracfin).

---

## 📁 Structure du Répertoire

```
prudential-dashboard/
├── index.html            # Interface interactive Tailwind CSS (Stitch Design System)
├── risk_engine.py        # Moteur de calcul économétrique et de simulation AML
├── requirements.txt      # Dépendances Python
├── LICENSE               # Licence MIT
└── README.md             # Documentation institutionnelle
```

---

## 🚀 Démarrage Rapide

### 1. Cloner le Répertoire
```bash
git clone https://github.com/lynshames-sketch/prudential-dashboard.git
cd prudential-dashboard
```

### 2. Lancer l'Interface Web
Vous pouvez lancer le serveur local via Python :
```bash
python -m http.server 8085
```
Puis ouvrez votre navigateur sur : **`http://localhost:8085/`**

### 3. Exécuter le Moteur Économétrique en Ligne de Commande
```bash
python risk_engine.py
```

---

## 👤 Auteur

**Saubaber Longang Gamo (Ph.D.)**  
*Économiste, Expert en Modélisation Économétrique & Évaluation de Politiques Publiques*  
- **LinkedIn :** [linkedin.com/in/saubaber-longang-18416216a](https://www.linkedin.com/in/saubaber-longang-18416216a)

---

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
