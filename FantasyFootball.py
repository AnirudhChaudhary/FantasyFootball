#Fantasy Football

"""
Current Objective:

2. Need to consider players based off of their positions as well. Perhaps this could be done by creating another variable in the battlefield class
that represents what players have already been picked. You could optimize player selection to only cases where you would actually need that player

Notes: Perhaps need to change how classes work and interact with one another

Player Class: handles all methods related to players regarding cost, position, value and name
Battlefield Class: handles what players we have chosen and what positions they inhabit
Analytics Class: Takes in a list of players and the battlefield that we have and finds the best path with the players available and battlefield

Be able to take a list of players, their costs, and their values and construct a list of players that are most optimal

Future Objectives:
1. Incorporate multipliers for players that we think are going to perform exceptionally well. This would be another case to add to the "dynamic program"
For every player we consider adding the player as a normal player, adding as a multiplied player, or not adding the player



3. Need to make the test case situation much better. Create a better framework for the way that I create tests. Need to make assertions rather than
just print statements.
"""
"""
This is a player class that stores Player Objects.
"""
import sys
from FF_Testing import test_func


class Player:
    def __init__(self, name, position, cost, value):
        self.name = name
        self.position = position
        self.cost = cost
        self.value = value

    def __repr__(self):
        return "\nPlayer: %s, Position: %s, Cost: %s, Value: %s" % (self.name, self.position, self.cost, self.value)

"""
This class will be where the crux of the calculations happen.
"""
class Battlefield:
    #This variable is set to be public because we want all Battlefield instances to access all players
    playerData = {}
    num_positions = 2   #Can decide to make this variable later

    def __init__(self):
        self.QB = None
        self.RB = None
        #self.WR1 = None
        #self.WR2 = None
        #self.FLEX = None

    """
    Returns the player at the specified index
    """
    def getPlayerAt(index):
        return Battlefield.playerData[index]


class InputOutput:
    """
    This function is resposible for collecting all of the user input data regarding players from a manually user input.

    Position handling: √
    """
    def store_player_data_manually():
        # TODO: FIX PLAYER INPUT (IE BAD INPUTS)

        player,flag = None, True
        while flag:
            print("First I need to know how many different positions there are. List out the position or write 'done'")
            pos = input("Position: ")
            if pos == "done":
                break
            else:
                Battlefield.playerData[pos] = []
        while flag:
            name = input("Player: ")
            name = name.upper()
            flag = False
            if name != "DONE":
                position = input("Position: ")
                points = float(input("Projected Points: "))
                cost = float(input("Cost?: "))
                p = Player(name, position, cost, points)
                Battlefield.playerData[position].append(p)
                flag = True

    """
    This function is responsible for collecting user input data regarding players in bulk using predefined data in the input list.
    """
    def store_player_data_bulk(input_list, position_list):
        counter = 0 
        for position in position_list:
            Battlefield.playerData[position] = []
        num_players = len(input_list)
        while counter < num_players:
            current_player = input_list[counter]
            name = current_player[0]
            position = current_player[1]
            cost = current_player[2]
            points = current_player[3]

            p = Player(name, position, cost, points)
            Battlefield.playerData[position].append(p)

            counter += 1

        return

class Util:
    """
    Given a list of players in player data and the allocated money, returns the max amount of points possible. This is not
    taking into consideration who the player is. Rather this is just trying to find the max amount and then a different function
    will try to find the order that created this max.

    Input: 
        playerData -> List of player data [name, position, cost, value]
        money -> int: represents how much money you have left to work with

    Output:
        integer -> the maximum number of points that you can receive with the given playerData money, and field
    """
    def find_max_points_old(playerData, money, field):
        #Exit Case: Player List empty or run out of money
        if not playerData or money < 0:        
            return 0

        #established that we have a player, need to decide what to do with that player
        else:
            player = playerData[0]
            if money - player.cost >= 0:
                #Don't choose the player, so we keep our field the same
                no_choose_player =  Util.find_max_points(playerData[1:], money)

                #Choose the player so have to change the position in the field and also make sure that we subtract the cost that might come along with that

                choose_player = playerData[0].value + Util.find_max_points(playerData[1:], money - player.cost)
                
                return max(choose_player,no_choose_player)
            
            else:
                return 0

    """
    Given a list of players in player data and the allocated money, returns the max amount of points possible. This is not
    taking into consideration who the player is. Rather this is just trying to find the max amount and then a different function
    will try to find the order that created this max.

    Input: 
        playerData -> List of player data [name, position, cost, value]
        money -> int: represents how much money you have left to work with
        field -> list tells us what position we have chosen so far

    Output:
        integer -> the maximum number of points that you can receive with the given playerData money, and field
    """
    def find_max_points(money, field):

        #Exit Case: Battlefield is full or run out of money
        if len(field) == Battlefield.num_positions or money < 0:
            return 0
        
        #print("PLAYER DATA: ", Battlefield.playerData)

        #print("FIELD: ", field)
        
        #Go through all of the possible positions and find one that we haven't set yet
        for position in Battlefield.playerData.keys():
                if position not in field:
                        starting_position = position
                        break

        #Now that we have our starting position, go through all of the possible candidates for that position
        #For each candidate, you want to add the value of picking that candidate and then take away the cost for that candidate

        max_points = 0
        new_field = field.copy()
        for player in Battlefield.playerData[position]:
            new_money = money - player.cost
            new_field.append(position)
            
            curr_points = player.value + Util.find_max_points(new_money, new_field)

            if curr_points > max_points:
                max_points = curr_points
            
            new_field = field

        return max_points
            
    """
    Finds and returns the pathways to the max amount of points
    """
    def pathways(playerData, target, money):
        if not playerData or Util.overshoot(playerData[0], target, money):
            return
        
        elif Util.hitTarget(playerData[0], target, money):
            return playerData[0].name
        
        else:
            #If there is a path, these should return a list of the names that lead up to the target
            first = Util.pathways(playerData[1:], target - playerData[0].value, money - playerData[0].cost)   #Assume we take the first, find the best out of the remaining
            second = Util.pathways(playerData[1:], target, money)

            if first:
                return first + " " + playerData[0].name
            return second

    '''
    Perhaps the next thing to do here would have these two functions merge into one function that can return 'hit' or
    'overshoot'
    '''
    def hitTarget(player, target, money):
        if target - player.value == 0 and money - player.cost >= 0:
            return True
        else:
            return False

    def overshoot(player, target, money):
        if target - player.value < 0 or money - player.cost < 0:
            return True
        else:
            return False


def main():
    test_type = input("Would you like to run all tests (test) or validate (validate)? ")

    if test_type == "test":
        testing()
    else:
        validation()
    return

"""
This is the function that will be used for testing different scenarios and to make sure that all test cases are passsing.

"""
def testing():
    #test_same_val()
    #test_not_enough_bank()
    test_regular()
    test_positions_once()

"""
Testing if position handling is working properly
"""
def test_positions_once():
    print("***** TESTING POSITION HANDLING ***** \n")

    bank = 10
    inp = [['a', 'QB', 3,3], ['b', 'RB', 4,4]]


    InputOutput.store_player_data_bulk(inp, ['QB', 'RB']) #inputting looks to be fine

    initial = Battlefield()

    print("final: ", Util.find_max_points(bank, []))


    return

def test_regular():
    print("***** TESTING REGULAR ***** \n")

    bank = 10
    inp = [['a', 'QB', 1, 2], ['d','QB', 1, 6], ['f', 'RB', 7, 8], ['h', 'RB', 4, 100]]

    InputOutput.store_player_data_bulk(inp, ['QB', 'RB'])

    #print(Battlefield.playerData)

    final = Util.find_max_points(bank, [])

    print(final)

    return


"""
Testing if our function works with all the players having the same value.
"""
def test_same_val():
    print("TESTING SAME VAL")
    bank = 3
    inp = [['a',3,3], ['b',3,3], ['c',3,3]]
    
    InputOutput.store_player_data_bulk(inp)

    points = Util.find_max_points(Battlefield.playerData, bank)
    #points = Battlefield.find_max_points(store, bank)
    print("MAX POINTS POSSIBLE: ", points)
    assert(points == 3)

    print("PLAYERS THAT YOU SHOULD PICK: ", Util.pathways(Battlefield.playerData, points, bank))
    #print("PLAYERS THAT YOU SHOULD PICK: ", Battlefield.pathways(store, points, bank))

"""
Test that we don't get an output if we don't have enough money in the bank to begin with. 
"""
def test_not_enough_bank():
    print("TESTING NOT ENOUGH BANK")
    bank = 2
    inp = [['a',3,3], ['b',3,3], ['c',3,3]]
    
    Battlefield.store_player_data_bulk(inp)

    points = Battlefield.find_max_points(Battlefield.playerData, bank)
    #points = Battlefield.find_max_points(store, bank)
    print("MAX POINTS POSSIBLE: ", points)
    #assert(points == 3)

    print("PLAYERS THAT YOU SHOULD PICK: ", Battlefield.pathways(Battlefield.playerData, points, bank))
    #print("PLAYERS THAT YOU SHOULD PICK: ", Battlefield.pathways(store, points, bank))
    



def validation():
    bank = int(input("How much money is avaliable? "))
    
    Battlefield.store_player_data_manually()
    #store = [['a', 1, 2], ['d', 1, 6], ['f', 7, 8], ['h', 100, 4]]
    points = Battlefield.find_max_points(Battlefield.playerData, bank)
    #points = Battlefield.find_max_points(store, bank)
    print("MAX POINTS POSSIBLE: ", points)

    print("PLAYERS THAT YOU SHOULD PICK: ", Battlefield.pathways(Battlefield.playerData, points, bank))
    #print("PLAYERS THAT YOU SHOULD PICK: ", Battlefield.pathways(store, points, bank))
    
    #print(store)
    #max_points = find_max_points(store, 10)
    

main()
