import math

def rms(samples):
    return math.sqrt(sum(x * x for x in samples) / len(samples)) if samples else 0.0

def peak(samples):
    return max((abs(x) for x in samples), default=0.0)

def peak_to_peak(samples):
    return max(samples) - min(samples) if samples else 0.0

def crest_factor(samples):
    value = rms(samples)
    return peak(samples) / value if value else 0.0

def zero_crossings(samples):
    return sum(1 for a, b in zip(samples, samples[1:]) if (a < 0 <= b) or (a > 0 >= b))

def spectrum(samples, sample_rate):
    n = len(samples)
    result = []
    for k in range(n // 2 + 1):
        real = imag = 0.0
        for i, value in enumerate(samples):
            angle = 2 * math.pi * k * i / n
            real += value * math.cos(angle)
            imag -= value * math.sin(angle)
        result.append((k * sample_rate / n, math.hypot(real, imag) / n))
    return result

def dominant_frequency(spectrum_data):
    return max(spectrum_data, key=lambda item: item[1])[0] if spectrum_data else 0.0

def band_energy(spectrum_data, low_hz, high_hz):
    return sum(magnitude * magnitude for freq, magnitude in spectrum_data if low_hz <= freq <= high_hz)
