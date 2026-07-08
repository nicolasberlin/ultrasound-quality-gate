from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ModelPrediction:
    quality_score: float
    reasons: list[str]


class QualityModel(ABC):
    """Common interface for ultrasound quality scoring models."""

    name: str

    @abstractmethod
    def predict(self, sample: Any) -> ModelPrediction:
        """Return a quality score in [0, 1] and optional reasons."""
