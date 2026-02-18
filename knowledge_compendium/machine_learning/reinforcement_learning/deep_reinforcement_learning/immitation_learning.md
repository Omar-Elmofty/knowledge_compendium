# Imitation Learning

Notes from the [Deep Reinforcement Learning Course](https://www.youtube.com/watch?v=WxRDyObrm_M&list=PLoROMvodv4rPwxE0ONYRa_itZFdaKCylL&index=2), lecture slides can be found [here](https://cs224r.stanford.edu/slides/02_cs224r_imitation_2025.pdf).


## Key learning goals
- How to represent distributions with neural networks
- Why expressive distributions matter for imitation learning
- What are compounding errors, and how can we address them


## Goal of Imitation Learning

**Data**: Given trajectories collected by expert "demonstrations" $D := \{(s_1, a_1, ..., s_T)\}$ sampled from some unknown policy $\pi_{expert}$

**Goal**: Learn a policy $\pi_\theta$ that performs at the level of the expert policy, by mimicking it.

## Version 0 - Learning deterministic policy

If the policy is deterministic, we can simply learn it by supervised regression:

$$
\min_\theta \frac{1}{|D|} \sum_{(s, a) \in D} ||a - \pi_\theta(s)||^2 
$$

This is vanilla supervised learning approach.

This quickly breaks down if the underlying policy we're trying to learn is stochastic. What this is going to learn is average of the expert distribution, which is not ideal. Ideally, we'd want to learn the full expressive distribution.

There is a good example in the lecture that shows that with driving decisions, please check that.

## Version 1 - Learning stochastic policy

Instead of directly learning and having the neural network output what the action should be, instead we make the neural network output distribution hyper parameters.

For example, the neural network can output the mean and standard deviation of a normal distribution. This distribution can then be sampled to get the action.


Different distributions that can be learned:
- For discrete actions, this reduces to the categorical classification problem, which produces a probability for each action. This approach is maximally expressive which is great (can model any distribution).
- For distributions of actions in continuous space, these are some of the following possibilities:
   1. Gaussian mixture models
   2. Discrete - Auto-regressive model
   3. Diffusion model

## Traits of Imitation Learning

- Algorithm is fully offline:   
  1. offline: using only existing dataset, no new data from learned policy.
  2. online: using new data from learned policy.
- Since the algorithm is fully offline, there is no need for data after deploying the policy (online data can be unsafe, expensive to collect).
- no need to define a reward function
- However, may need a lot of data to achieve reliable performance

## What can go wrong with Imitation Learning

### Compounding errors

When you perform imitation learning, you're doing supervised learning to the dataset collected by the expert. However, when deploying your learnt policy, if the policy drifts from the dataset it was taught on, it could produce higher errors, and higher errors can lead the policy to diverge more the from the dataset, leading to errors compounding which is bad.

Here is a diagram illustrating the issue of compounding errors:

![compounding errors](../../../diagrams/exported/imitation_learning_compounding_errors.png)


Potential solutions:
1. Collect A LOT of demo data and hope for the best! Very expensive
2. Collect corrective behavior data, this is better, so let's explore this solution a bit

Addressing compounding errors with corrective behavior data:
1. Roll out a learned policy
2. Query the expert action at visited states by the learnt policy $a^* \leftarrow \pi_{expert}(s') $
3. Aggregate corrections with existing data $D \leftarrow D \cup \{(s', a^*)\}$
4. Update the policy with the new dataset

> This approach is called "dataset aggregation" (DAgger)

This approach is a data-efficient way to learn from the expert, the problem is that it can be challenging to query the expert when the agent has control.

Another approach is called "human gated DAgger" where the expert takes full control of the agent:
1. Start rolling out the policy
2. Expert intervenes at time t when the policy makes a mistake
3. Expert provides (partial) demonstrations $s_t, a_t^*, ..., s_T'$
4. Aggregate the new demos with existing data
5. Update the policy

This provide a much more practical interface for providing corrections. The problem is that it can be hard to catch mistakes quickly in some application domains.








