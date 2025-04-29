def derivative(x, a):
    if a == 1:
        if x > 0: Dr = 1
        else: Dr = 0
    elif a == 2:
        Sx = Sigmoid(x)
        Dr = Sx * (1 - Sx)
    return Dr

def Sigmoid(x):
    return 1/(1+e ** -x)

def d_of_output(a,direct_neron_output):
    dirivitive_of_output = derivative(direct_neron_output, a)
    d = dirivitive_of_output - direct_neron_output
    return d

def d_of_hidden(outgoing_weight, previus_d):
    d = outgoing_weight * previus_d

def find_deltas(n_a, direct_neron_outputs, outgoing_weights):
    i = 0
    i2 = 0
    n = []
    while i < len(n_a):
        i2 = 0
        a = n_a[i][1]
        n = n_a[i][0]
        if i == 0:
            while i2 < n:
                d = d_of_output(a, direct_neron_outputs)
                i2 += 1
        else:
            while i2 < n:
                d = d_of_hidden(outgoing_weights, D)
                i2 += 1
        D = d
        i += 1

find_deltas([1, 2], [2, 1], [1, 0])

#[[[[-1, 0], 1, 1], [[1, 0], 0, 1]], [[[0, -1], 1, 2]]]
        
