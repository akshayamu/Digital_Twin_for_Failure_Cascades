# Digital Twin for Failure Cascades (Project B)

## Overview

This project implements a **causal digital twin** to study how **capacity stress propagates through a complex system**, leading to nonlinear failure cascades.

The system is intentionally **not predictive** and **not machine-learning driven**.  
Its purpose is to **explain how and why failures spread**, identify tipping points, and reveal misleading indicators in high-stakes systems.

The reference domain used here is **hospital capacity planning**, but the architecture generalizes to infrastructure, supply chains, cloud systems, and financial networks.

---

## Core Question

**If Hospital A suddenly loses 20%–50% of its nursing staff, which departments fail next, in what order, and why—over a 72-hour period?**

---

## Why This Project Exists

Most engineering and ML projects focus on:
- performance under normal conditions
- prediction of outcomes
- optimization of averages

This project focuses on:
- **failure modes**
- **nonlinear cascades**
- **threshold effects**
- **control vs capacity breakdown**
- **early vs late warning signals**

It answers questions decision-makers actually face:
> “What breaks first?”  
> “When does collapse become inevitable?”  
> “Which signals are misleading?”

---

## System Architecture

The model uses a **graph-based causal simulation architecture**.

### Nodes (Capacity & Control)
- Emergency Department (ED)
- Intensive Care Unit (ICU)
- General Ward
- Surgery / Operating Rooms
- Diagnostics (Lab + Imaging)
- Nursing Staff Pool
- Physician Staff Pool
- Bed Management / Patient Flow Control

### Key Properties
- Nodes have capacities and thresholds
- Failure = loss of functional capacity (not shutdown)
- Cascades propagate through dependencies
- Simulation is discrete-time and explainable

---

## Project Phases

### Phase 1 — Problem & Scope Lock
- Defined system boundary and exclusions
- Locked time horizon (72 hours)
- Fixed node set and failure semantics

### Phase 2 — Static Digital Twin
- Built the dependency graph
- Assigned capacities, loads, and thresholds
- No simulation or failure logic

### Phase 3 — Failure & Cascade Engine
- Implemented node states (healthy / stressed / failed)
- Introduced threshold-driven failure
- Modeled causal stress propagation
- Logged failures with explicit causes

### Phase 4 — Scenario & Risk Exploration
- Ran controlled stress scenarios (0%–50% nursing loss)
- Identified tipping points
- Measured cascade order and timing
- Distinguished early vs late warning signals

### Phase 5 — Narrative Decision Interface
- Converted results into decision-grade explanations
- Explained collapse mechanisms clearly
- Removed technical noise in favor of insight

---

## Key Findings

- **System collapse exhibits a sharp tipping point at ~20% nursing loss**
- **ICU stress is the earliest reliable warning signal**
- **Bed Management failure marks the point of no return**
- **ED congestion is a late, misleading indicator**
- Control failures amplify damage more than local capacity loss

---

## What This Model Is (and Is Not)

### This model IS:
- a failure cascade simulator
- a stress-testing instrument
- a systems risk analysis tool
- decision-support oriented

### This model is NOT:
- a machine learning model
- a predictive system
- a dashboard product
- a real-time monitoring tool

Machine learning, if added, belongs to a **separate follow-on project**.

---

## Repository Structure



Digital_Twin_for_Failure_Cascades/
├── phase1/ # Problem definition & scope lock
├── phase2/ # Static digital twin (graph)
├── phase3/ # Failure & cascade engine
├── phase4/ # Scenario & risk exploration
├── phase5/ # Narrative decision interface
├── README.md
├── requirements.txt
└── .gitignore


---

## How to Run

From project root:

```bash
# Run a single cascade
python -m phase3.cascade_engine

# Run all stress scenarios
python -m phase4.scenario_runner

Transferability

Although demonstrated on hospitals, the same architecture applies to:

power grids

supply chains

cloud infrastructure

financial contagion

disaster resilience planning

Only the domain labels change — the failure mechanics do not.