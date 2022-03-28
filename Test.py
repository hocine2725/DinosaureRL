import gym
import gym_Dino
import numpy as np
import random 


env = gym.make('Dino-v0')

state=env.reset()




while True:
    
    action = env.action_space.sample()
    [state,reward,done,info]=env.step(action)
    print(state)
    if done:
        env.reset()
    env.render()