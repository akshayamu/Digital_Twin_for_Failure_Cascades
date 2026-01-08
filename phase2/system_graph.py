"""
Phase 2 — Static Digital Twin Graph

This module defines the static hospital system as a directed graph.
It contains:
- node definitions
- node attributes
- dependency edges

No simulation, failure logic, or time dynamics are included here.
"""

import networkx as nx


def build_hospital_graph():
    """
    Constructs and returns the static hospital digital twin graph.
    """

    G = nx.DiGraph()

    # -------------------------
    # Node Definitions
    # -------------------------
    nodes = {
        "ED": {
            "name": "Emergency Department",
            "node_type": "clinical",
            "capacity": 100,
            "current_load": 60,
            "stress_threshold": 75,
            "failure_threshold": 100,
            "recovery_lag": 24
        },
        "ICU": {
            "name": "Intensive Care Unit",
            "node_type": "clinical",
            "capacity": 40,
            "current_load": 25,
            "stress_threshold": 30,
            "failure_threshold": 40,
            "recovery_lag": 48
        },
        "WARD": {
            "name": "General Ward",
            "node_type": "clinical",
            "capacity": 200,
            "current_load": 140,
            "stress_threshold": 160,
            "failure_threshold": 200,
            "recovery_lag": 72
        },
        "OR": {
            "name": "Surgery / Operating Rooms",
            "node_type": "clinical",
            "capacity": 30,
            "current_load": 18,
            "stress_threshold": 22,
            "failure_threshold": 30,
            "recovery_lag": 24
        },
        "DIAGNOSTICS": {
            "name": "Diagnostics (Lab + Imaging)",
            "node_type": "clinical",
            "capacity": 120,
            "current_load": 70,
            "stress_threshold": 90,
            "failure_threshold": 120,
            "recovery_lag": 12
        },
        "NURSING": {
            "name": "Nursing Staff Pool",
            "node_type": "staff",
            "capacity": 100,
            "current_load": 85,
            "stress_threshold": 80,
            "failure_threshold": 100,
            "recovery_lag": 72
        },
        "PHYSICIANS": {
            "name": "Physician Staff Pool",
            "node_type": "staff",
            "capacity": 60,
            "current_load": 50,
            "stress_threshold": 48,
            "failure_threshold": 60,
            "recovery_lag": 72
        },
        "BED_MGMT": {
            "name": "Bed Management / Patient Flow Control",
            "node_type": "control",
            "capacity": 1.0,
            "current_load": 0.5,
            "stress_threshold": 0.7,
            "failure_threshold": 1.0,
            "recovery_lag": 12
        },
        "AMBULANCE": {
            "name": "Ambulance Intake",
            "node_type": "inflow",
            "capacity": 80,
            "current_load": 55,
            "stress_threshold": 60,
            "failure_threshold": 80,
            "recovery_lag": 0
        }
    }

    for node_id, attrs in nodes.items():
        G.add_node(node_id, **attrs)

    # -------------------------
    # Dependency Edges
    # -------------------------
    edges = [
        ("AMBULANCE", "ED"),
        ("ED", "BED_MGMT"),

        ("BED_MGMT", "ICU"),
        ("BED_MGMT", "WARD"),
        ("BED_MGMT", "OR"),

        ("ICU", "NURSING"),
        ("WARD", "NURSING"),
        ("OR", "NURSING"),

        ("ICU", "PHYSICIANS"),
        ("WARD", "PHYSICIANS"),
        ("OR", "PHYSICIANS"),

        ("DIAGNOSTICS", "BED_MGMT")
    ]

    G.add_edges_from(edges)

    return G


if __name__ == "__main__":
    graph = build_hospital_graph()
    print(f"Nodes: {graph.number_of_nodes()}")
    print(f"Edges: {graph.number_of_edges()}")

    for node, data in graph.nodes(data=True):
        print(node, data)
