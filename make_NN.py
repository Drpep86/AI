#net = [[[[-1, 0], 1, 1], [[1, 0], 0, 1]], [[[0, -1], 1, 2]]]
import random
def_net = [[2, [1, 1]], [1, [2]]]
x = [1, 2]

def gen_weights(x):
    i = 0
    y = 0
    weights = []
    while i < x:
        y = random.randint(-1, 1)
        weights.append(y)
        i +=1
    return weights

def gen_neuron(activator, num_weights):
    bias = random.randint(-1, 1)
    weights = gen_weights(num_weights)
    return [weights, bias, activator]

def make_net(def_net, inputs):
    i = 0
    i2 = 0
    num_weights = len(inputs)
    activator = 0
    bias = 0
    activators = []
    network = []
    layer = []
    neuron = []
    weights = []

    while i < len(def_net):
        neurons = def_net[i][0]
        activators = def_net[i][1]
        i2 = 0
        while i2 < neurons:
            activator = activators[i2]
            neuron = gen_neuron(activator, num_weights)
            layer.append(neuron)
            i2 += 1

        network.append(layer)
        num_weights = len(layer)
        layer = []
        i += 1
    return network


print(make_net(def_net, x))
        
