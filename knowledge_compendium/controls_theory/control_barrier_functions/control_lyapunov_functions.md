# Control Lyapunov Functions (CLFs)

I've gone over the [Lyapunov Stability Theorem](lyapunov_theory.md) (if you haven't read that yet, please go over this section).


We now will introduce control into our system, so our system can be formulated as:

$$
\dot{x} = f(x, u)
$$

Where $u$ is the control input.
In this context, we will treat $x$ and $u$ as two independent variables since we don't have a controller designed yet, and we will be trying to build a controller that regulates $u$ such that our system is stable.

So let's start by defining the Lyapunov function after we've introduced the new system with the control $u$ introduced:

$$
Lyapunov\ function: V(x)
$$

Where:

$$
V(x_e) = 0, V(x) > 0\ \forall x \neq x_e
$$

$$
\dot{V}(x, u) < 0\ \forall x \neq x_e
$$

![test](../../diagrams/exported/control_lyapunov_function.png)

Hence, if we could pick a controller that will regulate $u$ such that the condition $\dot{V}(x, u) < 0$ is satisfied, then we have designed a controller that stabilizes the system. This will be the goal of the following sections. In the following sections, we will design a QP controller that utilizes the control Lyapunov function to make the system stable.
