from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .decision import decide_quality
from .explanations import build_explanations
from .models.interface import QualityModel


@dataclass(frozen=True)
class QualityGateOutput:
    usable: bool
    quality_score: float
    reasons: list[str]
    model_used: str
    decision: str


class QualityGatePipeline:
    def __init__(
        self,
        model: QualityModel,
        accept_threshold: float = 0.7,
        enable_explanations: bool = True,
    ) -> None:
        self.model = model
        self.accept_threshold = accept_threshold
        self.enable_explanations = enable_explanations

    def run(self, sample: Any) -> QualityGateOutput:
        prediction = self.model.predict(sample)
        decision = decide_quality(prediction.quality_score, accept_threshold=self.accept_threshold)
        reasons = build_explanations(
            model_reasons=prediction.reasons,
            decision_reasons=decision.reasons,
            enabled=self.enable_explanations,
        )
        return QualityGateOutput(
            usable=decision.usable,
            quality_score=prediction.quality_score,
            reasons=reasons,
            model_used=self.model.name,
            decision=decision.decision,
        )
