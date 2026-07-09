from typing import Dict


def apply_decision_rules(model_output: Dict, threshold: float = 0.7) -> Dict:
    """
    Converts model scores into a final accept/reject decision.
    """

    quality_score = model_output.get("quality_score", 0.0)
    usable = quality_score >= threshold

    return {
        **model_output,
        "usable": usable,
        "threshold": threshold,
        "decision": "accept" if usable else "reject",
    }
