# from smac.env import StarCraft2Env
from nash_envs import NashStarCraft2Env
import numpy as np


def main():
    env = NashStarCraft2Env(map_name="nash_3m")
    env_info = env.get_env_info()
    print(env_info)

    n_actions = env_info["n_actions"]
    n_agents = env_info["n_agents"]

    n_episodes = 100

    # env.reset()

    for e in range(n_episodes):
        env.reset()
        terminated = False
        episode_reward = 0

        while not terminated:
            obs = env.get_obs()
            state = env.get_state()

            actions = []
            for agent_id in range(n_agents):
                avail_actions = env.get_avail_agent_actions(agent_id)
                avail_actions_ind = np.nonzero(avail_actions)[0]
                action = np.random.choice(avail_actions_ind)
                actions.append(action)

            reward, terminated, _ = env.step(actions)
            episode_reward += reward
            env.render()

        print("Total reward in episode {} = {}".format(e, episode_reward))

    env.close()


if __name__ == '__main__':
    main()
