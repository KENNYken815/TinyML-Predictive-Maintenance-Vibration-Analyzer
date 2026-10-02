from .preprocessing import remove_mean, take_window
from .features import rms, peak, peak_to_peak, crest_factor, zero_crossings, spectrum, dominant_frequency
from .classifier import classify
from .diagnostics import health_state

class VibrationAnalyzer:
    def __init__(self, config):
        self.config = config

    def analyze(self, samples):
        conditioned = remove_mean(take_window(samples, self.config.window_size))
        spectral = spectrum(conditioned, self.config.sample_rate_hz)
        features = {
            'rms': rms(conditioned),
            'peak': peak(conditioned),
            'peak_to_peak': peak_to_peak(conditioned),
            'crest_factor': crest_factor(conditioned),
            'zero_crossings': zero_crossings(conditioned),
            'spectrum': spectral,
            'dominant_hz': dominant_frequency(spectral),
        }
        label, _ = classify(features, self.config)
        return features, label, health_state(label, features['rms'], self.config)
