import argparse
from scenarios.demo_scenarios import run_all
from src.diagnostics import DTC, format_report
from src.telemetry import save_rows

def main():
    parser = argparse.ArgumentParser(description='TinyML predictive-maintenance vibration analyzer')
    parser.add_argument('--csv', help='write analysis results to CSV')
    args = parser.parse_args()
    rows = []
    for name, features, label, state in run_all():
        print(format_report(name, features, label, state))
        rows.append([name, features['rms'], features['peak'], features['crest_factor'], features['dominant_hz'], label, state, DTC[label]])
    if args.csv:
        save_rows(rows, args.csv)
        print('CSV written to', args.csv)

if __name__ == '__main__':
    main()
