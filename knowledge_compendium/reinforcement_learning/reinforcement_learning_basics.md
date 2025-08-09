# Reinforcement learning basics

Notes for the following lecture:

- [Lecture Video](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-)
- [Lecture Slides](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/intro_rl.pdf)



## What is reinforcement learning?
It is the process by which an agent learns to maximize reward in a given environment.
Reinforcement learning deals with problems that involves sequential decisions by an agent, where after every decision taken the agent gets a specific reward.

## How is reinforcement learning different than other types of learning?
- Unlike supervised learning, there is no supervisor in reinforcement, the agent only gets a reward signal that just indicates how well the agent did in a particular setting. No supervisor tells the agent how to maximize reward (unlike supervised learning). If there is a supervisor gives the agent an example of optimal trajectories and the agent uses those to learn, then that's called imitation learning.
- The assumption that each data sample is independently and identically distributed or i.i.d (the assumption we make in supervised and unsupervised learning), this assumption doesn't hold in reinforcement learning, because different data samples may be conditioned on each other for example. Time matters in RL problems (sequential decision making), and the agent's action affects subsequent data it receives (hence why we can't have i.i.d assumption)
- Also in reinforcement, the feedback is often delayed, i.e. when taking a specific action, you may not necessarily know the consequences of taking such action until later on (when the RL episode is done)


## Components of Reinforcement Learning

The agent environment interaction:

<div align="center">
    <img src="attachment:c47f4bf2-d460-44fa-9d7f-eb6e17869c3f.png" width="500"/>
</div>

### Reward 

The is a scalar signal that the agent receives in every time step. The agent's objective is to maximize cumulative rewards. The reward signal can describe any goal. For example for an investment portfolio, the objective may be to maximize the total return while minimizing risk. You can then create a scalar value that balances between return and risk.

### State

The state is all the information needed to determine what happens next. It is what the agent uses to make the next decision. If the state is fully observed (like in an MDP), then:

$$
O_t = S_t^e = S_t^a
$$

Where the observations of the agent $O_t$ are equal to the state of the entire environment $S_t^e$ which is equal to the state the agent stores inside of it $S_t^a$ and is used to make the next decision.

If the environment is not fully observable (i.e. $O_t \neq S_t^e$), hence the agent will have to construct a belief of what the enviroment state is (which is $S_t^a$). That state could be either of:

1. The complete history $S_t^a = H_t$, where the history is $H_t = O_1, R_1, A_1, ...,A_{t-1}, O_t, R_t$
2. Beliefs of the environment state: $S_t^a = (P[S_t^e=s^1], ..., P[S_t^e = s^n])$
3. other forms of representing beliefs of the environment state $S_t^a = f(H_t)$

**Markov State**:

An information state (aka a Markov state) contains all useful information from the history

A state is Markov if:
$$
P[S_{t+1}|S_t] = P[S_{t+1}|S_1, ..., S_t]
$$

This means that the current state $S_t$ is a sufficient descriptor of the entire history, or in other words: The future is independent of the past given the present. Once the current state is known, the whole history can be thrown away.


See the below equation, the entire past leads to the current state, and the entire future stems from the current state. The future doesn't depend on the past given the present state.
$$
H_{1:t} \rightarrow S_t \rightarrow H_{t+1:\infty}
$$


**Markov Decision Process**: The environment is fully observable, and the state is markov.

**Partially observable Markov decision process (POMDP)**: The environment is partially observable, and the agent state is markov.



### Policy

The policy is a mapping between the agent's state and action. The policy can be defined as:

$$
a = \pi(s)
$$

The policy could also be stochastic:

$$
P[A_t = a | S_t = s] = \pi(a|s)
$$


### Value Function

The total future cumulative rewards at any given state, following a given policy (or transition dynamics).
The value function determines the goodness or badness (or value) of being at a specific state. It can be represented as:

$$
v_{\pi}(s) = E_{\pi}[R_{t+1} + \gamma R_{t+2} + \gamma R_{t+3} + ... | S_t = s]
$$

### Model

The agent's representation of how the environment works. A model can be used for prediction (predicting what the environment will do next), or planning (planning a trajectory in the environment knowing how the environment works). The model predicts the next state, and the next reward.

The model is optional, i.e. we don't have to have a model to solve the reinforcement learning problem. 
There are model-free approaches to RL, where we learn from experience (let the agent do things in the environment, then map out good action at a given state just from what the agent has experienced at that given state).

Here is the formalization of the model:

$$
P_{ss'}^a = P[S_{t+1} = s'| S_t = s, A_t = a]
$$
$$
R_s^a = E[R_{t+1} | S_t = s, A_t = a]
$$



## Types of Reinforcement Learning

### Model Free

The model of the environment is unknown. We only have access to the policy and the value function.
Can't do planning (can't plan out a trajectory in the environment). The agent can only act at a given state and has to wait for the environment state to propagate before it can see the reward of the action it has taken.

This is the pure reinforcement learning problem, similar to how humans and animals learn.

It is like trial and error learning.

### Model-based

Can have a model of the environment, which can be used for predicting what the environment will do next. This model can be used for planning, i.e. planning ahead a sequence of actions followed by predictions on what the environment will do next.


### Prediction vs. control

Prediction involves evaluating a policy into the future. Just purely unrolling the policy actions into the future and see how it behaves and what rewards we get.

Control is optimizing the policy for the future, i.e. finding the optimal policy.


