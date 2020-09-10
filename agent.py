#!/usr/bin/env python3

import random
import retro

import numpy as np

from os import path

def main():
    game    = 'PunchOut-Nes'
    state   = 'MikeTyson.state'
    actions = retro.Actions.DISCRETE
    record  = True

    env = retro.make(game=game, state=state, use_restricted_actions=actions, record=record)
    obs = env.reset()

    epsilon       = 1.0
    epsilon_min   = 0.005
    epsilon_decay = 0.99993
    alpha         = 0.65
    gamma         = 0.65

    max_steps = 999999
    episode   = 0
    step      = 0

    if path.exists('qtable.npy'):
        print('loading existing q-table')
        q = np.load('qtable.npy')
    else:
        print('creating new q-table')
        q = np.zeros((max_steps, env.action_space.n))

    while step < max_steps:
        if random.uniform(0, 1) > epsilon:
            action = np.argmax(q[step, :])
        else:
            action = env.action_space.sample()

        obs, rew, done, info = env.step(action)

        q[step, action] = \
            (1 - alpha) * q[step, action] + alpha * (rew + gamma * np.max(q[step + 1, :]))

        env.render()

        if done:
            print("episode: ", episode, " | epsilon: ", epsilon, " | reward: ", rew, ' | steps: ', step)

            with open('qtable.npy', 'wb') as f:
                np.save(f, q)

            if epsilon >= epsilon_min:
                epsilon *= epsilon_decay

            episode += 1
            step     = 0
            obs      = env.reset()

        step += 1

    env.close()

if __name__ == '__main__':
    main()
