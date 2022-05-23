#Fantasy Football Training Framework

"""
This is the file where we will create our testing frameworks and write our test cases for the Fantasy Football Project.
"""
import FantasyFootball as FF


def testing():
    #test_same_val()
    #test_not_enough_bank()
    test_regular()
    test_positions_once()
    test_not_all_positions()
    test_multiple_positions()

"""
Testing if position handling is working properly
"""

def test_regular():
    print("***** TESTING REGULAR ***** \n")

    bank = 10
    inp = [['a', 'QB', 1, 2], ['d','QB', 1, 6], ['f', 'RB', 7, 8], ['h', 'RB', 4, 100]]

    
    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB'])

    #print(Battlefield.playerData)

    final = FF.Util.find_max_points(bank, [])

    print(final)

    return

def test_positions_once():
    print("***** TESTING POSITION HANDLING ***** \n \n")
    print("*** TEST POSITION ONCE ***")

    bank = 10
    inp = [['a', 'QB', 3,3], ['b', 'RB', 4,4]]
    
    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB']) #inputting looks to be fine

    print("final: ", FF.Util.find_max_points(bank, []))
    return

def test_not_all_positions():
    print("\n*** TESTING NOT ALL POSITIONS ***")

    bank = 5
    inp = [['f', 'RB', 7, 8]]

    
    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB'])

    #print(Battlefield.playerData)

    final = FF.Util.find_max_points(bank, [])

    print(final)

    return

def test_multiple_positions():
    print("\n***** TESTING MULTIPLE POSITIONS *****")

    bank = 10
    #[name, position, cost, value]
    inp = [['nooooo', 'QB', 10, 100], ['a', 'QB', 5, 25], ['b', 'RB', 5, 25]]

    FF.InputOutput.store_player_data_bulk(inp, ['QB', 'RB'])

    final = FF.Util.find_max_points(bank, [])

    print(final)

    return

"""
Test that we don't get an output if we don't have enough money in the bank to begin with. 
"""

def validation():
    bank = int(input("How much money is avaliable? "))
    FF.InputOutput.store_player_data_manually()
    #store = [['a', 1, 2], ['d', 1, 6], ['f', 7, 8], ['h', 100, 4]]
    points = FF.Util.find_max_points(bank, [])
    #points = Battlefield.find_max_points(store, bank)
    print("MAX POINTS POSSIBLE: ", points)

    #print("PLAYERS THAT YOU SHOULD PICK: ", Battlefield.pathways(store, points, bank))
    
    #print(store)
    #max_points = find_max_points(store, 10)
    
    

def main():
    test_type = input("Would you like to run all tests (test) or validate (validate)? ")

    if test_type == "test":
        testing()
    else:
        validation()
    return

main()
    