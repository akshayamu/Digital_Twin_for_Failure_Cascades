# Phase 1 — Problem Definition and Scope Lock

## 1. System Overview

This project models a **single hospital** as a closed system in order to study
**failure cascades caused by capacity stress**.

The hospital is represented as a network of interdependent nodes (departments,
staff pools, and control functions). The objective is not to predict outcomes,
but to **explain how failures propagate through the system over time**.

---

## 2. Time Horizon

**72 hours**

This time horizon is chosen to:
- Allow second- and third-order cascades to emerge
- Capture delayed failures (boarding, staff overload)
- Avoid long-term recovery dynamics, which are out of scope

All simulations and reasoning are constrained to this window.

---

## 3. System Boundary (In Scope)

The model includes only components that directly affect **capacity propagation**
inside the hospital.

### Included
- Patient intake, flow, and internal transfers
- Departmental capacity constraints
- Staff availability as a limiting resource
- Control logic governing bed allocation

### Explicitly Excluded
- Individual patient outcomes
- Clinical decision quality
- Medical diagnosis accuracy
- Financial costs or billing
- Long-term staffing recovery or hiring
- Policy, regional, or national healthcare effects

If a factor does not directly contribute to capacity stress or cascade behavior,
it is excluded by design.

---

## 4. Node Definitions (Frozen)

The system consists of exactly **8 nodes**:

1. **Emergency Department (ED)**  
   Entry point for patients and primary source of demand.

2. **Intensive Care Unit (ICU)**  
   High-acuity care with strict capacity and staffing constraints.

3. **General Ward**  
   Medium-acuity inpatient care and primary bed volume.

4. **Surgery / Operating Rooms (OR)**  
   Scheduled and emergency procedures with downstream bed dependencies.

5. **Diagnostics (Lab + Imaging)**  
   Enables patient discharge and care progression; delays create bottlenecks.

6. **Nursing Staff Pool**  
   Shared staffing resource across all clinical departments.

7. **Physician Staff Pool**  
   Shared physician capacity supporting clinical operations.

8. **Bed Management / Patient Flow Control**  
   Control function governing admissions, transfers, and discharges.

No additional nodes will be added in Project B.

---

## 5. Failure Semantics

Failure is defined as **loss of functional capacity**, not total shutdown.

Each node can exist in one of three states:

- **Healthy:** Operating within safe capacity limits
- **Stressed:** Capacity limits approached or exceeded, throughput degraded
- **Failed:** Functional role compromised, causing upstream or downstream pressure

### Example — Emergency Department (ED)

- **Healthy:**  
  Patient wait times within acceptable limits; normal intake flow.

- **Stressed:**  
  Rising wait times; patient boarding due to downstream bed constraints.

- **Failed:**  
  Ambulance diversion activated; ED becomes a holding area rather than an intake node,
  propagating stress to staff pools and bed management.

All other nodes will follow this same semantic structure.

---

## 6. Dependency Logic (Conceptual)

Cascades occur due to:
- Shared staffing resources
- Bed availability constraints
- Delayed discharges
- Control logic bottlenecks

Examples:
- ICU saturation increases ED boarding
- Nursing staff loss reduces effective capacity across multiple departments
- Diagnostics delays slow discharges, feeding back into bed scarcity

Dependencies are causal, not predictive.

---

## 7. MVP Question (Scope Guardrail)

**This digital twin answers exactly the following question and nothing more:**

> **“If Hospital A suddenly loses 20% of its nursing staff, which departments fail next, in what order, and why—over a 72-hour period?”**

Questions about optimization, intervention, or alternative shocks are explicitly
out of scope for Project B.

---

## 8. Phase Status

Phase 1 is **complete and frozen**.

Any change to:
- time horizon,
- node list,
- failure semantics,
- or MVP question

requires reopening Phase 1 and invalidates downstream work.
