from model_review import model


predications = model.predict_proba({
    "train": "delayed"
})

for node, predications in zip(model.states, predications):
    if isinstance(predications, str):
        print(f"{node.name}: {predications}")

    else:
        print(f"{node.name}")
        for value, probability in predications.parameters[0].items():
            print(f"    {value}: {probability: 4f}")

