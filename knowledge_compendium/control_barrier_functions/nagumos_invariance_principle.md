# Nagumo's Invariance Principle

Nagumo's Invariance principle is very similar to [Lyapunov Stability Theorem](lyapunov_theory.md) but with a subtle difference. While Lyapunov Theory was concerned with the stability of the system around an equilibrium point, Nagumo's Invariance principle is concerned with the system trajectory being bounded by a specific set.

Again given that you have a system where:
$$
\dot{x} = f(x)
$$

Let's consider a function $h(x)$, where the set $C$ is defined as:
$$
C = {x | h(x) \geq 0}
$$

The set $C$ forms the boundary of the safe set that we're concerned with. If $h(x)$ satisfies the following condition:
$$
\dot{h}(x) \geq 0
$$
$$
\forall x \in \partial{C}
$$
Where $\partial{C}$ is the boundary of the set $C$.

See the below diagram for more illustration.
![nagumos_invariance_principle](../diagrams/exported/nagumos_invariance_principle.png)

What the above conditions enforce is that the trajectory of the system is free to navigate and evolve in the set $C$, however, it is not allowed to get outside of it. That's because whenever the system will approach the boundary of $C$ it will get pushed back into the set because of the condition $\dot{h}(x) \geq 0$.

This means that the set $C$ is an invariant set, meaning that the trajectory of the system will remain inside of $C$ as the system will evolve over time.

Note that the difference between $h(x)$ here and $V(x) in [Lyapunov Stability Theorem](lyapunov_theory.md) is that $V(x)$ had an invariant set at every sublevel, however, $h(x)$ only has an invariant set at the sublevel at $h(x) = 0$. $V(x)$ enforces a stricter requirement at the system to guarantee stability to an equilibrium point, while $h(x)$ is not concerned with keeping the system trajectory within a safe set and not enforcing any stability requirements over the system.

Again similar to $V(x)$ we just need to find one $h(x)$ that works for the system and enforces the above requirements no matter how complicated the dynamics of the system are. If we find $h(x)$ that satisfies the above requirements then we could prove that the system is stable.