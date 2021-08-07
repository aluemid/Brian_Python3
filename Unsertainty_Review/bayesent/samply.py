import pomegranate

from collections import Counter

from model_review import model

def generate_sample():

    sample = {}

    parents = {}

    for state in model.states:
        if isinstance(state.distribution, pomegranate.ConditionalProbabilityTable):
            sample[state.name] = state.distribution.sample(parent_values=parents)

        else:
            sample[state.name] = state.distribution.sample()

        parents[state.name] = sample[state.name]

    return sample

N = 10000
data = []
for i in range(N):
    sample = generate_sample()
    if sample["train"] == "delayed":
        data.append(sample["appointment"])

print(Counter(data))