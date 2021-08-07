from pomegranate import *

start = DiscreteDistribution({
    "sun": 0.5,
    "rain": 0.5
})

transition = ConditionalProbabilityTable([
    ["sun", "sun", 0.8],
    ["sun", "rain", 0.2],
    ["rain", "sun", 0.3],
    ["rain", "rain", 0.7]
], [start])

model = MarkovChain([start, transition])

print(model.sample(50))