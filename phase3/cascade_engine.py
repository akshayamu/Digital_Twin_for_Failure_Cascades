from phase2.system_graph import build_hospital_graph
from phase3.node_state import evaluate_node_state, NodeState
from phase3.event_log import EventLog

class CascadeEngine:
    def __init__(self):
        self.graph = build_hospital_graph()
        self.event_log = EventLog()
        self.time = 0

    def apply_nursing_staff_shock(self, reduction_percent):
        nursing = self.graph.nodes["NURSING"]
        nursing["current_load"] += nursing["capacity"] * reduction_percent

    def step(self):
        for node_id, data in self.graph.nodes(data=True):
            state = evaluate_node_state(
                data["current_load"],
                data["stress_threshold"],
                data["failure_threshold"]
            )

            self.event_log.log(
                time_step=self.time,
                node_id=node_id,
                state=state
            )

            if state == NodeState.FAILED:
                self.propagate_failure(node_id)
        self.time += 1

    def propagate_failure(self, failed_node):
        for dependent in self.graph.predecessors(failed_node):
            self.graph.nodes[dependent]["current_load"] += 10
            self.event_log.log(
                time_step=self.time,
                node_id=dependent,
                state=NodeState.STRESSED,
                cause=failed_node
             )    

# FIX: Move these lines to level 0 (no indentation)
if __name__ == "__main__":
    engine = CascadeEngine()
    engine.apply_nursing_staff_shock(0.2)

    for _ in range(5):
        engine.step()

    for event in engine.event_log.get_events():
        print(event)