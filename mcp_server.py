"""
MCP Server for Somatosensory Paired-Pulse Depression (PPD) Skill.
Conforms to Model Context Protocol (MCP) JSON-RPC 2.0 stdio specification.
"""

import sys
import json
from client import PairedPulsePlasticityClient


def handle_request(line: str) -> None:
    try:
        req = json.loads(line)
    except Exception:
        return

    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "genpark-personal-agent-somatosensory-paired-pulse-depression-ppd-skill",
                    "version": "1.0.0"
                }
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/list":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_paired_pulse",
                        "description": "Calculate Paired-Pulse Depression ratio (A2/A1), suppression percentage, and cortical GABAergic inhibitory tone.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "unconditioned_amplitude_a1_uv": {"type": "number", "description": "Amplitude of first conditioning evoked potential (uV)."},
                                "conditioned_amplitude_a2_uv": {"type": "number", "description": "Amplitude of second test evoked potential (uV)."},
                                "inter_stimulus_interval_ms": {"type": "number", "description": "Inter-stimulus interval in ms (default: 30.0)."},
                                "baseline_noise_uv": {"type": "number", "description": "Recording baseline noise (default: 0.2 uV)."}
                            },
                            "required": ["unconditioned_amplitude_a1_uv", "conditioned_amplitude_a2_uv"]
                        }
                    }
                ]
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_paired_pulse":
            client = PairedPulsePlasticityClient()
            try:
                res = client.evaluate_paired_pulse(
                    unconditioned_amplitude_a1_uv=float(args["unconditioned_amplitude_a1_uv"]),
                    conditioned_amplitude_a2_uv=float(args["conditioned_amplitude_a2_uv"]),
                    inter_stimulus_interval_ms=float(args.get("inter_stimulus_interval_ms", 30.0)),
                    baseline_noise_uv=float(args.get("baseline_noise_uv", 0.2))
                )
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
                    }
                }
            except Exception as e:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32000, "message": str(e)}
                }
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
    else:
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method {method} not found"}
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()


def main():
    for line in sys.stdin:
        if line.strip():
            handle_request(line)


if __name__ == "__main__":
    main()
