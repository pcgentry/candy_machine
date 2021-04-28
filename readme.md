# The CANDY Machine
Welcome to the CANDY machine, a **reinforcement learning system** to solve an economic relationship between wuzzles and CANDY. I created a whimsical environment to develop the system, but this would be useful in a number of scenarios such as **adoption services, job matching, a recommendation system for perishable goods**, ***or other similar scenarios***. Wuzzles are just more fun and I'm off the clock.

# The Problem Set

The planet Wuzzlopolis has **two** **big** **problems**.

## Problem 1: The planet is full of hungry wuzzles. 

Traditionally the **Kind King** of Wuzzlopolis would feed each wuzzle by hand based on how much he liked each wuzzle and what the Kind King thought they would like. 

This approach wasn't the best, because the Kind King was only one Wuzzle and had only one perspective. One wuzzle can only do so much, and he could never pay attention to every wuzzle and what they liked to eat... he had to make a lot of generalizations and while doing the best he could, his choices were somewhat arbitrary.

Still, Wuzzlopolis did O.K. under the Kind King.

Unfortunately, **THE Kind King HAS DIED SUDDENLY** and there is nobody to replace them. 

Obviously we must build a machine to do his job.

We also kinda low-key hope that our machine is better at feeding Wuzzles than the Kind King. If our machine is smart enough, it will be able to track wuzzle preferences individually and keep them fed for as long as possible before the food supply runs out.

## Problem 2: Wuzzlopolis is full of uneaten CANDY.

One interesting thing about CANDY on Wuzzlopolis is that it is alive. 

CANDY individuals also like to be eaten. In fact they need to be eaten because when they aren't, CANDY gets very **depressed and moody** and doesn't enjoy life very much. It also **dies a horrible death** after a few days.

CANDY comes in many flavors, ranging from **[ 'apple' : 'earwax' ]** and a single CANDY can have multiple flavors (but not always).

Luckily **WUZZLES EAT CANDY**, but are very picky about which flavors of candy they eat.

Obviously we must build a machine to distribute CANDY individuals to the wuzzles.

If our machine is smart enough, it will track CANDY individuals and keep them alive as long as possible.

# Let us create a CANDY machine and feed wuzzles CANDY!


## Further notes about the rules of Wuzzlopolis environment


- Every wuzzle has a set of flavors they can eat, but can't eat other flavors. ['peach', 'tarball', 'toe fuzz']
- If a wuzzle doesn't eat, it has a chance of SUDDEN DEATH. Every day unfed increases the chance of SUDDEN DEATH.
- If a CANDY individual isn't eaten for a day, it has a chance of SUDDEN DEATH. Every day unlicked increases the chance of SUDDEN DEATH.
- Every wuzzle has his own CANDY cookbook with lists sorted by CANDY breed where CANDY individuals can be listed. Our machine will pick CANDY individuals based on what CANDY individuals are on each CANDY list.
- Every wuzzle owns a lunchbox that can have up to 20 CANDY. Our machine will load the lunchbox from the cook book.
- When we say a wuzzle eats a candy, it actually just **licks** it and tosses it back into the wild. That wuzzle will never lick it again, but other wuzzles can lick the same candy.


# More about the CANDY machine.

- Each wuzzle has a cookbook that is a collection of lists. These are effectively **queues** of CANDY individuals that could potentially be licked.
- Our machine will pick individuals from those queues to be **added** to this particular wuzzles lunchbox.
- The wuzzle will **open** the lunchbox each day and see if they like any of the CANDY. If they do, they will lick it... So the lunchbox must be refilled every day.
- Our machine will be using **reinforcement learning** to determine which queues and which particular candy to put in each lunchbox. It might get **rewards** when:
	- A wuzzle is fed
	- A CANDY is licked
	- A wuzzle makes it through the day, or possibly a score for wuzzles each day
	- A CANDY makes it through the day, or possibly a score for CANDY each day
- We should probably build a few machines and compare them with each other. So it should be fairly **modular**.

---

# Development Setup

Create the virtual environment:

	source bin/activate
	pip install -r requirements.txt
	
	
***Future Considerations***:

	What if CANDY was actually wuzzles in disguise?
	What if wuzzles and CANDY can have **babies**?
	CANDY might lay eggs in wuzzle poop. We're not sure about that yet.

