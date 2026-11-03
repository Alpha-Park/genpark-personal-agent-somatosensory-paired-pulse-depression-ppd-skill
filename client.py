"""
Somatosensory Paired-Pulse Depression (PPD) & Short-Term Plasticity Client.
Zero-mock pure Python standard library implementation.
Calculates conditioned second response amplitude attenuation (A2 / A1),
inter-stimulus interval (ISI) recovery curve, and cortical GABAergic inhibitory tone.
"""

import math
from typing import Dict, Any, List, Optional


class PairedPulsePlasticityClient:
    """
    Computes Paired-Pulse Depression (PPD) ratio (A2 / A1) and Paired-Pulse Facilitation (PPF)
    from conditioning-test somatosensory evoked potentials (SEP / SSEP) at varying inter-stimulus intervals.
    """

    def __init__(self):
        pass

    def evaluate_paired_pulse(
        self,
        unconditioned_amplitude_a1_uv: float,
        conditioned_amplitude_a2_uv: float,
        inter_stimulus_interval_ms: float = 30.0,
        baseline_noise_uv: float = 0.2
    ) -> Dict[str, Any]:
        """
        Calculates PPD ratio and evaluates intracortical synaptic inhibition.
        unconditioned_amplitude_a1_uv: First conditioning pulse response amplitude in uV (e.g. N20-P25 peak-to-peak).
        conditioned_amplitude_a2_uv: Second test pulse response amplitude in uV.
        inter_stimulus_interval_ms: Interval between paired pulses in ms (typically 10 to 100 ms).
        baseline_noise_uv: Ambient recording noise in uV.
        """
        if unconditioned_amplitude_a1_uv <= 0:
            raise ValueError("Unconditioned amplitude A1 must be strictly positive.")
        if conditioned_amplitude_a2_uv < 0:
            raise ValueError("Conditioned amplitude A2 must be non-negative.")
        if inter_stimulus_interval_ms <= 0:
            raise ValueError("Inter-stimulus interval must be positive.")

        # Paired-Pulse Ratio (PPR) = A2 / A1
        ppr = conditioned_amplitude_a2_uv / unconditioned_amplitude_a1_uv

        # Suppression percentage: (1 - PPR) * 100%
        suppression_pct = max(0.0, (1.0 - ppr) * 100.0)

        # Expected physiological behavior:
        # At short ISIs (10 - 40 ms), healthy somatosensory cortex exhibits robust PPD (PPR < 0.70)
        # driven by GABA-A/B mediated short-interval intracortical inhibition (SICI).
        # At longer ISIs (100 - 300 ms), PPR returns towards 1.0 (baseline recovery).
        # Disinhibition (PPR > 0.85 at ISI 30ms) occurs in focal dystonia, cortical hyperexcitability, or neurodegeneration.
        if inter_stimulus_interval_ms <= 50.0:
            if ppr < 0.40:
                classification = "Strong Short-Interval Intracortical Inhibition (SICI)"
                synaptic_state = "Robust GABAergic interneuron feed-forward inhibition; resilient cortical gating."
                inhibitory_tone = "High / Preserved"
            elif ppr <= 0.75:
                classification = "Normal Physiological Paired-Pulse Depression (PPD)"
                synaptic_state = "Typical synaptic vesicle depletion and GABAergic inhibitory loop activation."
                inhibitory_tone = "Normal"
            elif ppr <= 1.05:
                classification = "Impaired Cortical Inhibition / Disinhibition"
                synaptic_state = "Blunted paired-pulse attenuation; deficient sensorimotor cortical gating."
                inhibitory_tone = "Sub-optimal / Attenuated"
            else:
                classification = "Paired-Pulse Facilitation (PPF) / Cortical Hyperexcitability"
                synaptic_state = "Paradoxical amplitude amplification (A2 > A1); persistent presynaptic residual calcium."
                inhibitory_tone = "Deficient / Hyperexcitable"
        else:
            # Extended ISI recovery window (50 - 200 ms)
            if ppr <= 0.85:
                classification = "Delayed Synaptic Recovery / Prolonged Refractoriness"
                synaptic_state = "Persistent slow inhibitory postsynaptic potentials (GABA-B mediated)."
                inhibitory_tone = "Prolonged Inhibition"
            elif ppr <= 1.15:
                classification = "Normal Full Synaptic Recovery"
                synaptic_state = "Restoration of readily releasable vesicle pool and normalized resting excitability."
                inhibitory_tone = "Normalized"
            else:
                classification = "Late Post-Inhibitory Rebound Re-Facilitation"
                synaptic_state = "Cortical rebound hyperexcitability at long recovery latencies."
                inhibitory_tone = "Rebound Facilitation"

        return {
            "status": "success",
            "inter_stimulus_interval_ms": round(inter_stimulus_interval_ms, 1),
            "unconditioned_amplitude_a1_uv": round(unconditioned_amplitude_a1_uv, 3),
            "conditioned_amplitude_a2_uv": round(conditioned_amplitude_a2_uv, 3),
            "paired_pulse_ratio": round(ppr, 3),
            "inhibition_percentage": round(suppression_pct, 1),
            "signal_to_noise_ratio": round(unconditioned_amplitude_a1_uv / (baseline_noise_uv + 1e-6), 1),
            "evaluation": {
                "classification": classification,
                "inhibitory_tone": inhibitory_tone,
                "synaptic_state": synaptic_state
            }
        }
