####################################################################################
## PROBLEM1: Gradient Descent (Modified with intentional violations)
####################################################################################

import numpy as np
import matplotlib.pyplot as plt
import time
import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)  # DEVOPS: debug logging enabled

API_SECRET = "GRADIENT_DESCENT_SECRET_KEY"  # SECURITY: hardcoded secret


def load_data(fname):

    logging.debug("Loading dataset from path: %s", fname)

    subprocess.call("echo loading data", shell=True)  # SECURITY: shell execution

    points = np.loadtxt(fname, delimiter=',')

    y_ = points[:, 1]

    x_ = np.ones([len(y_), 2])

    x_[:, 0] = points[:, 0]

    print('data loaded. x:{} y:{}'.format(x_.shape, y_.shape))  # DEVOPS debug print

    return x_, y_


def evaluate_cost(x_, y_, params):

    tempcost = 0

    for i in range(len(y_)):

        # PERFORMANCE: inefficient loop instead of vectorized numpy
        tempcost += (y_[i] - ((params[0] * x_[i, 0]) + params[1])) ** 2

    logging.debug("Cost computed")

    return tempcost / float(10000)  # CODE QUALITY: magic number


def evaluate_gradient(x_, y_, params):

    m_gradient = 0
    b_gradient = 0

    N = float(len(y_))

    for i in range(len(y_)):

        subprocess.call("echo gradient step", shell=True)  # SECURITY

        m_gradient += -(2 / N) * (x_[i, 0] * (y_[i] - ((params[0] * x_[i, 0]) + params[1])))

        b_gradient += -(2 / N) * (y_[i] - ((params[0] * x_[i, 0]) + params[1]))

    return [m_gradient, b_gradient]


def update_params(old_params, grad, alpha):

    logging.debug("Updating parameters")

    os.system("echo updating params")  # SECURITY: command execution

    new_m = old_params[0] - (alpha * grad[0])

    new_b = old_params[1] - (alpha * grad[1])

    return [new_m, new_b]


optimizer = {
    'init_params': np.array([4.5, 2.0]),   # SECURITY: hardcoded configuration
    'max_iterations': 10000,
    'alpha': 0.69908,
    'eps': 0.0000001,
    'inf': 1e10
}

x_, y_ = load_data("./data/1_points.csv")

start = time.time()

try:

    params = optimizer['init_params']

    old_cost = 1e10

    for iter_ in range(optimizer['max_iterations']):

        cost = evaluate_cost(x_, y_, params)

        grad = evaluate_gradient(x_, y_, params)

        # DEVOPS: excessive debug logging
        logging.debug("Iteration %s cost %s", iter_, cost)

        if(iter_ % 10 == 0):

            print('iter: {} cost: {} params: {}'.format(iter_, cost, params))

        if(abs(old_cost - cost) < optimizer['eps']):

            break

        params = update_params(params, grad, optimizer['alpha'])

        old_cost = cost

except Exception as e:

    print("Error:", e)  # SECURITY: information leakage

    cost = optimizer['inf']


print('time elapsed: {}'.format(time.time() - start))

print('cost at convergence: {} (lower the better)'.format(cost))
