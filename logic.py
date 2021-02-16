import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# import matplotlib.pyplot as plt

# input
time_dist = ctrl.Antecedent(np.arange(0, 2.05, 0.05), 'time_dist')
y_dist = ctrl.Antecedent(np.arange(-600, 601, 1), 'y_dist')
y_player = ctrl.Antecedent(np.arange(0, 601, 1), 'y_player')
# output
move = ctrl.Consequent(np.arange(-800, 810, 10), 'move')


time_dist['very small'] = fuzz.trimf(time_dist.universe, [0, 0, 0.1])
time_dist['small'] = fuzz.trimf(time_dist.universe, [0, 0.1, 0.3])
time_dist['medium'] = fuzz.trimf(time_dist.universe, [0.1, 0.3, 1])
time_dist['big'] = fuzz.trimf(time_dist.universe, [0.3, 2, 2])

y_dist['negative big'] = fuzz.trimf(y_dist.universe, [-600, -600, -80])
y_dist['negative small'] = fuzz.trimf(y_dist.universe, [-600, -80, 0])
y_dist['negative very small'] = fuzz.trimf(y_dist.universe, [-80, -1, 1])
y_dist['positive very small'] = fuzz.trimf(y_dist.universe, [-1, 1, 80])
y_dist['positive small'] = fuzz.trimf(y_dist.universe, [0, 80, 600])
y_dist['positive big'] = fuzz.trimf(y_dist.universe, [80, 600, 600])

y_player['top'] = fuzz.trimf(y_player.universe, [0, 0, 90])
y_player['middle'] = fuzz.trapmf(y_player.universe, [0, 90, 510, 600])
y_player['bottom'] = fuzz.trimf(y_player.universe, [510, 600, 600])


move['fast up'] = fuzz.trimf(move.universe, [-800, -800, -450])
move['slow up'] = fuzz.trimf(move.universe, [-800, -450, 0])
move['stay'] = fuzz.trimf(move.universe, [-450, 0, 450])
move['slow down'] = fuzz.trimf(move.universe, [0, 450, 800])
move['fast down'] = fuzz.trimf(move.universe, [450, 800, 800])

# def show_logic():
#     time_dist.view()
#     y_dist.view()
#     y_player.view()
#     move.view()
#     plt.show()
# show_logic()


rules = [
    ctrl.Rule(y_player['top'], move['fast down']),
    ctrl.Rule(y_player['bottom'], move['fast up']),

    ctrl.Rule(y_dist['negative big'] | y_dist['positive big'], move['stay']),
    #ctrl.Rule(y_dist['negative small'] | y_dist['positive small'], move['stay']),

    ctrl.Rule(y_dist['negative very small'] & time_dist['very small'], move['fast up']),
    ctrl.Rule(y_dist['positive very small'] & time_dist['very small'], move['fast down']),

    ctrl.Rule(y_dist['negative very small'] & time_dist['small'], move['slow up']),
    ctrl.Rule(y_dist['positive very small'] & time_dist['small'], move['slow down']),

    #ctrl.Rule(y_dist['negative very small'] & time_dist['medium'], move['stay']),
    #ctrl.Rule(y_dist['positive very small'] & time_dist['medium'], move['stay']),

    ctrl.Rule(y_dist['negative very small'] & time_dist['big'], move['stay']),
    ctrl.Rule(y_dist['positive very small'] & time_dist['big'], move['stay']),
]

move_ctrl = ctrl.ControlSystem(rules)
moving = ctrl.ControlSystemSimulation(move_ctrl)


# def show_logic_sim():
#     y_player.view(sim=moving)
#     time_dist.view(sim=moving)
#     y_dist.view(sim=moving)
#
#     move.view(sim=moving)
#
#     plt.show()

def logic_calc(time, dist_y, player_y):
    # dist_y can't be close to 0
    if dist_y > -0.01 and dist_y < 0.01:
        dist_y += 1

    moving.input['time_dist'] = time
    moving.input['y_dist'] = dist_y
    moving.input['y_player'] = player_y
    moving.compute()
    return moving.output['move']

