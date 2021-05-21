#Fantasy Football

'''
import requests
from bs4 import BeautifulSoup

web_link= "https://www.teamrankings.com/nfl/player-stat/quarterback-wins"
result = requests.get(web_link)

#404 - Content not present   200 - present and ok
print(result.status_code)

#Content
src = result.content

soup = BeautifulSoup(src,'lxml')

links = soup.find_all("td")
#titles = soup.find(class="text-right")
#print(titles)
print("\n")


#player = input("Who's passing attempts would you like to know?")


class Player(name):
    def __init__(self,name):
        self.name = name

#

def passing_attempts(player):
    
    Given a player, this program will find how many passing attempts that player has
    had so far in the season from "https://www.teamrankings.com/nfl/player-stat/passing-plays-completed"
    
    counter = 0
    loop = True
    while loop:
        try:
            lol = links[counter].attrs['data-sort']
            if player in lol:
                print(player + " has {0} wins".format((int(links[counter+3].attrs['data-sort']))%1000))
                loop = False
        except:
            pass
        counter += 1

#passing_attempts(player)
'''
"""
This is a player class that stores Player Objects.
"""
class Player:
    def __init__(self, name, cost, value):
        self.name = name
        self.cost = cost
        self.value = value
        
    def getName(self):
        return self.name

    def getCost(self):
        return self.cost

    def getValue(self):
        return self.value

"""
This class will be where the crux of the calculations happen.
"""
class Battlefield:
    playerData = []
    
    """
    This function is resposible for collecting all of the user input data regarding players"""
    def store_player_data():
        player,flag = None, True
        while flag:
            name = input("Player: ")
            flag = False
            if name != "Done":
                points = int(input("Projected Points: "))
                cost = int(input("Cost?: "))
                p = Player(name, cost, points)
                Battlefield.playerData.append(p)
                flag = True

    def getPlayerAt(index):
        return Battlefield.playerData[index]
    
    def find_max_points(playerData, money):
        if not playerData or money < 0:        #Exit Case: Player List empty or run out of money
            return 0
        else:
            if money - playerData[0].cost >= 0:
                first = playerData[0].value + Battlefield.find_max_points(playerData[1:], money - playerData[0].cost)
                second =  Battlefield.find_max_points(playerData[1:], money)
                return max(first,second)
            
            else:
                return 0
            
            

    def pathways(playerData, target, money):
        if not playerData or Battlefield.overshoot(playerData[0], target, money):
            return
        
        elif Battlefield.hitTarget(playerData[0], target, money):
            return playerData[0].name
        
        else:
            #If there is a path, these should return a list of the names that lead up to the target
            first = Battlefield.pathways(playerData[1:], target - playerData[0].value, money - playerData[0].cost)   #Assume we take the first, find the best out of the remaining
            second = Battlefield.pathways(playerData[1:], target, money)

            if first:
                return first + " " + playerData[0].name
            return second

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
    print(Battlefield.playerData)
    
    Battlefield.store_player_data()
    
    points = Battlefield.find_max_points(Battlefield.playerData, 10)
    print(points)

    print(Battlefield.pathways(Battlefield.playerData, points, 10))
    #store = [['a', 1, 2], ['d', 1, 6], ['f', 7, 8], ['h', 100, 4]]
    #print(store)
    #max_points = find_max_points(store, 10)
    

main()
#max_points(store_player_data(), 3)


#print(max_subseq(2567,5))
'''

            print("Testing: " + str(player_data[0][0]))
            print("\n")
            first = pathways(player_data[1:], target - player_data[0][1], money - player_data[0][2], iteration + 1)
            print(first)
            if first:
                first = [player_data[0][0]] + first
            print(player_data[1:])
            print("Below is second")
            second = pathways(player_data[1:], target, money, iteration + 1)
            
            #print(list(first))
            #print(list(second))
            print("First + Second: " + str(first + second))
            return first + second
'''
