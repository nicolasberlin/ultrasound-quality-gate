import unittest

from us_quality_gate.models.dummy import DummyQualityModel
from us_quality_gate.pipeline import QualityGatePipeline


class TestQualityGatePipeline(unittest.TestCase):
    def test_accept_output_schema(self) -> None:
        pipeline = QualityGatePipeline(model=DummyQualityModel(), accept_threshold=0.7)
        result = pipeline.run({"signal": 0.9})

        self.assertTrue(result.usable)
        self.assertEqual(result.decision, "accept")
        self.assertIsInstance(result.quality_score, float)
        self.assertIsInstance(result.reasons, list)
        self.assertEqual(result.model_used, "dummy_quality_model")

    def test_reject_when_below_threshold(self) -> None:
        pipeline = QualityGatePipeline(model=DummyQualityModel(), accept_threshold=0.8)
        result = pipeline.run({"signal": 0.3})

        self.assertFalse(result.usable)
        self.assertEqual(result.decision, "reject")
        self.assertIn("quality below threshold", result.reasons)

    def test_explanations_optional(self) -> None:
        pipeline = QualityGatePipeline(
            model=DummyQualityModel(),
            accept_threshold=0.7,
            enable_explanations=False,
        )
        result = pipeline.run({"signal": 0.9})

        self.assertEqual(result.reasons, ["quality above threshold"])


if __name__ == "__main__":
    unittest.main()
