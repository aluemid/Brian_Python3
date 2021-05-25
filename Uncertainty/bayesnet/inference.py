from model import model

# Calculate predictions.
# predict_proba(X:dict ofr array-like, shape <= n_nodes)
#   return the probabilities of each variable in the graph given evidence.
#   This calculates the marginal probability distributions for each state given the evidence provided
#       through loopy belief propagation. Loopy belief propagation is an approximate algorithm
#       which is exact for certain graph structures.
#   The evidence supplied to the graph. This canc either be a dictionary with keys being state names and values being the observed values
#   (either the emissions or distribution over the emissions) or an array with the values being ordered according to thenodes incorporation in the graph
#   (the order fed into .add_states/add_nodes) and None foir variables which are unknown.
#   Return: y_hat:array-like, shape(n_samples, n_nodes) An array of univariate distribution objects showing the probability of each variable.

predictions = model.predict_proba({
    "train": "delayed"
})

# print predictions for each node
# Python's zip() function is defined as zip(*iterable). The function takes in iterables as arguments and
#   returns an iterator. This iterator generates a series of tuples containing elements from each iterable.
#   zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.
for node, prediction in zip(model.states, predictions):

    # isinstance(object, classinfo)
    # Return True if the ojbect argument is an instance of the classinfo argument, or of a(direct, indirect or virtual)
    #   subclass thereof. if ojbect is not an object of the given type, the function always return False.
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability: 4f}")