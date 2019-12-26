from math import sqrt
from random import randint
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import time

startTime = time.time()

# ----- NUERON CLASS -----
class Neuron:
    def __init__(self, id=0, x=0, y=0, z=0, purpose=0):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.purpose = purpose # 0 for normal, 1 for input, 2 for output
        self.value = 0
        self.connections = []
        self.weights = []
        # self.connectionsPlotted = []


    def __str__(self):
        return "[({}, {}, {}), {}]".format(self.x, self.y, self.z, self.value)

    def __repr__(self):
        return "[({}, {}, {}), {}]".format(self.x, self.y, self.z, self.value)

    def adjustValue(self):
        pass
        # use connected neurons plus random quantity to adjust current value

class Creature:
    def __init__(self, id=0, x=0, y=0, smell=0, goalX=0, goalY=0):
        self.id = id
        self.x = x
        self.y = y
        self.smell = smell
        self.goalX = goalX
        self.goalY = goalY

    def __str__(self):
        return "x: {}, y: {}".format(self.x, self.y)

    def __repr__(self):
        return "x: {}, y: {}".format(self.x, self.y)

    def senseSmell(self):
        self.smell = sqrt( (self.goalX - self.x)**2 + (self.goalY - self.y)**2 )



# ----- GLOBAL VARIABLES -----
numNeurons = 400 # 86,000,000,000
maxConnections = 100 # 10,000
neurons = []

physicalLimit = 5 # microns
biologicalLimit = 1000 # microns
maxOriginDist = 2000 # microns


# ----- FUNCTION DEFINITIONS -----
def growTheMind(): # add neurons to a 3D mind space
    for i in range(numNeurons):
        # print("Neuron: ", i)

        while True:

            growable = True

            x = randint(0, maxOriginDist)
            y = randint(0, maxOriginDist)
            z = randint(0, maxOriginDist)

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
        

    # place them all in 3d space, a certain distance apart, not too far away
        # growth pattern (grow outward from one another)
        # spherical pattern
        # cubical pattern

def connectTheMind(): # add neural connections between neurons biologically
    for i in range(numNeurons):
        counter = 0 # finite limit on attempts to connect
        neuron = neurons[i]
        while len(neuron.connections) < maxConnections and counter < 10*maxConnections:
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
    creature = Creature(0, 0, 0, 0, 25, 80)
    creature.senseSmell()
    print("Smell:", creature.smell)

    while True:
        neurons[0].value = 5 - 5*(creature.smell/84) # smell neuron
        neurons[1].value = 5*(creature.X/100) # x neuron
        neurons[2].value = 5*(creature.Y/100) # y neuron
    
        # processing of all other neurons in random order
        for i in range(3, len(neurons)-1):
            neurons[i].adjustValue()

        # output neurons
        creature.x += neurons[-1].value*0.1
        creature.y -= neurons[-2].value*0.1

        # weight adjustment based on smell
        # weights *= smell difference (exponentiated) * scalefactor * randomnessFactor?
        smell = creature.smell
        smellDiff = creature.senseSmell - smell


    # # sustained while loop
    # while processing:
    #     // run through every nueron in random order all inclusive?
    #     // adjust value accordingly
    #         // weights
    #         // forward firing nature or else your are back? not really due to weights
        
    #     // dopamine
    #         // small dope hit based on fitness -> equivalent to human cooing baby for good progress
    #         // sense distance from goal

    #     // continously learn until goal is obtained?
    #         // simple task, baby stays focused with guidance until it is obtained

    #         // restart the task?
    #             // search for efficiency increases

def thinkTheMind():
    # no inputs, simulated neuron firing to appropriate an outcome?
        # using that output to obtain something
        # creating a stronger neural connections, making sense out of something
            # suffieciently complex to simulate a scenario and make a mental prediction? -> conscious
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

def globalStatTheMind():
    sum = 0
    for neuron in neurons:
        sum += len(neuron.connections)
    print("Neurons: {}".format(numNeurons))
    print("Neuron Connections: {}".format(sum))
    print("Neural Density: {}".format(numNeurons / (maxOriginDist *2)**3))


# ----- RUNNING FUNCTIONS -----
print("\nCreating Neurons")
growTheMind()
print(" --- %s seconds --- " % (time.time() - startTime))

print("\nCreating Connections")
connectTheMind()
print(" --- %s seconds --- " % (time.time() - startTime))

print("\nProcessing Input")
processTheMind()
print(" --- %s seconds --- " % (time.time() - startTime))

print("\nSingle Neuron Stats")
statOnTheMind(neurons[0])

print("\nGlobal Neuron Stats")
globalStatTheMind()

print(" --- %s seconds --- " % (time.time() - startTime))

# print("Visualize The Mind")
# visualizeTheMind()