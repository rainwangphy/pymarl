from functools import partial
from smac.env import MultiAgentEnv
from nash_envs.nash_starcraft2 import NashStarCraft2Env
import sys
import os


def env_fn(env, **kwargs) -> MultiAgentEnv:
    return env(**kwargs)


REGISTRY = {"sc2": partial(env_fn, env=NashStarCraft2Env)}

if sys.platform == "linux":
    os.environ.setdefault("SC2PATH",
                          os.path.join(os.getcwd(), "3rdparty", "StarCraftII"))