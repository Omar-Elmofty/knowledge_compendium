# Motion Planning

Collection of notes about motion planning algorithms.


Breadth-First Search: FIFO queue
Depth first search: LIFO queue
Dijkstra: Priority queue with just the g value
A*: priority queue with the f values, f = g + h

PRM: Build a road map probabilistically. Sample points in the configuration space, then connect neighbors to each other. This forms a roadmap which is a graph that could be searched using A*. probabilistically complete.

PRM*: uses a dynamic connection radius that reduces as the number of samples increase. Asymptotically optimal.

LazyPRM*: Delays collision checking to when the path is actually queried, this is better for dense graphs.

RRT: Expand a tree from the start, by sampling points in the configuration space and then connection this randomly sampled node to the closest node in the tree. You end up with a tree with branching. Only connecting to ONE nearest neighbor. Probabilistically complete. Will almost never obtain an optimal solution.

RRT-Connect: Builds 2 trees, one from the start and one from the goal, and have them connect in the middle.

RRT*: Instead of connecting to the nearest vertex like RRT does, we will connect to the most optimal vertex (within a local region) the will result in the lowest cost. Then we will look at the all the neighbors in that region, and see if they should be children of this newly added node. So it is a two step approach, we don't pick the closest vertex, we instead pick the optimal one, we also rewire neighbors to make paths leading to them more optimal. (Probabilistically complete and optimal).

Informed RRT*: Uses the current best path to bound the search.




Kalman Filter: 2 step approach, motion model (predict step) where you propagate the state forward, then measurement model where you update the belief based on measurements



SQP: sequentially approximate the non-linear function as quadratic and the constraints as linear
SLQ: Sequential Linear quadratic programming
LQR: The linear quadratic regulator

The Key Insight: An unconstrained Finite Horizon LQR problem, when solved at every time step with a receding horizon, is mathematically equivalent to an unconstrained Linear MPC (LMPC) problem.


ILQC: Iterative Linear quadratic regulator. It is a more generalized version of the LQR, it doesn't assume quadratic cost or linear constraints, it instead assumes


LQG: The linear quadratic guassian.
MPC: finite horizon LQR but re-evaluated every cycle

```{tableofcontents}
```
