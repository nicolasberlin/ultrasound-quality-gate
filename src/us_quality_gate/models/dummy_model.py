from typing import Any, Dict

from us_quality_gate.models.base import QualityModel


class DummyQualityModel(QualityModel):
    """
    Temporary model used to test the pipeline before integrating real models.
    """

    def predict(self, input_data: Any) -> Dict:
        return {
            "usable": True,
            "quality_score": 0.85,
            "reasons": [],
            "model_used": "dummy_model",
        }
