import unittest
from src.config import AnalyzerConfig
from src.signals import scenario
from src.analyzer import VibrationAnalyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.config = AnalyzerConfig()
        self.analyzer = VibrationAnalyzer(self.config)

    def test_healthy(self):
        self.assertEqual(self.analyzer.analyze(scenario('healthy', 256, 1000))[1], 'NORMAL')

    def test_high_vibration(self):
        self.assertEqual(self.analyzer.analyze(scenario('imbalance', 256, 1000))[1], 'EXCESSIVE_VIBRATION')

    def test_misalignment(self):
        self.assertIn(self.analyzer.analyze(scenario('misalignment', 256, 1000))[1], ('MISALIGNMENT', 'EXCESSIVE_VIBRATION'))

    def test_bearing(self):
        self.assertIn(self.analyzer.analyze(scenario('bearing', 256, 1000))[1], ('BEARING_FAULT', 'EXCESSIVE_VIBRATION'))

if __name__ == '__main__':
    unittest.main()
