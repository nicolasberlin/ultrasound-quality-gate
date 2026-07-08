#!/usr/bin/env python3
from __future__ import annotations

from us_quality_gate.models.dummy import DummyQualityModel
from us_quality_gate.models.literature import LiteratureAdapterConfig, LiteratureQualityModelAdapter
from us_quality_gate.pipeline import QualityGatePipeline


def run_benchmark() -> None:
    sample = {"signal": 0.72}
    models = [
        DummyQualityModel(),
        LiteratureQualityModelAdapter(LiteratureAdapterConfig(name="sonoqnet_adapter", base_score=0.68)),
        LiteratureQualityModelAdapter(LiteratureAdapterConfig(name="ultrasound_qa_cnn_adapter", base_score=0.74)),
    ]

    for model in models:
        output = QualityGatePipeline(model=model).run(sample)
        print(
            {
                "model_used": output.model_used,
                "quality_score": output.quality_score,
                "decision": output.decision,
            }
        )


if __name__ == "__main__":
    run_benchmark()
