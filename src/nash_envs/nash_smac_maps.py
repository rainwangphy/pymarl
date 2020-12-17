"""
Not used. With Errors
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pysc2.maps import lib


class SMACMap(lib.Map):
    directory = "SMAC_Maps"
    download = "https://github.com/oxwhirl/smac#smac-maps"
    players = 2
    step_mul = 8
    game_steps_per_episode = 0


map_param_registry = {

    "nash_3m": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 60,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
    },
}


def get_smac_map_registry():
    return map_param_registry


for name in map_param_registry.keys():
    globals()[name] = type(name, (SMACMap,), dict(filename=name))


def get_map_params(map_name):
    map_param_registry = get_smac_map_registry()
    return map_param_registry[map_name]
