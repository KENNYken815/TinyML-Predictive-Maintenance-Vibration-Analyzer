from dataclasses import dataclass

@dataclass(frozen=True)
class AnalyzerConfig:
    sample_rate_hz: int = 1000
    window_size: int = 256
    rms_warning_g: float = 1.5
    rms_fault_g: float = 2.5
    imbalance_band_hz: tuple = (18.0, 32.0)
    misalignment_band_hz: tuple = (35.0, 70.0)
    bearing_band_hz: tuple = (180.0, 260.0)
