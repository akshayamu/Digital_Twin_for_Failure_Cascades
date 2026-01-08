# Phase 5 — Narrative Decision Interface  
## Digital Twin for Hospital Failure Cascades

---

## 1. Problem Framing

Hospitals often appear stable until they suddenly are not.  
Capacity stress rarely causes immediate collapse; instead, it propagates silently through interdependent departments until a tipping point is crossed.

This project studies how **staffing shocks**, specifically nursing capacity loss, can trigger **nonlinear failure cascades** in a hospital system—failures that are not visible through traditional monitoring until it is too late.

The objective is not prediction or optimization, but **causal explanation**: understanding *how*, *when*, and *why* a hospital stops functioning as a coherent system.

---

## 2. System Overview

The hospital is modeled as a **causal digital twin** composed of eight interdependent nodes:

- Emergency Department (ED)  
- Intensive Care Unit (ICU)  
- General Ward  
- Surgery / Operating Rooms  
- Diagnostics (Lab + Imaging)  
- Nursing Staff Pool  
- Physician Staff Pool  
- Bed Management / Patient Flow Control  

Each node has capacity limits and operational thresholds.  
Failure is defined as **loss of functional capacity**, not total shutdown.

The system is simulated over a **72-hour horizon**, sufficient to observe second- and third-order cascades without introducing long-term recovery dynamics.

---

## 3. Stress Scenario

The system is stressed by **reducing nursing capacity** in controlled increments:

0%, 10%, 20%, 30%, 40%, and 50%

All other parameters remain fixed.  
This isolates causality and allows identification of tipping points.

---

## 4. Observed System Behavior

### Stable Regime (0–10% Nursing Loss)

At low levels of nursing loss, the system absorbs stress:

- Nursing stress appears but does not propagate
- No departments fail
- Bed Management remains functional
- ED operations remain unaffected

This confirms the system does **not overreact** to minor stress and behaves realistically under normal degradation.

---

### Tipping Point (~20% Nursing Loss)

At approximately **20% nursing loss**, the system undergoes a **regime shift**:

- **ICU is the first department to show stress**
- Nursing fails immediately due to threshold breach
- ICU and Surgery failures follow
- **Bed Management fails shortly after**
- **ED stress appears only after Bed Management failure**

At this point, collapse becomes **irreversible**.  
Additional time or capacity does not restore functionality.

---

### High-Stress Regime (30–50% Nursing Loss)

Beyond the tipping point:

- System behavior is qualitatively identical
- Collapse occurs with higher certainty, not different dynamics
- Additional stress does not change *what* fails, only *how predictably*

This demonstrates classic **nonlinear system behavior**.

---

## 5. Key Insights

- **ICU stress is the earliest reliable warning signal**
- **Bed Management failure marks the point of no return**
- ED congestion is a **late, lagging indicator**, not an early warning
- Small staffing losses can trigger disproportionate system-wide collapse
- Control failures amplify damage more than individual capacity losses

---

## 6. Decision-Relevant Implications

Monitoring ED congestion alone provides **false confidence**.  
By the time ED stress appears, the system has already lost coordination.

Effective intervention must occur:
- when ICU stress first emerges
- **before** Bed Management collapses

This reframes hospital resilience from “handling surges” to **preserving control and coordination under stress**.

---

## 7. Why This Model Matters

This digital twin does not aim to predict outcomes or optimize staffing levels.

It provides:
- a stress-testing framework
- visibility into hidden fragility
- identification of misleading indicators
- causal explanations suitable for high-stakes decisions

Although demonstrated on a hospital, the same architecture applies to:
- power grids
- supply chains
- cloud infrastructure
- financial systems

The domain changes; the failure mechanics do not.

---

## 8. Scope and Limitations

This model intentionally excludes:
- clinical outcomes
- patient-level optimization
- long-term recovery dynamics
- real-time monitoring

Its purpose is **failure understanding**, not operational control.

---

## 9. Project Status

Project B — Digital Twin for Failure Cascades  
**Status: Complete**