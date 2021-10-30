from parlai.core.opt import Opt
from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent
from parlai.core.worlds import create_task
from parlai.core.script import ParlaiScript, register_script
from parlai.utils.world_logging import WorldLogger
from parlai.agents.local_human.local_human import LocalHumanAgent
import parlai.utils.logging as logging

import random
opt = Opt.load("model.opt")
agent = create_agent(opt, requireModelExists=True)
agent.opt.log()
human_agent = LocalHumanAgent(opt)
# set up world logger
world_logger = WorldLogger(opt) if opt.get('outfile') else None
world = create_task(opt, [human_agent, agent])
