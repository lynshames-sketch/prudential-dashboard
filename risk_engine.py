"""
Moteur de Modélisation du Risque Bancaire & Surveillance Réglementaire (IFRS 9 / Bâle III-IV / AML)
Auteur : Dr. Saubaber Longang Gamo (PhD en Économie • Modélisation Économétrique)
"""

import math
import json
import sys

def calculate_ifrs9_metrics(loan_amount: float, dti_ratio: float, collateral_coverage: float, credit_score: int, macro_stress: str = "normal") -> dict:
    """
    Calcule la Probabilité de Défaut (PD), la Perte en cas de Défaut (LGD),
    la Perte de Crédit Attendue (ECL) et les RWA selon IFRS 9 et Bâle III/IV.
    """
    # 1. Facteur macroéconomique (Stress Testing)
    stress_multipliers = {
        "normal": 1.0,
        "modere": 1.45,   # Choc PIB -2%, hausse de taux +150 bps
        "severe": 2.20    # Choc PIB -5%, récession prolongée +300 bps
    }
    m_factor = stress_multipliers.get(macro_stress.lower(), 1.0)

    # 2. Modélisation Logistique de la Probabilité de Défaut (PD)
    # Score FICO/Interne standardisé (300 à 850)
    score_norm = (credit_score - 300) / (850 - 300)
    logit = 1.8 + (3.2 * dti_ratio) - (5.5 * score_norm) + (0.35 * (m_factor - 1.0))
    pd_base = 1.0 / (1.0 + math.exp(-logit))
    pd_final = min(max(pd_base * m_factor, 0.002), 0.99)

    # 3. Modélisation de la Perte en Cas de Défaut (LGD)
    # LGD standard 45% atténuée par la couverture de garantie (Collatéral)
    lgd_base = 0.45
    collateral_mitigation = min(collateral_coverage * 0.35, 0.35)
    lgd_final = max(lgd_base - collateral_mitigation, 0.10)

    # 4. Exposition au Défaut (EAD)
    ead = loan_amount

    # 5. Calcul de la Perte de Crédit Attendue (Expected Credit Loss - ECL)
    # Classification IFRS 9 par Stage
    if pd_final < 0.03 and credit_score >= 680:
        stage = "Stage 1 (Sain)"
        horizon = "12 mois"
        ecl = pd_final * lgd_final * ead
        decision = "APPROUVÉ"
        badge_color = "emerald"
    elif pd_final < 0.15:
        stage = "Stage 2 (Dégradation Significative - SICR)"
        horizon = "Durée de vie (Lifetime)"
        # Sur la durée de vie, la PD cumulée est plus élevée
        pd_lifetime = min(pd_final * 3.2, 0.95)
        ecl = pd_lifetime * lgd_final * ead
        decision = "SURVEILLANCE RENFORCÉE"
        badge_color = "amber"
    else:
        stage = "Stage 3 (Déprécié / Défaut avéré)"
        horizon = "Durée de vie (Lifetime)"
        ecl = 0.75 * lgd_final * ead
        decision = "REFUS / PROVISIONNEMENT INTÉGRAL"
        badge_color = "rose"

    # 6. Actifs Pondérés par les Risques (RWA - Approche IRB Bâle III/IV)
    # Formule réglementaire simplifiée de corrélation R
    r = 0.12 * (1.0 - math.exp(-50 * pd_final)) / (1.0 - math.exp(-50)) + 0.24 * (1.0 - (1.0 - math.exp(-50 * pd_final)) / (1.0 - math.exp(-50)))
    # Exigence de fonds propres minimum (8%)
    k_req = 0.08 * (pd_final * 0.5 + lgd_final * 0.5)
    rwa = loan_amount * k_req * 12.5
    capital_charge = rwa * 0.105  # Ratio CET1 + Coussins de conservation (10.5%)

    return {
        "loan_amount": loan_amount,
        "pd_percentage": round(pd_final * 100, 2),
        "lgd_percentage": round(lgd_final * 100, 2),
        "ecl_amount": round(ecl, 2),
        "ifrs9_stage": stage,
        "horizon": horizon,
        "decision": decision,
        "badge_color": badge_color,
        "rwa_amount": round(rwa, 2),
        "capital_charge_cet1": round(capital_charge, 2),
        "macro_scenario": macro_stress.capitalize()
    }

def simulate_aml_smurfing_alert() -> dict:
    """
    Simule la détection d'une structure de blanchiment de capitaux
    par fractionnement (Smurfing / Schtroumpfage) sous le seuil de déclaration de 10 000 $.
    """
    transactions = [
        {"id": "TX-901", "from": "Cpt-Inconnu A", "to": "Cpt-Pivot-7782", "amount": 9450, "time": "08:14"},
        {"id": "TX-902", "from": "Cpt-Inconnu B", "to": "Cpt-Pivot-7782", "amount": 9800, "time": "09:32"},
        {"id": "TX-903", "from": "Cpt-Inconnu C", "to": "Cpt-Pivot-7782", "amount": 9200, "time": "11:05"},
        {"id": "TX-904", "from": "Cpt-Inconnu D", "to": "Cpt-Pivot-7782", "amount": 9650, "time": "12:40"},
        {"id": "TX-905", "from": "Cpt-Pivot-7782", "to": "Offshore-Holdings-NV", "amount": 37500, "time": "14:15"}
    ]
    
    total_inflow = sum(t["amount"] for t in transactions[:4])
    outflow = transactions[-1]["amount"]
    
    return {
        "alert_type": "SCHTROUMPFAGE_STRUCTURE (AML / CFT)",
        "suspect_account": "Cpt-Pivot-7782",
        "jurisdiction": "Surveillance Réglementaire BEAC / CANAFE",
        "indicators": [
            f"4 dépôts consécutifs immédiatement sous le seuil légal de 10 000 $ (Total: {total_inflow:,} $)",
            f"Virement sortant massif immédiat ({outflow:,} $) vers une juridiction à fiscalité privilégiée",
            "Vélocité anormale des fonds (< 6 heures entre collecte et fuite)"
        ],
        "dos_report_id": "DOS-2026-0903-882A",
        "recommended_action": "Gel conservatoire 48h & Transmission à l'Unité de Renseignement Financier (URF)"
    }

if __name__ == "__main__":
    # Test unitaire en ligne de commande
    res = calculate_ifrs9_metrics(loan_amount=250000, dti_ratio=0.38, collateral_coverage=0.8, credit_score=720, macro_stress="modere")
    print("=== TEST RISK ENGINE IFRS 9 ===")
    print(json.dumps(res, indent=2, ensure_ascii=False))
