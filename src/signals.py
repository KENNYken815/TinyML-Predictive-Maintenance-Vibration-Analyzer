import math

def sine_wave(freq, amplitude, count, sample_rate):
    return [amplitude * math.sin(2 * math.pi * freq * i / sample_rate) for i in range(count)]

def add_signals(*signals):
    return [sum(values) for values in zip(*signals)]

def scenario(name, count=256, sample_rate=1000):
    base = sine_wave(25.0, 0.35, count, sample_rate)
    if name == 'healthy':
        return add_signals(base, sine_wave(90.0, 0.08, count, sample_rate))
    if name == 'imbalance':
        return add_signals(base, sine_wave(25.0, 1.8, count, sample_rate), sine_wave(50.0, 0.25, count, sample_rate))
    if name == 'misalignment':
        return add_signals(base, sine_wave(50.0, 0.9, count, sample_rate), sine_wave(100.0, 0.45, count, sample_rate))
    if name == 'bearing':
        return add_signals(base, sine_wave(220.0, 1.4, count, sample_rate), sine_wave(440.0, 0.5, count, sample_rate))
    raise ValueError('unknown scenario: ' + name)
