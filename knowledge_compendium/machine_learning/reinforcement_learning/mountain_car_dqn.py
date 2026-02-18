import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random
import torch
from torch import nn
import torch.nn.functional as F
import imageio.v3 as iio

# Define model
class DQN(nn.Module):
    def __init__(self, in_states, h1_nodes, out_actions):
        super().__init__()

        # Define network layers
        self.fc1 = nn.Linear(in_states, h1_nodes)   # first fully connected layer
        self.out = nn.Linear(h1_nodes, out_actions) # ouptut layer w

    def forward(self, x):
        x = F.relu(self.fc1(x)) # Apply rectified linear unit (ReLU) activation
        x = self.out(x)         # Calculate output
        return x

# Define memory for Experience Replay
class ReplayMemory():
    def __init__(self, maxlen):
        self.memory = deque([], maxlen=maxlen)

    def append(self, transition):
        self.memory.append(transition)

    def sample(self, sample_size):
        return random.sample(self.memory, sample_size)

    def __len__(self):
        return len(self.memory)

# MountainCar Deep Q-Learning
class MountainCarDQL():

    def __init__(self, 
            # Hyperparameters (adjustable)
            learning_rate_a = 0.05,         # learning rate (alpha)
            discount_factor_g = 0.9,         # discount rate (gamma)    
            network_sync_rate = 50000,          # number of steps the agent takes before syncing the policy and target network
            replay_memory_size = 100000,       # size of replay memory
            mini_batch_size = 32,            # size of the training data set sampled from the replay memory
            num_divisions = 20,
            # Neural Network
            loss_fn = nn.MSELoss(),          # NN Loss function. MSE=Mean Squared Error can be swapped to something else.
            optimizer = None,                # NN Optimizer. Initialize later.
            h1_nodes=10,                     # Number of hidden nodes
        ):
        self.learning_rate_a = learning_rate_a
        self.discount_factor_g = discount_factor_g
        self.network_sync_rate = network_sync_rate
        self.replay_memory_size = replay_memory_size
        self.mini_batch_size = mini_batch_size
        self.num_divisions = num_divisions
        self.loss_fn = loss_fn
        self.optimizer = optimizer
        self.h1_nodes = h1_nodes
        

    # Train the environment
    def train(self, episodes, render=False):
        env = gym.make('MountainCar-v0', render_mode='human' if render else None)
        # Create FrozenLake instance
        num_states = env.observation_space.shape[0] # expecting 2: position & velocity
        num_actions = env.action_space.n
        
        self.pos_low = env.observation_space.low[0]
        self.vel_low = env.observation_space.low[1]
        self.pos_range = env.observation_space.high[0] - env.observation_space.low[0]
        self.vel_range = env.observation_space.high[1] - env.observation_space.low[1]
    
        epsilon = 1 # 1 = 100% random actions
        memory = ReplayMemory(self.replay_memory_size)

        # Create policy and target network. Number of nodes in the hidden layer can be adjusted.
        policy_dqn = DQN(in_states=num_states, h1_nodes=self.h1_nodes, out_actions=num_actions)
        target_dqn = DQN(in_states=num_states, h1_nodes=self.h1_nodes, out_actions=num_actions)

        # Make the target and policy networks the same (copy weights/biases from one network to the other)
        target_dqn.load_state_dict(policy_dqn.state_dict())
        
        # Policy network optimizer. "Adam" optimizer can be swapped to something else. 
        self.optimizer = torch.optim.Adam(policy_dqn.parameters(), lr=self.learning_rate_a)

        # List to keep track of rewards collected per episode. Initialize list to 0's.
        rewards_per_episode = []

        # List to keep track of epsilon decay
        epsilon_history = []

        # Track number of steps taken. Used for syncing policy => target network.
        step_count=0
        goal_reached=False
        best_rewards=-100000
            
        for i in range(episodes):
            state = env.reset()[0]  # Initialize to state 0
            terminated = False      # True when agent falls in hole or reached goal
            truncated = False      # True when agent falls in hole or reached goal

            rewards = 0

            # Agent navigates map until it falls into hole/reaches goal (terminated), or has taken 200 actions (truncated).
            while(not terminated and rewards > best_rewards):

                # Select action based on epsilon-greedy
                if random.random() < epsilon:
                    # select random action
                    action = env.action_space.sample() # actions: 0=left,1=idle,2=right
                else:
                    # select best action            
                    with torch.no_grad():
                        action = policy_dqn(self.state_to_dqn_input(state)).argmax().item()

                # Execute action
                new_state,reward,terminated,truncated,_ = env.step(action)

                # Accumulate reward
                rewards += reward

                # Save experience into memory
                memory.append((state, action, new_state, reward, terminated)) 

                # Move to the next state
                state = new_state

                # Increment step counter
                step_count+=1


            # Keep track of the rewards collected per episode.
            rewards_per_episode.append(rewards)
            
            # if terminated:
            epsilon = max(1 - i/episodes, 0)
            
            epsilon_history.append(epsilon)

            # Graph training progress
            if(i!=0 and i%1000==0):
                print(f'Episode {i} Epsilon {epsilon}')
                                        
                self.plot_progress(rewards_per_episode, epsilon_history)
            
            if rewards > best_rewards:
                best_rewards = rewards
                print(f'Best rewards so far: {best_rewards}')
                print(f'Episode {i} Epsilon {epsilon}')
                # Save policy
                torch.save(policy_dqn.state_dict(), f"mountaincar_dql.pt")
            

            # Decay epsilon
            
            # Check if enough experience has been collected
            if len(memory)>self.mini_batch_size and terminated:
                for i in range(100):
                    mini_batch = memory.sample(self.mini_batch_size)
                    self.optimize(mini_batch, policy_dqn, target_dqn)        

                # Copy policy network to target network after a certain number of steps
                if step_count > self.network_sync_rate:
                    print("Swapped networks")
                    target_dqn.load_state_dict(policy_dqn.state_dict())
                    step_count=0                    

        # Close environment
        env.close()
    def plot_progress(self, rewards_per_episode, epsilon_history):
        # Create new graph 
        plt.figure(1)

        # Plot average rewards (Y-axis) vs episodes (X-axis)
        # rewards_curve = np.zeros(len(rewards_per_episode))
        # for x in range(len(rewards_per_episode)):
            # rewards_curve[x] = np.min(rewards_per_episode[max(0, x-10):(x+1)])
        plt.subplot(121) # plot on a 1 row x 2 col grid, at cell 1
        # plt.plot(sum_rewards)
        plt.plot(rewards_per_episode)
        
        # Plot epsilon decay (Y-axis) vs episodes (X-axis)
        plt.subplot(122) # plot on a 1 row x 2 col grid, at cell 2
        plt.plot(epsilon_history)
        
        # Save plots
        plt.savefig('mountaincar_dql.png')
    # Optimize policy network
    def optimize(self, mini_batch, policy_dqn, target_dqn):

        current_q_list = []
        target_q_list = []

        for state, action, new_state, reward, terminated in mini_batch:

            if terminated: 
                # Agent receive reward of 0 for reaching goal.
                # When in a terminated state, target q value should be set to the reward.
                target = torch.FloatTensor([reward])
            else:
                # Calculate target q value 
                with torch.no_grad():
                    target = torch.FloatTensor(
                        reward + self.discount_factor_g * target_dqn(self.state_to_dqn_input(new_state)).max()
                    )

            # Get the current set of Q values
            current_q = policy_dqn(self.state_to_dqn_input(state))
            current_q_list.append(current_q)

            # Get the target set of Q values
            target_q = target_dqn(self.state_to_dqn_input(state)) 
            # Adjust the specific action to the target that was just calculated
            target_q[action] = target
            target_q_list.append(target_q)
                
        # Compute loss for the whole minibatch
        loss = self.loss_fn(torch.stack(current_q_list), torch.stack(target_q_list))

        # Optimize the model
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    '''
    Converts a state (position, velocity) to tensor representation.
    Example:
    Input = (0.3, -0.03)
    Return = tensor([16, 6])
    '''
    def state_to_dqn_input(self, state)->torch.Tensor:
        return torch.FloatTensor([(state[0] - self.pos_low) / self.pos_range, (state[1] - self.vel_low) / self.vel_range])
    
    # Run the environment with the learned policy
    def test(self, episodes, model_filepath, video_name):
        # Create FrozenLake instance
        env = gym.make('MountainCar-v0', render_mode='human')
        num_states = env.observation_space.shape[0]
        num_actions = env.action_space.n

        self.pos_low = env.observation_space.low[0]
        self.vel_low = env.observation_space.low[1]
        self.pos_range = env.observation_space.high[0] - env.observation_space.low[0]
        self.vel_range = env.observation_space.high[1] - env.observation_space.low[1]

        # Load learned policy
        policy_dqn = DQN(in_states=num_states, h1_nodes=self.h1_nodes, out_actions=num_actions) 
        policy_dqn.load_state_dict(torch.load(model_filepath))
        policy_dqn.eval()    # switch model to evaluation mode
        
        
        frames = []

        render_env = gym.make("MountainCar-v0", render_mode="rgb_array")

        state, info = render_env.reset()
        done = False

        def select_action(state):
            return policy_dqn(self.state_to_dqn_input(state)).argmax().item()

        while not done:
            # Greedy action using your linear policy (replace with your function)
            action = select_action(state)

            next_state, reward, terminated, truncated, info = render_env.step(action)
            done = terminated or truncated

            frame = render_env.render()   # RGB array frame
            frames.append(frame)

            state = next_state

        render_env.close()


        # Save frames to MP4 using imageio
        iio.imwrite(
            video_name,
            frames,
            fps=30,
            codec="libx264"
        )
