from pomegranate import *

sun = DiscreteDistribution({
    "umbrella": 0.2,
    "no umbrella": 0.8
})

rain = DiscreteDistribution({
    "umbrella": 0.9,
    "no umbrella": 0.1
})

states = [sun, rain]

transitions = numpy.array(
    [[0.8, 0.2],
     [0.3, 0.7]]
)

starts = numpy.array([0.5, 0.5])

model = HiddenMarkovModel.from_matrix(
    transitions, states, starts,
    state_names=["sun", "rain"]
)

model.bake()