from math import sqrt
from random import randint
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import time

startTime = time.time()

class Neuron:
    def __init__(self, x=0, y=0, z=0):
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


def neuronStats(neuron):
    print(neuron)
    print(neuron.connections)
    print(len(neuron.connections))



numNeurons = 400
neurons = []
physicalLimit = 3
biologicalLimit = 2000
maxOriginDist = 4000
maxConnections = 100

def createNeurons():
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
                neurons.append( Neuron(x, y, z) )
                break
        

    # place them all in 3d space, a certain distance apart, not to far away
        # growth pattern
        # spherical pattern
        # cubical pattern


def creationConnections():
    for i in range(len(neurons)):
        counter = 0
        while len(neurons[i].connections) < maxConnections and counter < 1000:
            counter += 1
            randomNeuronID = randint(0, len(neurons)-1)
            randomNeuron = neurons[randomNeuronID]
            randomNeuronDist = sqrt( (neurons[i].x - randomNeuron.x)**2 + (neurons[i].y - randomNeuron.y)**2 + (neurons[i].z - randomNeuron.z)**2 )

            closeEnough = randomNeuronDist < biologicalLimit
            isntFullyConnected = len(randomNeuron.connections) < maxConnections
            notAlreadyConnected = randomNeuronID not in neurons[i].connections
            notTheSameNeuron = randomNeuronID != i

            print(closeEnough, isntFullyConnected, notAlreadyConnected, notTheSameNeuron)

            if closeEnough and isntFullyConnected and notAlreadyConnected and notTheSameNeuron:
                neurons[i].connections.append(randomNeuronID)
                randomNeuron.connections.append(i)


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



createNeurons()
creationConnections()
neuronStats(neurons[0])

print("Neural Density is {}".format(numNeurons / (maxOriginDist *2)**3))

print(" --- %s seconds --- " % (time.time() - startTime))

visualizeTheMind()