# Spreading Rumours
## Project Overview
This project focuses on simulating the spread of rumors within a population, represented on a 100x100 grid. The individuals in the population have varying levels of skepticism (S4, S3, S2, and S1), influencing their likelihood of believing and spreading rumors. The project aims to investigate how changing parameters such as population density (P), transmission delay (L), and the distribution of skepticism levels impact the rate of rumor spread in the network.

## Simulation Details
1. **Population Initialization:**
The population is distributed randomly on a 100x100 grid with varying population density (P).
Individuals are assigned one of four skepticism levels (S4, S3, S2, S1) randomly.

2. **Rumor Spread:**
* An isolated person initiates the rumor, spreading it to all neighboring individuals.
* Each individual decides to pass the rumor based on their skepticism level.
* If an individual receives the rumor from at least two neighbors in the same generation, their skepticism temporarily decreases.

3. **Transmission Delay:**
* After transmitting the rumor, an individual cannot transmit it again for L generations (a parameter to be experimented with).

4. **Simulation and Statistics:**
* Run each simulation at least 10 times to account for the non-deterministic nature of the process.
* Measure the rate of rumor spread, i.e., the percentage of the population exposed to the rumor up to a certain generation.
* Consider additional measures to analyze network behavior.

## Parameters to Investigate
1. **Population Density (P):**
  Vary P to observe its impact on rumor spread.
2. **Transmission Delay (L):**
  Experiment with different values of L to understand its effect on the spread.
3. **Skepticism Levels Ratio:**
  Alter the distribution of skepticism levels to investigate its influence.

## Implementation
1. **Random Distribution (Section A):**
  * Implement the initial random distribution of skepticism levels in the population.
2. **Strategic Placement (Section B):**
  * Propose and implement a strategy for placing individuals to significantly change network behavior.
  * For example, experiment with clustering individuals with similar skepticism levels.


## Running the Simulation
Navigate to the dist folder.
```shell
cd dist
```
To run seif_a.exe, enter the following command:
```shell
.\seif_a.exe
```
To run seif_b.exe, enter the following command:
```shell
.\seif_b.exe
```
## results
<p align="center">
  <img src="https://github.com/YuvalDahari/arknoid-game/blob/master/pics/%D7%AA%D7%9E%D7%95%D7%A0%D7%94%20%D7%A9%D7%9C%20WhatsApp%E2%80%8F%202024-06-25%20%D7%91%D7%A9%D7%A2%D7%94%2001.28.59_bdb300d9.jpg?raw=true" alt="level 1" width="45%"/>
  <img src="https://github.com/YuvalDahari/arknoid-game/blob/master/pics/%D7%AA%D7%9E%D7%95%D7%A0%D7%94%20%D7%A9%D7%9C%20WhatsApp%E2%80%8F%202024-06-25%20%D7%91%D7%A9%D7%A2%D7%94%2001.25.59_7fb47738.jpg?raw=true" alt="level 2" width="45%"/>
</p>
<p align="center">
  <img src="https://github.com/YuvalDahari/arknoid-game/blob/master/pics/%D7%AA%D7%9E%D7%95%D7%A0%D7%94%20%D7%A9%D7%9C%20WhatsApp%E2%80%8F%202024-06-25%20%D7%91%D7%A9%D7%A2%D7%94%2001.26.37_f325acb8.jpg?raw=true" alt="level 3" width="45%"/>
  <img src="https://github.com/YuvalDahari/arknoid-game/blob/master/pics/%D7%AA%D7%9E%D7%95%D7%A0%D7%94%20%D7%A9%D7%9C%20WhatsApp%E2%80%8F%202024-06-25%20%D7%91%D7%A9%D7%A2%D7%94%2001.28.15_07a5d35e.jpg?raw=true" alt="level 4" width="45%"/>
</p>

in the results we can see different square colors.
- gray: no one is in this area
- green- there is a person in the square but he did not get any rumor
- red: the person in that square got a rumor
