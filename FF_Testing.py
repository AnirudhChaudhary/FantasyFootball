#Fantasy Football Training Framework

"""
This is the file where we will create our testing frameworks and write our test cases for the Fantasy Football Project.
"""




def test_func():
    print("hello from the testing file :)")

    test_all()

"""
This is the function where we will define all of our test cases to run.
"""
def test_all():
    test_same_val()
    test_regular()

"""
Testing if our function works with all the players having the same value.
"""
def test_same_val():
    inp = [['a',3,3], ['b',3,3], ['c',3,3]]
    
    Battlefield.store_player_data_bulk(inp)
    