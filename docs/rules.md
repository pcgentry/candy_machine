# The CANDY Machine rules

[Document Home](./index.md)

Welcome to the CANDY machine, a reinforcement learning system to solve an economic relationship between wuzzles and CANDY. Although this was created in a whimsical environment, it could be useful in a number of scenarios such as adoption services, job matching, a recommendation system for perishable goods, or other similar scenarios. Wuzzles are just more fun and I'm off the clock.

## The Problem Set (Rules of the scenario)

The planet Wuzzlopolis has two big problems.

### Problem 1: The planet is full of hungry wuzzles.

Traditionally, the Kind King of Wuzzlopolis would feed each wuzzle by hand based on how much he liked each wuzzle and what he thought they would like. This approach wasn't ideal because the Kind King was only one wuzzle with only one perspective. He could never pay attention to every wuzzle and what they liked to lick, so he had to make a lot of generalizations. While he did the best he could, his choices were somewhat arbitrary. Still, Wuzzlopolis did alright under the Kind King.

Unfortunately, the Kind King has died suddenly and there is nobody to replace him. Obviously, we must build a machine to do his job. We also hope that our machine is better at feeding Wuzzles than the Kind King. If our machine is smart enough, it will be able to track wuzzle preferences individually and keep them fed for as long as possible before the food supply runs out.

### Problem 2: Wuzzlopolis is full of uneaten CANDY.

One interesting thing about CANDY on Wuzzlopolis is that it is alive. CANDY individuals also like to be licked. In fact, they need to be licked because when they aren't, they get very depressed and moody and don't enjoy life very much. They also die a horrible death after a few days. CANDY comes in many flavors, ranging from 'apple' to 'earwax', and a single CANDY can have multiple flavors (but not always).

Luckily, WUZZLES lick CANDY, but they are very picky about which flavors of candy they lick. Obviously, we must build a machine to distribute CANDY individuals to the wuzzles. If our machine is smart enough, it will track CANDY individuals and keep them alive as long as possible.

# Let's create a CANDY machine and feed wuzzles CANDY!

## Rules of the Wuzzlopolis environment:

- Every wuzzle has a set of flavors they can lick but can't lick other flavors, such as ['peach', 'tarball', 'toe fuzz'].
- If a wuzzle doesn't lick, it has a chance of SUDDEN DEATH. Every day unfed increases the chance of SUDDEN DEATH.
- If a CANDY individual isn't licked for a day, it has a chance of SUDDEN DEATH. Every day unlicked increases the chance of SUDDEN DEATH.
- Every wuzzle has their own CANDY cookbook with lists sorted by CANDY breed where CANDY individuals can be listed. Our machine will pick CANDY individuals based on what CANDY individuals are on each CANDY list.
- Every wuzzle owns a lunchbox that can have up to 20 CANDY. Our machine will load the lunchbox from the cookbook.
- When we say a wuzzle licks a candy, it actually just licks it and tosses it
