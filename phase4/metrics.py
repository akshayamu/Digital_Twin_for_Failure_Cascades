from collections import defaultdict


def extract_metrics(event_log):
    """
    Extracts risk-relevant metrics from a cascade event log.
    """

    first_stress = None
    first_failure = None
    bed_mgmt_failure_time = None
    ed_stress_time = None

    seen_stress = set()
    seen_failure = set()

    for event in event_log:
        time = event["time"]
        node = event["node"]
        state = event["state"]

        if state == "stressed" and node not in seen_stress:
            seen_stress.add(node)
            if first_stress is None:
                first_stress = (node, time)

            if node == "ED" and ed_stress_time is None:
                ed_stress_time = time

        if state == "failed" and node not in seen_failure:
            seen_failure.add(node)
            if first_failure is None:
                first_failure = (node, time)

            if node == "BED_MGMT" and bed_mgmt_failure_time is None:
                bed_mgmt_failure_time = time

    return {
        "first_stress": first_stress,
        "first_failure": first_failure,
        "bed_mgmt_failure_time": bed_mgmt_failure_time,
        "ed_stress_time": ed_stress_time,
        "total_failed_nodes": len(seen_failure)
    }
