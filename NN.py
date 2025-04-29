
net = [[[[-1, 0], 1, 1], [[1, 0], 0, 1]], [[[0, -1], 1, 2]]]

x = [0, 1]

dataset = [[[0, 0], [0]], [[1, 1], [0]], [[1, 0], [1]], [[0, 1], [1]]]

e = 2.718281828459045

def avrage_loss(net, dataset):
    i = 0
    x = []
    actual_value = []
    predicted_values = []
    mse = 0
    average_loss = 0
    while i < len(dataset):
        x = dataset[i][0]
        actual_value = dataset[i][1]
        predicted_values = forward_pass(x, net)
        mse += MSE(actual_value, predicted_values)
        i +=1
    average_loss = mse / len(dataset)
    return average_loss
    
def MSE(actual_values, predicted_values):
    mse_total = 0
    i = 0
    while i < len(predicted_values):
        predicted_value = float(predicted_values[i])
        actual_value = float(actual_values[i])

        error = predicted_value - actual_value
        mse_total += error ** 2
        i += 1
    mse = mse_total / len(predicted_values)
    return mse

def ReLU(x):
    if x <= 0:
        return 0
    else:
        return x

def Sigmoid(x):
    return 1/(1+e ** -x)

    if k_j == 0:
        return prediction - actual * compute_delta(prediction, a)

def forward_pass(net_input, net):
    l_z = []
    final_output = []
    Net_depth = 0
    Layer = []
    neuron = []
    activator = 0
    bias = 0
    output = []
    layer_input = net_input
    weights = []
    t = 0
    i = 0
    i1 = 0
    i2 = 0
    Net_depth = len(net)

    while i < Net_depth:
        output = []
        L_z = []
        Layer = net[i]
        i1 = 0
        L_z.append(l_z)
        L_z.clear
        while i1 < len(Layer):
            neuron = Layer[i1]
            activator = neuron[2]
            weights = neuron[0]
            bias = neuron[1]
            t = 0
            i2 = 0
            f_z = 0
            while i2 < len(weights):

                t += weights[i2] * layer_input[i2]
                i2 +=1

            t += bias
            l_z.append(t)

            if activator == 1:
                output.append(ReLU(t))

            elif activator == 2:
                output.append(Sigmoid(t))
            i1 +=1 

        layer_input = output
        i += 1

    print(L_z)
    final_output = output
    return final_output
            

# print(avrage_loss(net, dataset))

print(forward_pass(x, net))

