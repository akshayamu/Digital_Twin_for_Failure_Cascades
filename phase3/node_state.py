from enum import Enum


class NodeState(Enum):
    HEALTHY = "healthy"
    STRESSED = "stressed"
    FAILED = "failed"


def evaluate_node_state(current_load, stress_threshold, failure_threshold):
    """
    Determines the state of a node based on its load.
    """
    if current_load >= failure_threshold:
        return NodeState.FAILED
    elif current_load >= stress_threshold:
        return NodeState.STRESSED
    else:
        return NodeState.HEALTHY
