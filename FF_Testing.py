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
    test_simple()
    print("\n")
    test_multiple_multipliers()
    #test_multiple_multipliers_small()

"""
Testing if position handling is working properly
"""

def test_simple():
    bank = 10

    inp = [['a', 'QB', 9, 1], ['b', 'RB', 1, 4], ['c', 'QB', 1, 5]]
    multipliers = [2,1]

    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB'])
    
    final = FF.Util.find_max_points(bank,[], multipliers, None)

    assert(final[0] == 14)

    print(final)
    print("\n")

def test_multiple_multipliers():
    bank = 10
    inp = [['a', 'QB', 2, 1], ['b', 'RB', 1, 4], ['c', 'WR', 1, 5]]

    multipliers = [2, 1.5, 1]

    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB', 'WR'])
    
    final = FF.Util.find_max_points(bank,[], multipliers, None)

    print(final)
    print("Expected: 17")

def test_multiple_multipliers_small():
    bank = 10
    inp = [['a', 'QB', 2, 1], ['b', 'RB', 1, 4]]
    multipliers = [2,1]

    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB'])
    
    final = FF.Util.find_max_points(bank,[], multipliers, None)

    print(final)
    print("Expected: 9")



def test_regular():
    print("***** TESTING REGULAR ***** \n")

    bank = 10
    inp = [['a', 'QB', 1, 2], ['d','QB', 1, 6], ['f', 'RB', 7, 8], ['h', 'RB', 4, 100]]

    
    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB'])

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
    
    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB']) #inputting looks to be fine

    print("final: ", FF.Util.find_max_points(bank, []))
    FF.Battlefield.reset()
    return

def test_not_all_positions():
    print("\n*** TESTING NOT ALL POSITIONS ***")

    bank = 5
    inp = [['f', 'RB', 7, 8]]

    
    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB'])

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

    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB'])

    final = FF.Util.find_max_points(bank, [])

    FF.Battlefield.reset()

    print(final)

    return


def test_multiple_same_position():

    print("\n***** TESTING PICK MULTIPLE OF SAME PLAYER *****")

    bank = 10
    #[name, position, cost, value]
    inp = [['nooooo', 'QB', 10, 100], ['a', 'QB', 5, 25], ['b', 'RB1', 3, 25], ['c', 'RB2', 2, 35]]

    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB1', 'RB2'])

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
    