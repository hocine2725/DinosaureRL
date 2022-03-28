import gym
import gym_Dino
from stable_baselines3 import PPO    
import random 

#tensorboard --logdir ./PPO/

env = gym.make('Dino-v0')

print(env.action_space.n)

## pour rentrainer le modèle, il faut enlever le commentaire des 3 lignes suivantes
#model = PPO("MlpPolicy", env, verbose=1,tensorboard_log="./PPO/",device='cuda',learning_rate=0.0001)
#model.learn(total_timesteps=250_000)
#model.save("dino")

model = PPO.load("dino") 

obs = env.reset()

for i in range(10000):
    
    action, _state = model.predict(obs,deterministic=True )
    
    obs, reward, done, info = env.step(action)
    env.render()
    if done: 
        env.reset()
    


