from pomegranate import *

# Create node for bayesian network.

# Rain node has no parents.
rain = Node(DiscreteDistribution({
    "none": 0.7,
    "light": 0.2,
    "heavy": 0.1
}), name="rain")


# Track maintenance node is conditional on rain.
maintenance = Node(ConditionalProbabilityTable([
    ["none", "yes", 0.4],
    ["none", "no", 0.6],
    ["light", "yes", 0.2],
    ["light", "no", 0.8],
    ["heavy", "yes", 0.1],
    ["heavy", "no", 0.9]
],[rain.distribution]), name="maintenance")

# Train node is conditional on rain and maintenance.
train = Node(ConditionalProbabilityTable([
    ["none", "yes", "on time", 0.8],
    ["none", "yes", "delayed", 0.2],
    ["none","no", "on time", 0.9],
    ["none","no", "delayed", 0.1],
    ["light","yes", "on time", 0.6],
    ["light","yes", "delayed", 0.4],
    ["light", "no", "on time", 0.7],
    ["light", "no", "delayed", 0.3],
    ["heavy", "yes", "on time", 0.4],
    ["heavy", "yes", "delayed", 0.6],
    ["heavy", "no", "on time", 0.5],
    ["heavy", "no", "delayed", 0.5],
],[rain.distribution, maintenance.distribution]), name="train")

# Appointment node is conditional on Train
appointment = Node(ConditionalProbabilityTable([
    ["on time", "attend", 0.9],
    ["on time", "miss", 0.1],
    ["delayed", "attend", 0.6],
    ["delayed", "miss", 0.4],
], [train.distribution]), name="appointment")

# Create a Bayesian Network and add states.
model = BayesianNetwork()
# API Reference / add_states() (can take variable arguments / add_state() is take one argument).
# Another name for node.
model.add_states(rain, maintenance, train, appointment)

# Add edges connecting nodes
# API Reference / add_edge()
# Add a transition from state a to state b which indicates tha B is dependent on A in ways specified by the distribution.
model.add_edge(rain, maintenance)
model.add_edge(rain, train)
model.add_edge(maintenance, train)
model.add_edge(train, appointment)

# finalize model
# API Reference / bake()
# Finalize the topology of the model.
# Assign a numerical index to every state and create the underlying arrays corresponding to the states nad edges between the states.
# This method must be called before any of the probability-calculating methods. This includes converting coditioal probability tables into joint probability tables and creating a list of both marginal and table node.

model.bake()
