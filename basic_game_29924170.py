
"""
COMBAT SIMULATOR BASIC VERSION
Author name :Chaithra Kumar 
Created Date :09-August -2018
Updated Date: 23-August -2018
Description of program :
Program to Simulate Simple Combat Simulator
Each player or Commander has total of 10$ at the starting,
Each player can purchase a maximum  of 10 units at 1$ for each unit.
Each player gets to select three units :Archer(A),Soldier(S),Knight(k)
Units are made to fight in the order which they were purchased.
The winner of each unit round is shown.
The winner of each battle is left to fight the next round and the loser unit dies.
At the end of the combat if the player is left out he wins the entire battle.

"""
# declaring dictionary to print unit names
Soldier_name = {
  "A": "Archer",
  "S": "Soldier",
  "K": "Knight",

                }

# creating BasicGame class


class BasicGame:

    """ Constructor __init__  to initial class variable
         Instance Variables :
            self.player_name : String
                    hold player name
            self.player_list : list
                    hold player army units

         Parameters:
            player_name : String
                    player name to assign instance variable self.player_name
            player_list : list
                    list of units that must be assigned to instance variable self.army_list

    """

    def __init__(self, player_name, player_list):
        self.player_name = player_name
        self.army_list = player_list

    """ 
        input_fun is method to take input from the user (list of units) ,store it in army_list[] list
        return : None
    
    """

    def input_fun(self):
        print("\n"+self.player_name+":")
        print("You have 10$ - Purchase each unit at 1$  ")
        while True:
            if len(self.army_list) < 10:  # Maximum number of units is 10

                print("\n"+str(10 - len(self.army_list)) + "$ Remaining!")  # Remaining units
                self.print_army()

                x = input("Select your Unit \n A:Archer 1$ \n K:Knight 1$ \n S:Soldier 1$ \n F:Finalize your army :")
                # if the user wants to finalize the units ,he Presses F
                if x == "F":
                    # display prompt to the user if units are remaining
                    print("\n" + str(10 - len(self.army_list)) + " " + "$ Remaining!")
                    yes_no = input("do you wish to finalize the army :\n Press F to finalize and C to Continue").strip()
                    if yes_no == "C":
                        continue
                    elif yes_no == "F":
                        break
                    else:
                        print("Invalid Response")
                        continue
                    # if the user selects (A,K,S) as unit ,the selected unit is appended to the users list ,
                elif x == "A" or x == "S" or x == "K":
                    self.army_list.append(x)
                    # display invalid response if inappropriate response is submitted
                else:
                    print("invalid response")
                    continue
            # if number of units selected is 10 ,exit the loop
            elif len(self.army_list) == 10:
                break

    """
        print_army method to print the units in the player_list
        Return :None
    """
    def print_army(self):
        if len(self.army_list):
            print("-------------------------")
            print(self.player_name + " Army:")
            for each in self.army_list:
                print(Soldier_name[each], sep=' ', end=' ', flush=True)
            print("\n-------------------------")


""" battle_winner function to decide winner of each battle and 
    Parameter:
        player1obj : object of BasicGame Class
                -- player name and units selected by the player1
        player2obj : object of BasicGame Class
                -- player name and units selected by the player1
    return: none
"""


def battle_winner(player1obj, player2obj):
    winner = ""  # variable used to assign winner for each battle
    round_number = 0  # to keep count of number of battles fought
    print("\n")
    while len(player1obj.army_list) and len(player2obj.army_list):
        if player1obj.army_list[0] == player2obj.army_list[0]:
            winner = player1obj.army_list[0]
        elif player1obj.army_list[0] in ["S", "A"] and player2obj.army_list[0] in ["S", "A"]:
            winner = "A"
        elif player1obj.army_list[0] in ["K", "A"] and player2obj.army_list[0] in ["K", "A"]:
            winner = "K"
        elif player1obj.army_list[0] in ["K", "S"] and player2obj.army_list[0] in ["K", "S"]:
            winner = "S"
        round_number = round_number + 1  # increment count after each battle
        print("Round "+str(round_number)+":")
        print_winner(winner, player1obj, player2obj)  # print the winner of each battle


"""
    print_winner : function to print the winner of each battle and remove the unit from the lost player list
    Parameter : 
        winner:String
            - winner of each battle
        player1obj : object of BasicGame Class
                -- player name and units selected by the player1
        player2obj : object of BasicGame Class
                -- player name and units selected by the player1
    return : none
"""


def print_winner(winner, player1obj, player2obj):

    if player1obj.army_list[0] == winner and player2obj.army_list[0] == winner:  # condition for tie
        print("Tie" + ":" + Soldier_name[winner] + " v/s " + Soldier_name[winner])
        player1obj.army_list.pop(0)  # remove the unit from both the  players list using pop() method
        player2obj.army_list.pop(0)
        # if last round is tie and one of the players have units left in the army.
        if len(player1obj.army_list) == 0 and len(player2obj.army_list) > 0:
            print("Player2 has units left")
            player2obj.print_army()
        elif len(player2obj.army_list) == 0 and len(player1obj.army_list) > 0:
            print("Player1 has units left")
            player1obj.print_army()

    elif player1obj.army_list[0] == winner:
        # condition if winner unit is in player1 list(remove(pop) unit from player2 list)
        print("Player 1 wins against player 2: " + Soldier_name[player1obj.army_list[0]] + " wins against ", end=' ')
        print(Soldier_name[player2obj.army_list.pop(0)])
    else:
        # condition if winner unit is in player2 list(remove(pop) unit from player1 list)
        print("Player 2 wins against player 1: " + Soldier_name[player2obj.army_list[0]] + " wins against ", end='')
        print(Soldier_name[player1obj.army_list.pop(0)])


print("-------------------------------")
print("COMBAT SIMULATOR BASIC VERSION")
print("-------------------------------")
# creating object of BasicGame class and initialising the player name and list to instance variables for player1
player1 = BasicGame("Player1", [])
# calling the input_fun method  to read the units and store in list for player1
player1.input_fun()
# calling the print_army method to print the units of player1
player1.print_army()
# creating object of BasicGame class and initialing the player name and list to instance variables for player2
player2 = BasicGame("Player2", [])
# calling the input_fun method  to read the units and store in list for player2
player2.input_fun()
# calling the print_army method to print the units of player2
player2.print_army()
# calling battle_winner function to decide winner of each battle
print("---------------------------------------")
print("BATTLE BEGINS!")
battle_winner(player1, player2)
print("----------------------------------------")

# print the battle winner , the player left with units wins the battle
print("\n*********************************************")
print("Battle Over:")
if len(player1.army_list) == len(player2.army_list):
    print("No winner declared ! It's a Tie")
elif len(player1.army_list) < len(player2.army_list):
    print("Player 2 wins the battle")
    print("Congratulations!")
elif len(player1.army_list) > len(player2.army_list):
    print("Player 1 wins the battle")
    print("Congratulations!")
print("*********************************************")

