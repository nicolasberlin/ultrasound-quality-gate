from us_quality_gate.models.dummy_model import DummyQualityModel
from us_quality_gate.pipeline.quality_gate import UltrasoundQualityGate


def main():
    model = DummyQualityModel()
    gate = UltrasoundQualityGate(model=model, threshold=0.7)

    fake_ultrasound_input = "data/samples/example.png"

    result = gate.run(fake_ultrasound_input)

    print(result)


if __name__ == "__main__":
    main()
