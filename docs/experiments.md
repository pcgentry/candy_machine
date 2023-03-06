# Modeling

[Document Home](./index.md)

## Implementation of Random

The first task of this project was to implement the simulation itself and establish a baseline for what happens in an uncontrolled simulation. It was also necessary to gain insight into what happens during a simulation run.

So in the first notebook in the series, a random algorithm is used to establish a baseline for what happens when no intelligent routing of candy happens.

### Simulation Results

- All the Wuzzles die eventually due to starvation because they cannot lick the same candy more than once, and no new candy is introduced.
- The day of the "Wuzzlpocalypse" (i.e., the last Wuzzle dies of starvation) is recorded in each simulation, and there is a distribution of how long that takes.
- The total number of licks that happen in each simulation, as well as the mean of them, is shown.
- The number of licks per day is shown.

## Incremental Learning

Before building the reinforcement learning piece, an incrementally trained model was implemented to give a chance to flesh out things like model persistence and further develop the simulation.

### River Library

River is a Python library for online machine learning. It is the result of a merger between creme and scikit-multiflow. River's ambition is to be the go-to library for doing machine learning on streaming data.

### Decision Tree Model

The first model used was a Decision Tree because of its ease of implementation and support for incremental training.

- The check_menu() method in the Wuzzle class is used to decide whether to lick a candy or not.
- This action is attached to the train_one() method of the model, and the model is persisted to disk.

### Hypothesis

The hypothesis for this part of the project is that this model will be good at feeding the best candy to Wuzzles. Unfortunately, it is expected to lead to initial gluttony followed by a faster starvation cycle and an earlier Wuzzlpocalypse.

### Simulation Results

- The Wuzzlpocalypse date is significantly moved up when the Decision Tree model is used.
- The tree model is reasonably good at feeding wuzzles and letting them lick themselves to death.

### Bernoulli Naive Bayes Model

Another model tested was Bernoulli Naive Bayes, which is not native to River but instead comes from scikit-learn.

### Simulation Results

- The base model does better than Random, but not quite as well as the Decision Tree.

### Accuracy

Another thing to look at is accuracy over time for each simulation.

- The Random model starts at an artificially high accuracy rating, but over time, it trends down towards an expected 50/50 accuracy.
- The Decision Tree model quickly trains to an improved accuracy after a few nights and stays in that range. It is worth noting that it gets trained with every wuzzle looking at candy, so even by the end of the first night, it has had (Number of Wuzzles x Number of Simulations) of data points to train on.
