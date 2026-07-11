from __future__ import annotations

from typing import Any

from .interface import ModelPrediction, QualityModel


class DummyQualityModel(QualityModel):
    """Deterministic baseline model for development and tests."""

    name = "dummy_quality_model"

    def predict(self, sample: Any) -> ModelPrediction:
        if isinstance(sample, dict):
            score = float(sample.get("signal", 0.5))
        elif isinstance(sample, (int, float)):
            score = float(sample)
        else:
            score = 0.5

        score = min(1.0, max(0.0, score))
        reasons = ["dummy baseline score"]
        return ModelPrediction(quality_score=score, reasons=reasons)
