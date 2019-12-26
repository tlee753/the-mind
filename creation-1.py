from math import sqrt
from random import randint
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import time

startTime = time.time()

class Neuron:
    def __init__(self, id=0, x=0, y=0, z=0, purpose=0):
        self.id = id
        self.purpose = purpose # 0 for normal, 1 for input, 2 for output
        self.value = 1
        self.connections = []
        self.connectionsPlotted = []
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "[({}, {}, {}), {}]".format(self.x, self.y, self.z, self.value)

    def __repr__(self):
        return "[({}, {}, {}), {}]".format(self.x, self.y, self.z, self.value)

    def adjustValue(self):
        pass
        # use connected neurons plus random quantity to adjust current value



numNeurons = 4000
neurons = []
physicalLimit = 5 # microns
biologicalLimit = 1000
maxOriginDist = 2000
maxConnections = 200

def growTheMind():
    for i in range(numNeurons):
        # print("Neuron: ", i)

        while True:

            growable = True

            x = randint(-maxOriginDist, maxOriginDist)
            y = randint(-maxOriginDist, maxOriginDist)
            z = randint(-maxOriginDist, maxOriginDist)

            # if (sqrt(x**2 + y**2 + z**2) > maxOriginDist):
                # get new point
                # spherical pattern
            
            for neuron in neurons:
                if (sqrt( (x - neuron.x)**2 + (y - neuron.y)**2 + (z - neuron.z)**2 ) < physicalLimit):
                    growable = False
                    break
            
            if growable:
                neurons.append( Neuron(i, x, y, z) )
                break
        

    # place them all in 3d space, a certain distance apart, not to far away
        # growth pattern
        # spherical pattern
        # cubical pattern


def connectTheMind():
    for i in range(numNeurons):
        counter = 0
        neuron = neurons[i]
        while len(neuron.connections) < maxConnections and counter < 1000:
            counter += 1
            randomNeuronID = randint(0, numNeurons-1)
            randomNeuron = neurons[randomNeuronID]
            randomNeuronDist = sqrt( (neuron.x - randomNeuron.x)**2 + (neuron.y - randomNeuron.y)**2 + (neuron.z - randomNeuron.z)**2 )

            closeEnough = randomNeuronDist < biologicalLimit
            isntFullyConnected = len(randomNeuron.connections) < maxConnections
            notAlreadyConnected = randomNeuronID not in neuron.connections
            notTheSameNeuron = randomNeuronID != i

            # print(closeEnough, isntFullyConnected, notAlreadyConnected, notTheSameNeuron)

            if closeEnough and isntFullyConnected and notAlreadyConnected and notTheSameNeuron:
                neuron.connections.append(randomNeuronID)
                randomNeuron.connections.append(i)

def processTheMind():
    # process inputs in a thinking sense to result in an output
    pass

def thinkTheMind():
    # no inputs, simulated neuron firing to appropriate an outcome?
    pass

def sleepTheMind():
    # no inputs, reinforcing neurological constructs
        # based on what?
    pass

def visualizeTheMind():
    fig = plt.figure(figsize=(16,9))
    ax = plt.axes(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    x = []
    y = []
    z = []
    c = []
    s = []

    for neuron in neurons:
        x.append(neuron.x)
        y.append(neuron.y)
        z.append(neuron.z)
        c.append(neuron.value)

        for connection in neuron.connections:
            ax.plot3D([neuron.x, neurons[connection].x], [neuron.y, neurons[connection].y], [neuron.z, neurons[connection].z])

    ax.scatter3D(x, y, z, c=c, cmap='Spectral')

    plt.show()


# def importTheMind():
#     for neuron in neurons:
#         mindFile.write(str(nueron) + ",")
#         mindFile.write(nueron.connections):


# def exportTheMind():
#     for neuron in neurons:
#         mindFile.write(str(nueron) + ",")
#         mindFile.write(nueron.connections):

def statOnTheMind(neuron):
    print(neuron)
    print(neuron.connections)
    print("Connections: ", len(neuron.connections))
    print()

print("Creating Neurons\n")
growTheMind()

print("Creating Connections\n")
connectTheMind()

print("Single Neuron Stats")
statOnTheMind(neurons[0])

print("Global Neuron Stats")

sum = 0
for neuron in neurons:
    sum += len(neuron.connections)
print("Neurons: {}, Neuron Connections: {}".format(numNeurons, sum))

print("Neural Density is {}".format(numNeurons / (maxOriginDist *2)**3))

print(" --- %s seconds --- " % (time.time() - startTime))

# visualizeTheMind()