from abc import ABC, abstractmethod
from typing import Any, Dict


class QualityModel(ABC):
    """
    Base interface for all ultrasound quality models.
    """

    @abstractmethod
    def predict(self, input_data: Any) -> Dict:
        """
        Returns:
            {
                "usable": bool,
                "quality_score": float,
                "reasons": list[str],
                "model_used": str
            }
        """
        raise NotImplementedError
