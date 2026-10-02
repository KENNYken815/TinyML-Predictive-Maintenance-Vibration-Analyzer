from src.config import AnalyzerConfig
from src.signals import scenario
from src.analyzer import VibrationAnalyzer

def run_all():
    config = AnalyzerConfig()
    analyzer = VibrationAnalyzer(config)
    for name in ('healthy', 'imbalance', 'misalignment', 'bearing'):
        features, label, state = analyzer.analyze(scenario(name, config.window_size, config.sample_rate_hz))
        yield name, features, label, state
