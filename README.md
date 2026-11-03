# Somatosensory Paired-Pulse Depression (PPD) Skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://www.python.org/)
[![OpenClaw](https://img.shields.io/badge/ecosystem-OpenClaw-orange.svg)](https://openclaw.org/)
[![GenPark](https://img.shields.io/badge/sovereign-GenPark-purple.svg)](https://alphapark.ai/)
[![MCP](https://img.shields.io/badge/protocol-MCP-success.svg)](https://modelcontextprotocol.io/)

Somatosensory Paired-Pulse Depression (PPD) and Synaptic Plasticity Evaluator based on neurophysiological evoked potential analysis.

```mermaid
flowchart TD
    A[Paired Nerve Stimulation: Conditioning S1 & Test S2] --> B[Record Evoked Potentials: A1 & A2]
    B --> C[Compute Paired-Pulse Ratio: PPR = A2 / A1]
    C --> D[Compute Synaptic Inhibition Percentage: 1 - PPR * 100%]
    D --> E{PPR Threshold at Short ISI}
    E -- < 0.70 --> F[Intact Intracortical GABAergic Gating]
    E -- >= 1.00 --> G[Cortical Disinhibition / Hyperexcitability]
```

## Features
- **Zero PIP Dependencies**: Implemented strictly with Python Standard Library (`math`, `json`, `sys`, `typing`).
- **Short-Interval Intracortical Inhibition**: Quantifies sensorimotor cortex gating and inhibitory tone.
- **Interval Sensitivity**: Analyzes both short (10-50 ms) and long (50-200 ms) recovery regimes.
- **Dual Architecture**: Native Python import and Model Context Protocol (MCP) JSON-RPC 2.0 stdio server.

## Quickstart
```bash
python example_usage.py
```

## License
Apache-2.0
