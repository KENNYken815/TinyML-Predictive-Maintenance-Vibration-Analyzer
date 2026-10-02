from .features import band_energy

def classify(features, config):
    scores = {
        'IMBALANCE': band_energy(features['spectrum'], *config.imbalance_band_hz),
        'MISALIGNMENT': band_energy(features['spectrum'], *config.misalignment_band_hz),
        'BEARING_FAULT': band_energy(features['spectrum'], *config.bearing_band_hz),
    }
    if features['rms'] >= config.rms_fault_g:
        return 'EXCESSIVE_VIBRATION', scores
    label = max(scores, key=scores.get)
    return (label, scores) if scores[label] >= 0.02 else ('NORMAL', scores)
