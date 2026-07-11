# ultrasound-quality-gate

Python research scaffold for an ultrasound acquisition quality-control pipeline.

## Structure

- `src/us_quality_gate/` core package
- `configs/` example pipeline config
- `scripts/` model benchmark script
- `docs/` project notes
- `tests/` focused unit tests

## Quickstart

```bash
PYTHONPATH=src python -m unittest discover -s tests -q
PYTHONPATH=src python scripts/benchmark_models.py
```

No real medical data is included.
