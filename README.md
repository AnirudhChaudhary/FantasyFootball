# FantasyFootball

Issue: 
- FanDuel hosts competitions for players to create their own superteam given a budget. Each user is allowed a fixed number of entries into the competitions and winners get cash prizes.

Project:
There are two components to this project:
  1. Predict the number of points a player will get in a given game based on multiple factors like:
    a. Home / Away
    b. Offense / Defense
    c. Surrounding Players
    d. Performance in previous weeks
    e. Strength of opposition
    
  2. Given players with projected points and a given salary, create a lineup of players that are optimized based on salary and points predicted.
  
 Currently: working on step number 2. Step number 1 involves machine learning and will be attacked once the optimization is complete.


## Objectives:
1. ** Multipliers **
2. ** Position Handling **
3. ** Test Case Handling **
4. ** Algorithm Speedup **

## Objective Explanation
1. ** Multipliers **
Incorporate multipliers for players that we think are going to perform exceptionally well. This would be another case to add to the "dynamic program"
For every player we consider adding the player as a normal player, adding as a multiplied player, or not adding the player

2. ** Position Handling **
Need to consider players based off of their positions as well. Perhaps this could be done by creating another variable in the battlefield class
that represents what players have already been picked. You could optimize player selection to only cases where you would actually need that player

Notes: Perhaps need to change how classes work and interact with one another

Player Class: handles all methods related to players regarding cost, position, value and name
Battlefield Class: handles what players we have chosen and what positions they inhabit
Analytics Class: Takes in a list of players and the battlefield that we have and finds the best path with the players available and battlefield

Be able to take a list of players, their costs, and their values and construct a list of players that are most optimal

3. ** Test Case Handling / Code Management **
 Need to make the test case situation much better. Create a better framework for the way that I create tests. Need to make assertions rather than
just print statements.

4. ** Algorithm Speedup **
The algorithm that is used in this program could be made better (faster and more efficient) if implemented with a dynamic program. when there are large inputs, it may be more helpful to implement a dyamic program to save repeated calculations