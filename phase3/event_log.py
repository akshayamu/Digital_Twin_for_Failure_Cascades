class EventLog:
    def __init__(self):
        self.events = []

    def log(self, time_step, node_id, state, cause=None):
        self.events.append({
            "time": time_step,
            "node": node_id,
            "state": state.value,
            "cause": cause
        })

    def get_events(self):
        return self.events
