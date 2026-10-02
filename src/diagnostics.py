DTC = {
    'NORMAL': 'VIB_000',
    'EXCESSIVE_VIBRATION': 'VIB_101',
    'IMBALANCE': 'VIB_102',
    'MISALIGNMENT': 'VIB_103',
    'BEARING_FAULT': 'VIB_104',
}

def health_state(label, rms_value, config):
    if label != 'NORMAL' and rms_value >= config.rms_fault_g:
        return 'FAULT'
    if label != 'NORMAL' or rms_value >= config.rms_warning_g:
        return 'WARNING'
    return 'NORMAL'

def format_report(name, features, label, state):
    return (f'{name:<14} state={state:<7} class={label:<20} '
            f'rms={features["rms"]:.3f}g peak={features["peak"]:.3f}g '
            f'crest={features["crest_factor"]:.2f} '
            f'dominant={features["dominant_hz"]:.1f}Hz dtc={DTC[label]}')
