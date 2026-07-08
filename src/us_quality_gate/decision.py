from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DecisionResult:
    usable: bool
    decision: str
    reasons: list[str]


def decide_quality(quality_score: float, accept_threshold: float = 0.7) -> DecisionResult:
    if quality_score >= accept_threshold:
        return DecisionResult(usable=True, decision="accept", reasons=["quality above threshold"])
    return DecisionResult(usable=False, decision="reject", reasons=["quality below threshold"])
