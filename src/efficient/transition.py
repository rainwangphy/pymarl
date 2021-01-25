from torch import nn


class TransitionModel(nn.Module):

    def __init__(self, state_dim, num_agent, action_dim,
                 hidden_dim=64, act_fn='relu'):
        super().__init__()
        self.state_dim = state_dim
        self.num_agent = num_agent
        self.action_dim = action_dim

        self.hidden_dim = hidden_dim
        self.act_fn = act_fn
