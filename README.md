# Terminal de Risque Bancaire & Surveillance Réglementaire (`prudential-dashboard`)

> **Modélisation Prudentielle du Risque de Contrepartie (*IFRS 9* • *Bâle IV* *IRB*) & Détection Topologique *AML***  
> **Auteur :** Saubaber Longang Gamo (Ph.D. en Économie • Modélisation Économétrique & Risques Financiers)

[![License: MIT](https://img.shields.io/badge/License-MIT-5bc0be.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Palette Coolors](https://img.shields.io/badge/Coolors%20Palette-0a1128%20%7C%201c2541%20%7C%203a506b%20%7C%205bc0be%20%7C%20f4f5f6-3a506b)](https://coolors.co/0a1128-1c2541-3a506b-5bc0be-f4f5f6)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-5bc0be?logo=github)](https://lynshames-sketch.github.io/prudential-dashboard/)

---

## 🎨 Charte Graphique & Palette Coolors Bancaire

Palette officielle : 🔗 **[https://coolors.co/0a1128-1c2541-3a506b-5bc0be-f4f5f6](https://coolors.co/0a1128-1c2541-3a506b-5bc0be-f4f5f6)**

* `#0a1128` : Oxford Blue / Fond sombre d'institution centrale
* `#1c2541` : Deep Space Cadet / Panneaux et cartes financières
* `#3a506b` : Steel Slate Blue / Bordures prudentielles et séparateurs
* `#5bc0be` : Ice Cyan / Indicateurs actifs, courbes et formules
* `#f4f5f6` : Pure Platinum / Typographie contrastée haute fidélité

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
