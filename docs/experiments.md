# Modeling

## Implementation of Random

The first task of this project was to implement the simulation itself and establish a baseline for what happens in an uncontrolled simulation. It was also necessary to gain insight into what happens during a simulation run.

So in the first notebook in the series, a random algorithm is used to establish a baseline for what happens when no intelligent routing of candy happens.

Much as we would expect, all the Wuzzles die. This is because the same Wuzzle cannot lick the same candy more than once, and there are never new candy introduced, so eventually all the Wuzzles starve to death.
![](images/random_wuzzle_population_over_time.png)

I use the term "**Wuzzlpocalypse**" to represent the day that the last Wuzzle dies of starvation. In each simulation, the day is recorded and you can see a distribution of how long that takes in the graph below.

![](images/random_distribution_final_days.png)

Next we can see the total number of licks that happen in each simulation as well as the mean of them. You can see that early on the number climbs quickly and as the candy supply diminishes, the number levels off and everyone dies.

![](images/random_total_licks.png)

Last, we look at licks per day. It is similar to the last graph, but focused on each day rather than a grand total for the simulation.

![](images/random_nightly_licks.png)


## Incremental Learning

Before building the reinforcement learning piece, it made sense to also implement an incrementally trained model to give me a chance to flesh out things like model persistence and further develop the simulation.

Incremental learning has a lot in common with the idea of reinforcement learning, so it made sense to go after those parts first. In order to accomplish this easily, I employed a python library called River.

**River**: River is a Python library for online machine learning. It is the result of a merger between creme and scikit-multiflow. River's ambition is to be the go-to library for doing machine learning on streaming data.

The first model I chose was a **Decision Tree** simply because of:

- Ease of implementation.
- Support for incremental training.

The way it works is via the check_menu() method in the Wuzzle class. Basically when a wuzzle looks at a candy on the menu, he decides wether to lick it or not. I attached this action to the train_one() method of the model and then persist the model to disk. 

Here is the breakdown of the first training:

![](images/dt.png)

### My hypothesis for this part of the project is that this model will actually be good at feeding the best candy to wuzzles. Unfortunately I think this will lead to initial gluttony followed by a faster starvation cycle and an EARLIER Wuzzlpocalypse... which is very bad for the Wuzzles.


## Let's find out:

It looks like, **yes**, the date for Wuzzlpocalypse is significantly moved up when we use the Decision Tree model. It looks like our tree is reasonably good at feeding wuzzles and letting the gluttonous little buggerslickthemselves to death.

![](images/random_nightly_licks.png)
![](images/dt_nightly_licks.png)

## Before moving on, I wanted to add one more model. Bernoulli Naive Bayes. 

Let's see how it did... as you can see, the base model also does better than Random, but not quite as well as the Decision Tree. Mostly the reason I wanted to test this model is that it was a model not native to River, instead coming from scikit learn.

![](images/bnb_nightly_licks.png)


### Accuracy

Another thing we can look at is accuracy over time for each simulation.

Because of the non-deterministic nature of the random model and the structure of the code, Random starts at an artificially high accuracy rating. However over time, you can see it trend down towards an expected 50/50 accuracy. 

On the other hand the **tree** model quickly trains to an improved accuracy after a few nights and stays in that range. It is worth noting that it gets trained with every wuzzle looking at candy, so even by the end of the first night, it has had **(Number of Wuzzles x Number of Simulations)** of data points to train on. 



![](images/random_machine_accuracy.png)
![](images/dt_machine_accuracy.png)
![](images/bnb_machine_accuracy.png)
