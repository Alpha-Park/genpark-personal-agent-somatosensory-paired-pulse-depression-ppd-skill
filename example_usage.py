"""
Example usage of Somatosensory Paired-Pulse Depression (PPD) Skill.
Demonstrates normal cortical GABAergic inhibition vs cortical hyperexcitability.
"""

import json
from client import PairedPulsePlasticityClient


def main():
    print("=== Testing Somatosensory Paired-Pulse Depression (PPD) Skill ===")
    client = PairedPulsePlasticityClient()

    # 1. Normal short-interval intracortical inhibition (ISI = 30 ms, A1 = 2.4 uV, A2 = 1.1 uV -> PPR = 0.458)
    res_normal = client.evaluate_paired_pulse(
        unconditioned_amplitude_a1_uv=2.40,
        conditioned_amplitude_a2_uv=1.10,
        inter_stimulus_interval_ms=30.0
    )
    print("\n[Case 1: Normal Intracortical Paired-Pulse Depression]")
    print(json.dumps(res_normal, indent=2))

    # 2. Cortical hyperexcitability / loss of inhibition (ISI = 30 ms, A1 = 2.2 uV, A2 = 2.6 uV -> PPF)
    res_hyperexcitable = client.evaluate_paired_pulse(
        unconditioned_amplitude_a1_uv=2.20,
        conditioned_amplitude_a2_uv=2.60,
        inter_stimulus_interval_ms=30.0
    )
    print("\n[Case 2: Cortical Disinhibition / Paired-Pulse Facilitation]")
    print(json.dumps(res_hyperexcitable, indent=2))

    # 3. Normalized long-interval recovery (ISI = 150 ms, A1 = 2.4 uV, A2 = 2.35 uV -> PPR ~ 0.98)
    res_recovered = client.evaluate_paired_pulse(
        unconditioned_amplitude_a1_uv=2.40,
        conditioned_amplitude_a2_uv=2.35,
        inter_stimulus_interval_ms=150.0
    )
    print("\n[Case 3: Complete Synaptic Recovery at Long Interval]")
    print(json.dumps(res_recovered, indent=2))

    # Assertions
    assert res_normal["paired_pulse_ratio"] < 0.70
    assert res_hyperexcitable["paired_pulse_ratio"] > 1.0
    assert 0.90 <= res_recovered["paired_pulse_ratio"] <= 1.10
    print("\n[SUCCESS] Somatosensory Paired-Pulse Depression tests passed!")


if __name__ == "__main__":
    main()
