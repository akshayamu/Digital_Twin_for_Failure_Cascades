Build Log (What Actually Happened)

This project was not built in a straight line.
Most of the value came from things breaking, and then understanding why they broke.

Early mistakes

At the beginning, I treated this like a normal ML-style project.
I was thinking in terms of prediction and outputs instead of system behavior.

That was wrong.

I initially tried to:

propagate failures in the wrong graph direction

treat stress and failure as the same thing

rely on output states without tracking causal reasons

This caused the system to “fail” but not explain why.
That was the first big red flag.

Major failure #1 — Cascades did not propagate

The first working version showed nursing failing, but nothing else followed.

At first I thought this was a bug.

It turned out to be a modeling error:

I was propagating failure to downstream nodes

but resource failures propagate to dependent nodes (upstream)

Fixing this required rethinking:

dependency direction vs failure direction

control flow vs resource flow

Once corrected, the cascade became realistic and explainable.

This was a turning point in the project.

Major failure #2 — Everything failed too early

After fixing propagation, the system collapsed instantly in all scenarios.

This made the model useless.

The issue was:

no distinction between stress and failure

no time separation between degradation and collapse

Introducing a stressed state fixed this and allowed:

early warning signals

delayed collapse

realistic intervention windows

This is where the model stopped being a toy.

Phase discipline (hard but necessary)

Several times I wanted to:

add ML

add dashboards

add more realism

Each time, I stopped and froze the phase instead.

This discipline was intentional:

Phase 2 stayed static

Phase 3 handled mechanics only

Phase 4 handled exploration only

Phase 5 handled explanation only

This kept the project coherent.

Time investment (realistic)

This project evolved over multiple weeks of iteration:

thinking

rewriting

deleting code

re-reading assumptions

testing edge cases

Most of the time was not spent coding.
It was spent understanding why the system behaved the way it did.

What I Learned (Technically)

Failure propagation is often opposite of dependency direction

Control nodes matter more than capacity nodes

Thresholds create nonlinear behavior

Stress is more important than failure for early warning

Late indicators (like ED congestion) are misleading

Simple models can reveal deep fragility if scoped correctly

Most importantly:

Explaining failure is harder — and more valuable — than predicting success.

How I Would Explain 
“What problem were you solving?”

I was not trying to predict hospital overload.
I was trying to understand how small staffing losses turn into system-wide collapse, and where early warning signals actually appear.

“Why didn’t you use machine learning?”

Because the problem is causal, not statistical.

We already know the system structure.
The challenge is modeling thresholds, dependencies, and nonlinear cascades, not fitting patterns from data.

ML would hide the very mechanisms I needed to expose.

“What was the hardest part?”

Getting the direction of failure propagation right.

The system failed many times in ways that looked correct numerically but were wrong logically.
Fixing that required stepping back and reasoning about real-world behavior, not code.

“What makes this project strong?”

It models failure, not performance

It identifies tipping points

It separates early vs late indicators

It is explainable end-to-end

It shows judgment, not just implementation

“What would you improve next?”

Add probabilistic delays (Monte Carlo)

Test alternative shock types

Extend to another domain (power grid or logistics)

Only then consider ML as a separate layer

Why This Project Exists

This project exists to demonstrate systems thinking, not tooling.

The domain is healthcare.
The skill is risk engineering.