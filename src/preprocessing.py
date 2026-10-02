def remove_mean(samples):
    if not samples:
        return []
    mean = sum(samples) / len(samples)
    return [value - mean for value in samples]

def take_window(samples, size):
    if len(samples) < size:
        raise ValueError('not enough samples for analysis window')
    return samples[:size]
