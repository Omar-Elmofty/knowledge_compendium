# Prioritized Planning

The whole idea of prioritized planning is that:
1. Each agent will have a priority, then agents plan their paths one at a time.
2. Highest priority agent plans its path in the environment.
3. Lower priority agents plan their paths with respect to the higher priority agents, ensuring they don't collide with them and respect them.

As you can see, this approach is not optimal as, first you have to rank agents by priority and you don't have a way to have 2 agents have the same priority.
Second, is that you can't have a globally optimal solution this way.

Advantages:
1. Simplicity: Simple to understand and implement.
2. Can run both in a centralized or distributed fashion, so it inherits the advantages of each.

Disadvantages:
1. Incomplete: Doesn't guarantee finding a solution if one exists, for example, the highest priority agent may make a plan that makes it impossible for all other agents to find a path and reach their goals.
2. Suboptimal: Even if a solution is found, it is most likely suboptimal.
3. Have to rank agents with priority, causing the fairness issue, as some agents will always get treated in an unfair way relative to the other agents.
4. Picking the priority itself is a problem, for example, you could always assign static priorities to agents, however, this is very inflexible. You could also dynamically assign priority, which complicates the algorithm and could lead to deadlocks, etc.
