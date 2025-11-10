# Control Barrier Functions

Similar to the [Control Lyapunov function](control_lyapunov_functions.md), which uses the Lyapunov Stability theory but includes the input in the equation to make the system stable, the control barrier function uses the [Nagumo's Invariance Principle](nagumos_invariance_principle.md), adding the input into the mix to define a safe system.


Remember the system that we've formulated before:

$$
\dot{x} = f(x, u)
$$

Where $u$ is the control input.

Again, in this context, we will treat $x$ and $u$ as two independent variables since we don't have a controller designed yet, and we will be trying to build a controller that regulates $u$ such that our system is safe.

So let's start by defining the $B(x)$ function, which is similar to the $h(x)$ function in Nagumo's Invariance Principle (it defines the safe set). $B(x)$ must satisfy the following conditions:


$$
Barrier\ function: B(x)
$$

$$
B(x) \geq 0 \ \forall x \in C
$$

And:

$$
\dot{B}(x, u) \ge 0 \ \forall x \in \partial C
$$

Where $\partial C$ is the boundary of the safe set C.

We now have to simply find the controller that regulates $u$ such that the above conditions are satisfied. This will ensure that the system will remain in the safe set C.
