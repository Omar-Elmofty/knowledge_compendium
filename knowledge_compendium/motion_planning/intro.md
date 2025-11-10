# Motion Planning

A collection of notes about motion planning algorithms.


Breadth-First Search: FIFO queue
Depth-First Search: LIFO queue
Dijkstra: Priority queue with just the g value
A*: Priority queue with the f values, f = g + h

PRM: Build a roadmap probabilistically. Sample points in the configuration space, then connect neighbors to each other. This forms a roadmap, which is a graph that could be searched using A*. Probabilistically complete.

PRM*: Uses a dynamic connection radius that reduces as the number of samples increases. Asymptotically optimal.

LazyPRM*: Delays collision checking to when the path is actually queried. This is better for dense graphs.

RRT: Expands a tree from the start by sampling points in the configuration space and then connecting this randomly sampled node to the closest node in the tree. You end up with a tree with branching. Only connects to ONE nearest neighbor. Probabilistically complete. Will almost never obtain an optimal solution.

RRT-Connect: Builds two trees, one from the start and one from the goal, and has them connect in the middle.

RRT*: Instead of connecting to the nearest vertex like RRT does, it connects to the most optimal vertex (within a local region) that will result in the lowest cost. Then it looks at all the neighbors in that region and sees if they should be children of this newly added node. So it is a two-step approach: it doesn't pick the closest vertex, but instead picks the optimal one, and it also rewires neighbors to make paths leading to them more optimal. (Probabilistically complete and optimal).

Informed RRT*: Uses the current best path to bound the search.




Kalman Filter: A two-step approach: motion model (predict step), where you propagate the state forward, then measurement model, where you update the belief based on measurements



SQP: Sequentially approximate the non-linear function as quadratic and the constraints as linear
SLQ: Sequential Linear Quadratic Programming
LQR: The Linear Quadratic Regulator

The Key Insight: An unconstrained Finite Horizon LQR problem, when solved at every time step with a receding horizon, is mathematically equivalent to an unconstrained Linear MPC (LMPC) problem.


ILQC: Iterative Linear Quadratic Regulator. It is a more generalized version of the LQR. It doesn't assume quadratic cost or linear constraints; instead, it assumes


LQG: The linear quadratic guassian.
MPC: finite horizon LQR but re-evaluated every cycle

```{tableofcontents}
```
