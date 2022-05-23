#Fantasy Football

"""
This is a player class that stores Player Objects.
"""

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
    num_positions = 0   


class InputOutput:
    """
    This function is resposible for collecting all of the user input data regarding players from a manually user input.
    """
    def store_player_data_manually():
        # TODO: FIX PLAYER INPUT (IE BAD INPUTS)

        want_to_add_player, want_to_add_position = True, True
        num_positions = 0 
        # print("First I need to know how many different positions there are. List out the position or write 'done' \n")
        # while want_to_add_position:
        #     pos = input("Position: ")
        #     if pos == "done":
        #         want_to_add_player = False
        #     else:
        #         Battlefield.playerData[pos] = []
        #         num_positions += 1
        # #update our battlefield to store the number of positions that we want to consider
        # Battlefield.num_positions = num_positions
        while want_to_add_player:
            name = input("Player: ")
            name = name.upper()
            want_to_add_player = False

            #Fill in fields for our newly created player
            if name != "DONE":
                position = input("Position: ")                  #INPUT CHECKS
                points = float(input("Projected Points: "))
                cost = float(input("Cost?: "))
                p = Player(name, position, cost, points)
                
                if position in Battlefield.playerData.keys():
                    Battlefield.playerData[position].append(p)
                else:
                    Battlefield.playerData[position] = [p]
                    Battlefield.num_positions += 1
                want_to_add_player = True
                print("\n")

    """
    This function is responsible for collecting user input data regarding players in bulk using predefined data in the input list.
    """
    def store_player_data_bulk(input_list, position_list):
        counter = 0 
        for position in position_list:
            Battlefield.playerData[position] = []

        Battlefield.num_positions = len(position_list)
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
        field -> list tells us what position we have chosen so far

    Output:
        integer -> the maximum number of points that you can receive with the given playerData money, and field
    """
    def find_max_points(money, field):
        #print("FIELD: ", field)
        # Ran out of money so we shouldn't include the player (maybe need to use negative infinity)
        if money < 0 or (money == 0 and len(field) != Battlefield.num_positions):
            return (float("-inf"),[])
        
        if len(field) == Battlefield.num_positions:
            return (0, [])
        
        #Go through all of the possible positions and find one that we haven't set yet
        for position in Battlefield.playerData.keys():
                if position not in field:
                        starting_position = position
                        break
        
        
        max_points = 0
        final_arrangement = []
        #temp field stores a copy of field so that we can add different position players
        temp_field = field.copy()
        for player in Battlefield.playerData[starting_position]:
            new_money = money - player.cost
            temp_field.append(position)

            rest_tuple = Util.find_max_points(new_money, temp_field)
            
            curr_points = player.value + rest_tuple[0]
            rest_tuple[1].append(player.name)
            arrangement = rest_tuple[1]

            if curr_points > max_points:
                max_points = curr_points
                final_arrangement = arrangement 

            temp_field = field


        return (max_points, final_arrangement)

