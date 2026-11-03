---
name: genpark-personal-agent-somatosensory-paired-pulse-depression-ppd-skill
description: Paired-Pulse Depression (PPD) and Facilitation (PPF) synaptic plasticity analyzer. Evaluates inter-stimulus interval somatosensory evoked potential amplitude ratios (A2 / A1) to quantify cortical GABAergic intracortical inhibition.
version: 1.0.0
author: GenPark Ecosystem
license: Apache-2.0
tags:
  - personal-agent
  - neurophysiology
  - paired-pulse
  - intracortical-inhibition
  - gaba
  - openclaw
  - genpark
  - mcp
---

# Somatosensory Paired-Pulse Depression (PPD) Skill

## Overview
This skill computes synaptic short-term depression and sensorimotor gating:
- **Conditioning-Test Paradigm**: Two identical electrical peripheral nerve stimuli are delivered at short inter-stimulus intervals (ISI: 10 - 100 ms).
- **Paired-Pulse Ratio ($A_2 / A_1$)**: The response of the second evoked cortical potential ($A_2$) is typically attenuated ($A_2 / A_1 < 0.70$) due to presynaptic transmitter depletion and feed-forward GABAergic inhibitory interneuron activation.
- **Cortical Disinhibition**: Elevation or loss of PPD ($A_2 / A_1 \ge 1.0$) marks cortical hyperexcitability, dystonia, or impaired sensory filtering.

## Mathematical Formulation
1. **Paired-Pulse Ratio (PPR)**:
   $$\text{PPR} = \frac{A_2}{A_1}$$
2. **Inhibition Percentage**:
   $$\text{Inhibition} = \max\left(0, (1 - \text{PPR}) \times 100\%\right)$$
3. **Signal-to-Noise Ratio (SNR)**:
   $$\text{SNR} = \frac{A_1}{\text{Noise}_{\text{RMS}}}$$

## Usage
```python
from client import PairedPulsePlasticityClient

client = PairedPulsePlasticityClient()
res = client.evaluate_paired_pulse(
    unconditioned_amplitude_a1_uv=2.40,
    conditioned_amplitude_a2_uv=1.10,
    inter_stimulus_interval_ms=30.0
)
print(res["evaluation"]["classification"])
```
