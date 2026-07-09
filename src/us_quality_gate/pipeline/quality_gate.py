from typing import Any, Dict

from us_quality_gate.models.base import QualityModel
from us_quality_gate.pipeline.decision_rules import apply_decision_rules


class UltrasoundQualityGate:
    """
    Main pipeline for ultrasound acquisition quality control.
    """

    def __init__(self, model: QualityModel, threshold: float = 0.7):
        self.model = model
        self.threshold = threshold

    def run(self, input_data: Any) -> Dict:
        model_output = self.model.predict(input_data)
        return apply_decision_rules(model_output, threshold=self.threshold)
