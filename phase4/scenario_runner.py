from phase3.cascade_engine import CascadeEngine
from phase4.metrics import extract_metrics


NURSING_LOSS_LEVELS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
TIME_HORIZON = 72


def run_scenario(nursing_loss):
    engine = CascadeEngine()
    engine.apply_nursing_staff_shock(nursing_loss)

    for _ in range(TIME_HORIZON):
        engine.step()

    metrics = extract_metrics(engine.event_log.get_events())
    metrics["nursing_loss"] = nursing_loss
    return metrics


def run_all_scenarios():
    results = []

    for loss in NURSING_LOSS_LEVELS:
        metrics = run_scenario(loss)
        results.append(metrics)

    return results


if __name__ == "__main__":
    results = run_all_scenarios()

    for r in results:
        print(f"\nNursing loss: {int(r['nursing_loss']*100)}%")
        print(f"  First stress: {r['first_stress']}")
        print(f"  First failure: {r['first_failure']}")
        print(f"  BedMgmt failure time: {r['bed_mgmt_failure_time']}")
        print(f"  ED stress time: {r['ed_stress_time']}")
        print(f"  Total failed nodes: {r['total_failed_nodes']}")
