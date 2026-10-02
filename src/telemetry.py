import csv
from pathlib import Path

def save_rows(rows, filename):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(['scenario', 'rms_g', 'peak_g', 'crest_factor', 'dominant_hz', 'class', 'state', 'dtc'])
        writer.writerows(rows)
