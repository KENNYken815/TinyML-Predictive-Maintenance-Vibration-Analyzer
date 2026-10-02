# Architecture

The project separates signal generation, preprocessing, feature extraction, classification, diagnostics, and telemetry.

```text
Accelerometer / ADC (future hardware)
            |
            v
      preprocessing
            |
            v
    feature extraction
            |
            v
    TinyML classifier
            |
            v
 health state + DTC + telemetry
```

The synthetic signal generator is intentionally isolated so it can later be replaced by a real accelerometer driver without changing the analysis pipeline.
