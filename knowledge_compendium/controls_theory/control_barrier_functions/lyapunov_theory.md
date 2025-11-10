# Lyapunov Stability Theory


The Lyapunov stability theory states that first, given a dynamical system with the dynamics defined as:

$$
\dot{x} = f(x)
$$

You could prove that the system is **stable** around an equilibrium point $x_e$ if you could define a function $V(x)$ that satisfies the following conditions:

$$
V(x_e) = 0,\ V(x) > 0\ for\ x\neq x_e
$$
$$
\dot{V}(x) = \frac{\partial V}{\partial x}f(x)<0\ for\ x\neq x_e
$$


You could visualize $V(x)$ like the surface in the diagram below.

![test](../../diagrams/exported/lyapunov_stability_theorm.png)

You could also think of $V(x)$ as an energy function, where if you could prove that the energy of the system always goes down as time passes, reaching zero energy at $x_e$, then you've proven that the system is stable about $x_e$. For example, you could imagine $V(x)$ as a bowl, with a ball that rolls inside of it, where gravity always guarantees that the ball always rolls down to the bottom of the bowl.

One might ask, why is the Lyapunov Stability theorem useful? It is useful since the system dynamics may be highly non-linear, and it could be hard to reason about what the system will do in the future. However, if we could just find a function $V(x)$ that satisfies the above conditions, then we could prove that the system is stable, no matter how complicated the system dynamics are.

## Invariance at every sublevel

Another property that we get as a result of defining $V(x)$ as above is that every sublevel of $V(x)$ is an *invariant set*. Let's break this down a bit:
- **Sublevel**: This is the set $\Omega_c = \{x | V(x) \leq c\}$
- **Invariant set**: This is a set where, if the system starts inside it, it will always remain in it as time evolves. You can think of it as the system being trapped within that set.

In summary, as the system starts at a specific sublevel $V(x) = c$, it will always follow a trajectory that guarantees that $V(x) \leq c$, hence the system stays within the set $\Omega_c$ which is invariant.