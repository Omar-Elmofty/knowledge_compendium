# Multi-agent path finding

> **Good Links**
> Also, a curated list of MAPF papers can be found here https://github.com/joonyeol-sim/awesome-mapf, also more information can be found in https://mapf.info/


In this section contains notes about multiple multi-agent path finding (MAPF) algorithms.

MAPF algorithms can often be split into **Centralized** vs. **Decentralized planners**. See brief descriptions below:

## Centralized Methods

Centralized methods involve a central planner making the decision for all agents. Think of it as the "Traffic Light" solution, where the traffic light (green, yellow, red) organizes all the agents.

Advantages:
1. No synchronization concerns, decision is made in a central location with states of all agents known.
2. Can guarantee an optimal solution since the state of all agents is known, and the decision is made centrally.
3. Is often complete, can find a solution when one exists.
4. Better global coordination / Predictability since the central planner now is capable of reasoning about the state of all the agents.
5. Easier to implement and debug since all decision-making logic resides in one place.

Disadvantages:
1. Single point of failure
2. Harder to scale for large fleets of robots (curse of dimensionality, with more agents the problem can become intractable).
3. Communication overhead, central sever must be able to communicate with all agents (requiring large communication infrastructure), this can induce latency in decision making, vs agents communicating peer to peer (via bluetooth for example) for the distributed case.
4. Not as flexible for dynamic environments. For central planner to deal with all the changes in environment of all agents is very tricky, and it won't be capable of resolving the MAPF problem every time we have a change in the environment.

Popular centralized MAPF planners:
1. A* in joint space of all agents.
2. CBS (conflict base search)
3. ICTS (Increasing Cost tree search).

## Decentralized (Distributed) methods

Distributed methods involve the decision being distributed across all agents. A good example is a "Roundabout" for intersection management, where each agent entering the roundabout makes the decision on whether to yield or not to others. This is opposed to the "Traffic Light" case.

Advantages:
1. Scalable, each cluster of robots can reason about their state and coordinate locally and independently of the rest of the fleet.
2. Often more robust than centralized planner. With the central planner, if it makes a mistake or fails, it impacts the entire fleet. However, with the distributed case, if one agents makes a mistake, the other agents can still coordinate around it and make better decisions.
3. More suited for highly dynamic environments, since the decision and compute is distributed across all agents, so each agent an independently deal with changes to its dynamic environment.
4. Lower communication overhead, agents can locally communicate with each other, and don't need the entire fleet to be connected to a single planning server.
5. Lower compute overhead, each agent just solves the coordination problem locally which is much cheaper than the solving the problem for all fleet at once.

Disadvantages:
1. Often suboptimal, since the decision is distributed across all agent, and as opposed to the central planner where the central planner had knowledge of all the state of the environment which makes capable of making good decisions, we don't have this in the distributed case.
2. Often incomplete, they can't find a solution if one exits.
3. Synchronization concerns, failure in agents properly communicating with each other, or communication delays can cause agents to not all agree on the same (correct) decision, resulting in sub-optimal behavior.
4. Can be super hard to develop and debug, you have to reason about the state of all agents involved in the coordination activity.
5. Can be less predictable, and can cause local conflicts / deadlocks that are hard to resolve.

Popular decentralized methods:
1. Prioritized planning
2. Token Passing
3. Rule based methods


```{tableofcontents}
```
