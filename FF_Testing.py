#Fantasy Football Training Framework

"""
This is the file where we will create our testing frameworks and write our test cases for the Fantasy Football Project.
"""
import FantasyFootball as FF



def testing():
    #test_same_val()
    #test_not_enough_bank()
    #test_regular()
    #test_positions_once()
    #test_not_all_positions()
    #test_multiple_positions()
    #test_multiple_same_position()
    #test_simple()
    print("\n")
    #test_multiple_multipliers()
    test_complex_one_position()
    test_complex_one_position_multiple()
    test_complex_one_position_multiple_money_manage()
    #test_multiple_multipliers_small()

"""
Testing if position handling is working properly
"""

def test_simple():
    bank = 10

    inp = [['a', 'QB', 9, 1], ['b', 'RB', 1, 4], ['c', 'QB', 1, 5]]
    multipliers = [2,1]

    FF.InputOutput.store_predefined_player_data(inp, ['QB', 'RB'])
    
    final = FF.Util.find_max_points(bank,[], multipliers, None)

    assert(final[0] == 14)

    print(final)
    print("\n")

def test_complex():
    bank = 16

    inp = [['a', 'QB', 5, 3], ['b', 'RB', 3, 2], ['c', 'WR', 4, 5], ['d', 'QB', 6, 7], ['e', 'RB', 5,4], ['f', 'WR', 5, 10]]
    multipliers = [1,1,1]

    FF.InputOutput.store_predefined_player_data(inp, ['QB', 'RB', 'WR'])
    
    final = FF.Util.find_max_points(bank,[], multipliers)


    print(final)
    print("\n")

def test_complex_one_position():
    '''
    This is meant to test if we can get the correct result if there is no restriction on positions of the players, simply picking the best 5 players.
    In the case that we are just picking based on the best 5 players, then we don't need to store by position. We can go straight into the calculation where 
    we make considerations about whether or not we pick the current player and if we do pick, then what multiplier do we give.
    
    [player, position, cost, value]
    '''

    bank = 10

    inp = [['a', 'Util', 5, 5], ['b', 'Util', 3, 5], ['c', 'Util', 7, 6]]

    multipliers = [2,1]

    FF.InputOutput.store_predefined_player_data(inp, ['Util'])

    FF.Battlefield.num_positions = len(multipliers)

    points, assignment = FF.Util.find_max_points_no_positions(bank,[], multipliers)
    
    assert(points == 17)

    print(points)
    print(assignment)
    print("\n")
    FF.Battlefield.reset()
    return

def test_complex_one_position_multiple():
    '''
    This is meant to test if we can get the correct result if there is no restriction on positions of the players, simply picking the best 5 players.
    In the case that we are just picking based on the best 5 players, then we don't need to store by position. We can go straight into the calculation where 
    we make considerations about whether or not we pick the current player and if we do pick, then what multiplier do we give.
    
    [player, position, cost, value]
    '''

    bank = 10

    inp = [['a', 'Util', 1, 1], ['b', 'Util', 1, 1], ['c', 'Util', 1, 1], ['d', 'Util', 1, 1], ['e', 'Util', 5, 5], ['f', 'Util', 5, 5]]

    multipliers = [2,1]

    positions = ['Util']

    FF.InputOutput.store_predefined_player_data(inp, positions)

    FF.Battlefield.num_positions = len(multipliers)

    
    final = FF.Util.find_max_points_no_positions(bank,[], multipliers)


    print(final)
    print("\n")
    FF.Battlefield.reset()
    return

def test_complex_one_position_multiple_money_manage():
    '''
    This is meant to test if we can get the correct result if there is no restriction on positions of the players, simply picking the best 5 players.
    In the case that we are just picking based on the best 5 players, then we don't need to store by position. We can go straight into the calculation where 
    we make considerations about whether or not we pick the current player and if we do pick, then what multiplier do we give.
    '''

    bank = 60000

    inp = [['Butler', 'Util', 16000, 42.41], ['Tatum', 'Util', 15500, 45.01], ['Brown', 'Util', 14000, 37.71], ['Horford', 'Util', 13000, 30.60], ['Lowry', 'Util', 12000, 30.17], ['williams', 'Util', 11500, 31.59], ['adebayo', 'Util', 11000, 38.02], ['Herro', 'Util', 10000, 30.92], ['White','Util', 9500, 26.73], ['Tucker', 'Util', 9000, 19.66], ['Strus', 'Util', 8500, 18.05], ['G. Williams', 'Util', 8000, 16.94], ['Vincent', 'Util', 7500, 17.41], ['Oladipo', 'Util', 7500, 20.99], ['Martin', 'Util', 7000, 16.74], ['Robinson', 'Util', 7000, 16.61], ['Pritchard', 'Util', 6500, 12.11], ['Dedmon', 'Util', 6500, 14.81], ['Highsmith', 'Util', 6000, 4.14]]

    multipliers = [2,1.5,1.2,1,1]

    FF.InputOutput.store_predefined_player_data(inp, ['Util'])

    FF.Battlefield.num_positions = len(multipliers)

    
    final = FF.Util.find_max_points_no_positions(bank,[], multipliers)

    print(final)
    print("\n")
    FF.Battlefield.reset()
    return


def test_multiple_multipliers():
    bank = 10
    inp = [['a', 'QB', 2, 1], ['b', 'RB', 1, 4], ['c', 'WR', 1, 5]]

    multipliers = [2, 1.5, 1]

    FF.InputOutput.store_predefined_player_data(inp, ['QB', 'RB', 'WR'])
    
    final = FF.Util.find_max_points(bank,[], multipliers, None)

    print(final)
    print("Expected: 17")

def test_multiple_multipliers_small():
    bank = 10
    inp = [['a', 'QB', 2, 1], ['b', 'RB', 1, 4]]
    multipliers = [2,1]

    FF.InputOutput.store_predefined_player_data(inp, ['QB', 'RB'])
    
    final = FF.Util.find_max_points(bank,[], multipliers, None)

    print(final)
    print("Expected: 9")



def test_regular():
    print("***** TESTING REGULAR ***** \n")

    bank = 10
    inp = [['a', 'QB', 1, 2], ['d','QB', 1, 6], ['f', 'RB', 7, 8], ['h', 'RB', 4, 100]]

    
    FF.InputOutput.store_predefined_player_data(inp, ['QB', 'RB'])

    #print(Battlefield.playerData)

    final = FF.Util.find_max_points(bank, [])

    print(final)
    FF.Battlefield.reset()

    return

def test_positions_once():
    print("***** TESTING POSITION HANDLING ***** \n \n")
    print("*** TEST POSITION ONCE ***")

    bank = 10
    inp = [['a', 'QB', 3,3], ['b', 'RB', 4,4]]
    
    FF.InputOutput.store_predefined_player_data(inp, ['QB', 'RB']) #inputting looks to be fine

    print("final: ", FF.Util.find_max_points(bank, []))
    FF.Battlefield.reset()
    return

def test_not_all_positions():
    print("\n*** TESTING NOT ALL POSITIONS ***")

    bank = 5
    inp = [['f', 'RB', 7, 8]]

    
    FF.InputOutput.store_predefined_player_data(inp, ['QB', 'RB'])

    #print(Battlefield.playerData)

    final = FF.Util.find_max_points(bank, [],)

    print(final)
    FF.Battlefield.reset()

    return

def test_multiple_positions():
    print("\n***** TESTING MULTIPLE POSITIONS *****")

    bank = 10
    #[name, position, cost, value]
    inp = [['nooooo', 'QB', 10, 100], ['a', 'QB', 5, 25], ['b', 'RB', 5, 25]]

    FF.InputOutput.store_predefined_player_data(inp, ['QB', 'RB'])

    final = FF.Util.find_max_points(bank, [])

    FF.Battlefield.reset()

    print(final)

    return


def test_multiple_same_position():

    print("\n***** TESTING PICK MULTIPLE OF SAME PLAYER *****")

    bank = 10
    #[name, position, cost, value]
    inp = [['nooooo', 'QB', 10, 100], ['a', 'QB', 5, 25], ['b', 'RB1', 3, 25], ['c', 'RB2', 2, 35]]

    FF.InputOutput.store_predefined_player_data(inp, ['QB', 'RB1', 'RB2'])

    final = FF.Util.find_max_points(bank, [])

    print(final)
    FF.Battlefield.reset()

    return

def manual():
    bank = int(input("How much money is avaliable? "))
    FF.InputOutput.store_player_data_manually()
    #store = [['a', 1, 2], ['d', 1, 6], ['f', 7, 8], ['h', 100, 4]]
    points = FF.Util.find_max_points(bank, [])

    return points
    
    

def main():
    test_type = input("Would you like to run all tests (test) or manually enter data (manual)? ")

    if test_type == "test":
        testing()
    else:
        manual()
    return

main()
    