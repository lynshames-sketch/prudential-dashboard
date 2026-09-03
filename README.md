# Terminal de Risque Bancaire & Surveillance Réglementaire (`prudential-dashboard`)

> **Modélisation Prudentielle du Risque de Contrepartie (*IFRS 9* • *Bâle IV* *IRB*) & Détection Topologique *AML***  
> **Auteur :** Saubaber Longang Gamo (Ph.D. en Économie • Modélisation Économétrique & Risques Financiers)

[![License: MIT](https://img.shields.io/badge/License-MIT-5bc0be.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-5bc0be?logo=github)](https://lynshames-sketch.github.io/prudential-dashboard/)

---

## 🎨 Charte Graphique : Haute Finance Prudentielle

* `#040711` : **Noir Saphir Impérial** (Fond d'immersion institutionnel)
* `#121a2d` : **Cadet Profond** (Conteneurs et panneaux financiers)
* `#2a3b5c` : **Gris Ardoise Acier** (Bordures prudentielles et séparateurs)
* `#5bc0be` : **Cyan Glacé** (Indicateurs actifs, courbes et formules)
* `#f4f5f6` : **Platine Pur** (Typographie contrastée haute fidélité)

---

## 📐 Spécifications Économétriques & Prudentielles ($\LaTeX$)

### 1. Provision pour Pertes Attendues (*IFRS 9* *ECL*)
$$\text{ECL} = \sum_{t=1}^T \frac{\text{PD}_t \times \text{LGD}_t \times \text{EAD}_t}{(1 + r)^t}$$

### 2. Modèle Structurel de Vasicek (*Bâle IV* *IRB*)
$$K = \left[ \text{LGD} \cdot \Phi\left( \frac{\Phi^{-1}(\text{PD}) + \sqrt{\rho}\Phi^{-1}(0.999)}{\sqrt{1-\rho}} \right) - \text{PD} \cdot \text{LGD} \right] \cdot \text{MA}$$

### 3. Ratio de Solvabilité *CET1*
$$\text{Ratio CET1} = \frac{\text{Fonds Propres CET1}}{\text{RWA}} \ge 8.0\% + \text{Buffers}$$

---

## 🚀 Démarrage Rapide

```bash
git clone https://github.com/lynshames-sketch/prudential-dashboard.git
cd prudential-dashboard
python -m http.server 8085
```
Accédez ensuite à : **`http://localhost:8085/`**

---

## 👤 Auteur

**Saubaber Longang Gamo (Ph.D.)**  
- **LinkedIn :** [linkedin.com/in/saubaber-longang-18416216a](https://www.linkedin.com/in/saubaber-longang-18416216a)

---

## 📄 Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.
