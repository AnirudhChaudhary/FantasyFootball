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
        return "Player: %s, Position: %s, Cost: %s, Value: %s" % (self.name, self.position, self.cost, self.value)

"""
This class will be where the crux of the calculations happen.
"""
class Battlefield:
    #This variable is set to be public because we want all Battlefield instances to access all players
    playerData = {}
    num_positions = 0 

    #This function resets the Battlefield back to it's default orientation. 
    #There was a bug where the testing function calls were persistently affecting the battlefield over multiple function calls
    def reset():
        Battlefield.playerData = {}
        Battlefield.num_positions = 0


class InputOutput:
    """
    This function is resposible for collecting all of the user input data regarding players from a manually user input.
    """
    def store_player_data_manually():
        # TODO: FIX PLAYER INPUT (IE BAD INPUTS)

        want_to_add_player= True
        num_positions = 0 

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


    def store_predefined_player_data(input_list, position_list):
        """
        This function is responsible for creating a battlefield based on user input data. All player information has to be specified beforehand.

        TODO: Handle input validation
        Input:
            input_list -> List[List[String]]
            position_list -> List[Positions]
        
        Return:
            None
        """
        counter = 0 
        #initialize all the positions to be empty
        for position in position_list:
            Battlefield.playerData[position] = []

        
        Battlefield.num_positions = len(position_list)
        num_players = len(input_list)
        while counter < num_players:
            #parse the input data for player information
            current_player = input_list[counter]
            name = current_player[0]
            position = current_player[1]
            cost = current_player[2]
            points = current_player[3]
            
            #create player object and add to the battlefield
            p = Player(name, position, cost, points)
            Battlefield.playerData[position].append(p)

            counter += 1

        return

class Util:
    """
    Given a list of players in player data and the allocated money, returns the max amount of points possible. This is not
    taking into consideration who the players are that result in the optimal. 
    Rather this is just trying to find the max amount and then a different function will try to find the order that created this max.

    Input: 
        playerData -> List of player data [name, position, cost, value]
        money -> int: represents how much money you have left to work with
        field -> list tells us what position we have chosen so far

    Output:
        integer -> the maximum number of points that you can receive with the given playerData money, and field
    """

    def find_max_points_no_positions(money,chosenPlayers, multipliers):
        '''
        This is the function that we will use to find out what players to pick, assuming we are in a competition where there are no restrictions on 
        what players we choose.

        The multipliers will be our base case, telling us when we need to stop
        '''
        #print("Starting Function with: ", chosenPlayers)

        #Use too much money -> we can't take the arrangement into consideration so return negative inf to make sure arrangement isn't considered
        #Used our money but we don't have the correct number of players
        if money < 0 or (money == 0 and len(chosenPlayers) != Battlefield.num_positions):
            #print("ran out of money")
            return (float("-inf"),[])

        #If we have used up all our multipliers then we can't add any more value
        if len(multipliers) == 0:
            #print("no more multipliers")
            return (0, [])

        max_points = 0
        final_arrangement = []
        original_multipliers = multipliers.copy()
        original_field = chosenPlayers.copy()
        flexibile_field = chosenPlayers.copy()

        #Go through all of the players that we have
        for player in Battlefield.playerData['Util']:
            
            #only need to consider the players that we don't have already
            if player not in chosenPlayers:
                new_money = money - player.cost
                flexibile_field.append(player)
                for mult in multipliers:
                    #Remove it to create a new instance where we don't have as many multipliers
                    multipliers.remove(mult)

                    tuple_with_current_multiplier = Util.find_max_points_no_positions(new_money, flexibile_field, multipliers)
                    
                    points_w_curr_mult = tuple_with_current_multiplier[0]
                    arrange_w_curr_mult = tuple_with_current_multiplier[1]

                    #Best we can do currently is to take the multiplier we chose and add the max without that multiplier (calculated in step above)
                    curr_points = player.value * mult + points_w_curr_mult

                    title = player.name + ": " + str(mult)
                    arrange_w_curr_mult.append(title)
                    arrangement = arrange_w_curr_mult

                    if curr_points > max_points:
                        max_points = curr_points
                        final_arrangement = arrangement 
                    multipliers = original_multipliers.copy()
                flexibile_field = original_field.copy()

        return (max_points, final_arrangement)
                    



    def find_max_points(money,field, multipliers):
        final_tuple = Util.find_max_points_helper(money, field, multipliers)
        max_points = final_tuple[0]
        final_arrangement = final_tuple[1]
        if len(final_arrangement) != Battlefield.num_positions:
            print("FINAL ARRANGMENT: ", final_arrangement)
            print("Invalid arrangment")
        else:
            print("MAX POINTS: ", max_points)
            print("ARRANGEMENT: ", final_arrangement)
        
        return (0,0)



    def find_max_points_helper(money, field, multipliers):
        # Ran out of money so we shouldn't include the player (maybe need to use negative infinity)
        if money < 0 or (money == 0 and len(field) != Battlefield.num_positions):
            #print("ah here")
            return (float("-inf"),[])
        
        if len(field) == Battlefield.num_positions:
            #print("ah here 2")
            return (0, [])
        
        #Go through all of the possible positions and find one that we haven't set yet
        for position in Battlefield.playerData.keys():
                if position not in field:
                        starting_position = position
                        break
        
        #print("CHOOSING: ", starting_position)
        max_points = 0
        final_arrangement = []
        #temp field stores a copy of field so that we can add different position players
        original_field = field.copy()
        flexible_field = field.copy()
        #print(original_field)
        #print(field)
        #print(Battlefield.playerData[starting_position])
        for player in Battlefield.playerData[starting_position]:
            #print("TEMP FIELD: ",temp_field)
            new_money = money - player.cost
            flexible_field.append(starting_position)

            #At this stage, we can choose what multiplier to give to our player or no multiplier
            original_multipliers = multipliers.copy()
            for multiplier in original_multipliers:
                #print("Multiplier: ", multiplier)
                #print("POSITION: ", starting_position)
                #print("BEFORE CALL FIELD: ", flexible_field)
                #print("\n")
                #print("multipliers before: ", multipliers)
                multipliers.remove(multiplier)
                
                tuple_with_current_multiplier = Util.find_max_points_helper(new_money, flexible_field, multipliers)

                points_w_curr_mult = tuple_with_current_multiplier[0]
                arrange_w_curr_mult = tuple_with_current_multiplier[1]
                curr_points = player.value * multiplier + points_w_curr_mult

                arrange_w_curr_mult.append(player.name)
                arrangement = arrange_w_curr_mult

                if curr_points > max_points:
                    max_points = curr_points
                    final_arrangement = arrangement 
                multipliers = original_multipliers.copy()

                
            flexible_field = original_field.copy()


        return (max_points, final_arrangement)

    
