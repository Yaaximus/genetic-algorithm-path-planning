# Python implementation of Genetic Algorithm in Path Planning

![GA_path_planning](https://user-images.githubusercontent.com/37571161/58662732-51820100-8344-11e9-97fb-a66e6e1cc877.gif)

## Running instruction:
- Run the main.py file from directory. 
- User can defined path points, links b/w path points, population size, mutation rate
in the Config.py file

## Requirements
- python
- numpy

## Features
- user can define fixed links b/w nodes
- user can initialize population of chromosomes which are initialized randomly
but program insures that two consective nodes should be linked to each other.
- user can calculate chromosome fitness based on total distance of chromosomes
and connectivity of nodes.
- user can find best fitness indices
- user can rank the initial population of chromosomes using roulets wheels 
selection method
- user can do crossover on the population
- user can do mutation on the population

## Fixed issues:
- bug fixed in create population function
- bug related to chromosome population fitness best indices removed
- Bug in generate mating pool function of ranking file fixed
- Bug removed in function check fitness based on connection in fitness file

## Example for usage: 
#### You can initialize population in main function like:
- chr_population = population()
#### You can calculate fitness & find best fitness indices in main function like:
- chr_pop_fitness, chr_best_fitness_index = fitness(chr_pop=chr_population)
#### You can obtain ranked population in main function like:
- chr_ranked_population = ranking(chr_pop_fitness=chr_pop_fitness, pop=chr_population)
#### You can do crossover & mutation in main function like:
- chr_crossover_mutated_population = dna(chr_pop_fitness=chr_pop_fitness, 
ranked_population=chr_ranked_population, chr_best_fitness_index=chr_best_fitness_index,
last_pop=chr_population)

## Objective
- Use Genetic Algorithm for finding a best path for mobile robot in a 2D environment.
- To move from starting point to the endpoint while avoiding collisions with
obstacles and minimizing total distance travelled.

## Problem Statement

<li>Mobile robots move in environments, which can be static or dynamic.</li>
<li>In the static environment shown in the Fig., the MR is required to move from the start
point to the endpoint (Goal) on permissible paths while avoiding collisions with the
obstacles and minimizing the total distance travelled, time taken or energy consumed.</li></br>

<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/37571161/82874509-7c9b3280-9f4f-11ea-8b68-f2231e13617b.PNG">
</p>

## Methodology
Genetic Algorithms: A stochastic evolutionary technique based on human genetics.

## Theory

### Stochastic Methods

<li>Stochastic Methods are based on laws of probability for sampling of random events and have
the advantage that they can handle large problems.</li>

### Genetic Algorithms (GA)

<li>The GA method is applicable to both static and dynamic environments. In static environment
all coordinates (MR, obstacles, goal) are input into the onboard computer system of MR while
in dynamic environment sensors need to be used.</li>

<li>A brief comparison between genetic algorithms and human genetics is given below:</li>

<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/37571161/82874755-db60ac00-9f4f-11ea-919d-15a77d13960c.png">
</p>

## GA Program

<li>A chromosome consists of path points from Start to End</li>

<li>Each path has an associated length Or “distance”</li>

<li>Objective is to find the “optimal” path i.e. the shortest path</li>

## Flow Chart of Genetic Algorithm

<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/37571161/82874940-2aa6dc80-9f50-11ea-8927-02845a76a1c3.png">
</p>

## Algorithm Development

### Create Environment

The Environment is “created” by defining the workspace i.e. the 2D min and max of the coordinates
(x,y); there are 7 obstacles and path points labeled 0-15 i.e. 16 path points; Starting Position is 0 and
End-Point is 15 (see figure).

<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/37571161/82875166-7ce7fd80-9f50-11ea-997c-174aa7540e9c.png">
</p>

Note that link points in table are 1 through 16 and in adjoining image they are from 0 to 15.

### Fitness of each chromosome

The “fitness” of a path is the inverse of the length of the path from starting point to end-point

<p>Fitness(iPath) = 1.0/DistanceInPath(iPath)</p>

### Chromosome Length

No. of chromosomes: NC=20

For each iteration select 40% of these i.e. 8 chromosomes

<p> No. of Bits NBITS = log NPTS /log 2 = log 16 / log 2 = 4</p>
<p>If there are 1024 points, then NBITS = log 1024/log 2 = 10</p>

<p>CHR_LEN=(NOBS+2)*NBITS = (7+2)*4 = 36 for 7 obstacles and 4 bits</p>
<p>CHR_LEN = (7+2)*10=900 for 7 obstacles and 10 bits</p>

## Selection of Path Points (Generating Population)
A Path is generated by selected points from a specified start-point to a specified end-point.

<li>Starting Point</li>
<li>Consider each link point</li>
<li>Find distance from each link point to end-point</li>
<li>Calculate the Probability of moving to each link point (PDF and CDF)</li>
<li>Generate a random number in (0,1)</li>
<li>Select the next point in path (based on the random number generated)</li>
<li>Continue till end point is reached</li>

## Summary
An optimal solution is obtained by generating an initial population of chromosomes (paths
consisting of path points), computing their “fitness” to select “best” parents for producing the
“next generation” of chromosomes by carrying out evolutionary procedures of cross-over and
mutation. The procedure is continued until no further improvement is possible; this is called
“convergence” which corresponds to an “optimal” solution.