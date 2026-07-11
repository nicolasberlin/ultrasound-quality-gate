from __future__ import annotations


def build_explanations(model_reasons: list[str], decision_reasons: list[str], enabled: bool) -> list[str]:
    if not enabled:
        return decision_reasons
    return model_reasons + decision_reasons
