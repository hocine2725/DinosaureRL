from pickle import FALSE
import gym

from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

from utility import *


class DinoEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        menu()
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.MultiDiscrete([ 1001, 3,2 ])
        self.reward=0
        
    def step(self, action):
        player.update(action)
        done=player.done
        self.state=[player.distance,player.arbre,player.type]
        reward=player.rew
        info={}
        return self.state,reward,done,info

    def reset(self):
        
        menu()
        player.done=False
        player.points=0
        player.rew=0.1
        self.state=[player.distance,player.arbre,player.type]

        return self.state
    
    def render(self, mode='human'):
        dessiner()
      
   