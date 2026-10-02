# TinyML Predictive Maintenance Vibration Analyzer

A host-runnable TinyML-style predictive-maintenance reference project that processes vibration samples, extracts lightweight features, classifies machine condition, and produces maintenance diagnostics.

> **Project status:** Completed reference/simulation implementation. It demonstrates an embedded/TinyML workflow with deterministic synthetic vibration data. It does not claim deployment on a specific MCU, real accelerometer calibration, or production fault-detection accuracy.

## Pipeline
```text
Vibration samples -> preprocessing -> feature extraction -> lightweight classifier -> machine health -> diagnostics/telemetry
```

## Implemented
- Synthetic vibration signal generation
- Configurable 1 kHz sampling and 256-sample analysis window
- Mean removal
- RMS, peak, peak-to-peak and crest factor
- Zero-crossing count
- Dependency-free DFT magnitude spectrum
- Dominant-frequency and band-energy features
- Lightweight feature-based fault classification
- Healthy, imbalance-like, misalignment-like and bearing-fault-like scenarios
- Machine health state and DTC output
- CSV export
- Python unit tests with no external packages

## Reference parameters
| Parameter | Value |
|---|---:|
| Sample rate | 1000 Hz |
| Window | 256 samples |
| RMS warning | 1.50 g |
| RMS fault | 2.50 g |
| Imbalance band | 18–32 Hz |
| Misalignment band | 35–70 Hz |
| Bearing band | 180–260 Hz |

These are simulation values, not production machine limits.

## Repository structure
```text
src/                  Core implementation
  config.py           Analysis/calibration settings
  signals.py          Synthetic vibration generation
  preprocessing.py    Signal conditioning
  features.py         Embedded-friendly feature extraction
  classifier.py       Lightweight classifier
  diagnostics.py      Health state and DTC formatting
  telemetry.py        CSV reporting
  analyzer.py         End-to-end analysis pipeline
scenarios/            Ready-made test conditions
tests/                Automated unit tests
docs/                 Design and verification notes
output/               Generated files only
run_demo.py           User-facing entry point
Makefile              make run / make test
README.md             Project guide
```

## Quick start
```bash
python3 run_demo.py
python3 -m unittest discover -s tests -v
python3 run_demo.py --csv output/vibration_analysis.csv
```
Or:
```bash
make run
make test
```

## Scenarios
- **Healthy:** low-amplitude baseline vibration
- **Imbalance-like:** strong rotational component
- **Misalignment-like:** stronger harmonic content
- **Bearing-fault-like:** energy in the configured bearing band

These are simplified signal models for software demonstration, not physical machine-identification models.

## Diagnostic codes
| Code | Meaning |
|---|---|
| `VIB_000` | Healthy / no active fault |
| `VIB_101` | Excessive overall vibration |
| `VIB_102` | Imbalance-like pattern |
| `VIB_103` | Misalignment-like pattern |
| `VIB_104` | Bearing-fault-like pattern |

## TinyML deployment path
The current classifier is intentionally lightweight and explainable. For an MCU implementation, the synthetic signal source can be replaced with an accelerometer/ADC driver, the DFT with an optimized FFT where appropriate, and the rule-based classifier with a quantized model such as a small decision tree or TensorFlow Lite Micro model.

## Portfolio value
Demonstrates vibration signal processing, embedded-friendly feature engineering, TinyML-style classification, diagnostics, deterministic testing, and clean separation between data generation and application logic.

## Validation scope
The included tests validate deterministic software behavior. Real predictive-maintenance performance requires representative labeled vibration data, sensor calibration, machine-specific operating envelopes, and target-hardware validation.
