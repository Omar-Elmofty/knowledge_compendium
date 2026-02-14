from typing import Callable, List, Tuple, Dict, Any
import numpy as np
from numpy.typing import NDArray
import gymnasium as gym


State = NDArray[np.float64]


def train_mountain_car(
    env: gym.Env[NDArray[np.float64], int],
    choose_action: Callable[[State, float], int],
    Q_values: Callable[[State], NDArray[np.float64]],
    update_w: Callable[[float, State, int], None],
    gamma: float,
    epsilon: float,
    epsilon_decay: float,
    epsilon_min: float,
    num_episodes: int,
    verbose: bool = False,
) -> List[float]:
    reward_history: List[float] = []

    for episode in range(num_episodes):
        state_raw, info = env.reset()
        state = np.asarray(state_raw, dtype=np.float64)
        done = False
        total_reward = 0.0

        while not done:
            action = choose_action(state, epsilon)

            next_state_raw, reward, terminated, truncated, info = env.step(action)
            next_state = np.asarray(next_state_raw, dtype=np.float64)

            done = bool(terminated or truncated)
            total_reward += float(reward)

            # Compute target
            if done:
                td_target = float(reward)
            else:
                q_vals_next = Q_values(next_state)
                td_target = float(reward) + gamma * float(np.max(q_vals_next))

            # TD error
            q_vals_state = Q_values(state)
            td_error = float(td_target - float(q_vals_state[action]))

            # Gradient update
            update_w(td_error, state, action)

            state = next_state

        # Epsilon decay
        epsilon = max(epsilon_min, epsilon * epsilon_decay)

        reward_history.append(total_reward)

        if verbose:
            print(f"Episode {episode}, Reward: {total_reward}, Epsilon: {epsilon:.3f}")

    return reward_history


def render_mountain_car_policy(Q_values, video_name):

    frames = []

    render_env = gym.make("MountainCar-v0", render_mode="rgb_array")

    state, info = render_env.reset()
    done = False

    def select_action(state):
        return np.argmax(Q_values(state))

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
