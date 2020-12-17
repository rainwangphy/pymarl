"""
Not used. With Errors
"""

from nash_envs.nash_smac_maps import get_smac_map_registry


def get_map_params(map_name):
    map_param_registry = get_smac_map_registry()
    return map_param_registry[map_name]
