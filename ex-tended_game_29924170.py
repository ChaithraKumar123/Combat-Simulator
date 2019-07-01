# EXTENDED GAME
"""
COMBAT SIMULATOR Extended VERSION (Medics and Expanded Army)
Author name :Chaithra Kumar 
Created Date :13-August -2018
Updated Date: 23-August -2018
Description of program :
Program to Simulate Extended Combat Simulator
Each player or Commander has total of 10$ at the starting,
Each player can purchase a maximum  of 10 units at respective cost
Each player gets to select five units :Archer(A),Soldier(S),Knight(k),Siege Equipment(SE),Wizard(W)(EXPANDED ARMIES)
Archer(A)-3$,Soldier(S)-1$,Knight(k)-1$,Siege Equipment(SE)-2$,Wizard(W)-3$
Units are made to fight in the order which they were purchased.
The winner of each unit round is shown.
The winner of each battle is left to fight the next round and the loser unit dies.
If Money is Remaining after the armies it will be used for hiring medics .
Medics: when the units die ,it will be returned bck at the end of pool if the medics is supplied .
Each time medics is supplied 1$ is deducted for all the units.
At the end of the combat if the player is left out he wins the entire battle.
"""

# declaring dictionary to print unit names
Soldier_name = {
  "A": "Archer",
  "S": "Soldier",
  "K": "Knight",
  "SE": "Siege Equipment",
  "W": "Wizard"
            }

# declaring dictionary to assign unit values
unit_price = {
    "A": 3,
    "S": 1,
    "K": 1,
    "SE": 2,
    "W": 3

            }

"""
    creating ExtendedGame class
    This class takes input from the user and displays the list of units entered by the user
"""


class ExtendedGame:

    """
        Constructor __init__ : to initial class variable
        Instance variables:
            self.player_name :String
                - used to store player name
            self.army_list :list
                - use to store units selected by players
            self.rem_funds : int
                - to store remaining funds left
        Parameters:
            player_name : String
                 player name to assign instance variable self.player_name
            player_list : list
                 list of units that must be assigned to instance variable self.army_list
            rem_funds : int
                 remaining fund to assign to instance variable self.rem_funds

    """
    def __init__(self, player_name, player_list, rem_funds):
        self.player_name = player_name
        self.army_list = player_list
        self.rem_funds = rem_funds

    """
        input_fun: method to take input from the user(list of units), store it in army_list[] list
        return :none
        
    """
    def input_fun(self):
        print("\n"+self.player_name+":")
        print("You have 10$ : Purchase units at respective cost")
        while True:
            print("---------------------------")
            if self.rem_funds > 0:  # Remaining funds should be greater than zero

                print(str(self.rem_funds) + "$ Remaining!")
                self.print_army()
                print("\nSelect your Player")
                print(" A:Archer 3$ \n K:Knight 1$ \n S:Soldier 1$", end='\n')
                print(" SE:Siege Equipment 2$ \n W:Wizard 3$ \nF:Finalize your army :")
                x = input().strip()
                # if the user wants to finalize the units ,he Presses F
                if x == "F":
                    if self.rem_funds < 10:
                        # display prompt to the user if units are remaining
                        print("\n" + str(self.rem_funds) + "$ Remaining!")
                        print("Do you wish to finalize the army :\n Press F to finalize and C to Continue")
                        yes_no = input().strip()
                        if yes_no == "C":
                            continue
                        elif yes_no == "F":
                            break
                        else:
                            print("Invalid Response")
                            continue
                # if the user selects (A,K,S,SE,W) as unit ,the selected unit is appended to the users list ,
                elif x == "A" or x == "S" or x == "K" or x == "SE" or x == "W":
                    # check for negative balance
                    if (self.rem_funds - unit_price[x]) < 0:
                        print("Negative balance cannot purchase this unit!")
                    else:
                        self.army_list.append(x)
                        self.rem_funds = (self.rem_funds - unit_price[x])
                else:
                    print("invalid response")
                    continue
            # if remaining funds is 0 ,break the loop
            elif self.rem_funds == 0:
                break
            print("\n---------------------------")

    """ 
      print_army : method to print the units in the player_list
      return : none
    
    """
    def print_army(self):
        if len(self.army_list):
            print(self.player_name + " Army", end=':')
            for each in self.army_list:
                print(Soldier_name[each], sep=' ', end=' ', flush=True)


""" battle_winner function to decide winner of each battle and 
    Parameter:
        player1obj : object of BasicGame Class
                -- player name and units selected by the player1
        player2obj : object of BasicGame Class
                -- player name and units selected by the player1
    return : none
"""


def battle_winner(player1obj, player2obj):
    winner = ""  # variable used to assign winner for each battle
    round_number = 0  # to keep count of number of battles fought
    print("\nBattle Begins:")
    while len(player1obj.army_list) and len(player2obj.army_list):
        if player1obj.army_list[0] == player2obj.army_list[0]:
            winner = player1obj.army_list[0]
        elif player1obj.army_list[0] in ["S", "A"] and player2obj.army_list[0] in ["S", "A"]:
            winner = "A"
        elif player1obj.army_list[0] in ["K", "A"] and player2obj.army_list[0] in ["K", "A"]:
            winner = "K"
        elif player1obj.army_list[0] in ["K", "S"] and player2obj.army_list[0] in ["K", "S"]:
            winner = "S"
        elif player1obj.army_list[0] in ["W", "A"] and player2obj.army_list[0] in ["W", "A"]:
            winner = "A"
        elif player1obj.army_list[0] in ["SE", "K"] and player2obj.army_list[0] in ["SE", "K"]:
            winner = "K"
        elif player1obj.army_list[0] in ["SE", "A", "S"] and player2obj.army_list[0] in ["SE", "A", "S"]:
            winner = "SE"
        elif player2obj.army_list[0] in ["W", "K", "SE", "S"] and player1obj.army_list[0] in ["W", "K", "SE", "S"]:
            winner = "W"
        round_number = round_number + 1  # increment count after each battle
        print("Round " + str(round_number) + ":")
        print_winner(winner, player1obj, player2obj) # print the winner of each battle


"""  medics function to prompt whether the player wants to retain the units,if yes it is appended to back of the list
    Parameter:
        playerobj : object of BasicGame Class
                -- player name and units selected by the player1
        player : string
                -- name of the unit which won the battle 
    return : none
"""


def medics(playerobj, player):
    print("-------------------------------")
    if playerobj.rem_funds == 0:  # check if remaining funds are equal to zero
        print(playerobj.player_name + ": "+"zero funds left cannot retain the player")
    else:
        print(playerobj.player_name + ": Medics left:"+" "+str(playerobj.rem_funds))
        while True:
            yes_no = input(" Do you want to retain the player("+Soldier_name[player]+")(y/n)")
            if yes_no == "y" or yes_no == "Y":
                playerobj.rem_funds = playerobj.rem_funds - 1
                playerobj.army_list.append(player)
                print(playerobj.player_name+" :"+Soldier_name[player]+ " retained Medics left:" + str(playerobj.rem_funds) + "")
                playerobj.print_army()
                break
            elif yes_no == "n" or  yes_no == "N":
                break
            else:
                print("invalid input!")
                continue
    print("\n-------------------------")


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

    if player1obj.army_list[0] == winner and player2obj.army_list[0] == winner:
        print("Tie" + ":" + Soldier_name[winner] + " v/s " + Soldier_name[winner])
        # remove the unit from both the  players list using pop() method
        # prompt both players to use medics
        medics(player1obj, player1obj.army_list.pop(0))
        medics(player2obj, player2obj.army_list.pop(0))
        # if last round is tie and one of the players have units left in the army.
        if len(player1obj.army_list) == 0 and len(player2obj.army_list) > 0:
            print("Player2 has units left")
            player2obj.print_army()
        elif len(player2obj.army_list) == 0 and len(player1obj.army_list) > 0:
            print("Player1 has units left")
            player1obj.print_army()

    elif player1obj.army_list[0] == winner:
        # condition if winner unit is in player1 list(remove(pop) unit from player2 list)
        # prompt player2 to use medics
        print("Player 1 wins against player 2: " + Soldier_name[player1obj.army_list[0]] + " wins against ", end='')
        print(Soldier_name[player2obj.army_list[0]])
        medics(player2obj, player2obj.army_list.pop(0))
    else:
        # condition if winner unit is in player2 list(remove(pop) unit from player1 list)
        # prompt player1 to use medics
        print("Player 2 wins against player 1: " + Soldier_name[player2obj.army_list[0]] + " wins against ", end='')
        print(Soldier_name[player1obj.army_list[0]])
        medics(player1obj, player1obj.army_list.pop(0))


print("-------------------------------------------------------------")
print("COMBAT SIMULATOR EXTENDED VERSION (Medics and Expanded armies)")
print("-------------------------------------------------------------")
# creating object of ExtendedGame class and initialing the player name and list to instance variables for player1
player1 = ExtendedGame("Player1", [], 10)
# calling the input_fun method  to read the units and store in list for player1
player1.input_fun()
# calling the print_army method to print the units of player1
print("\n-------------------------------")
player1.print_army()
print("\nMedics and Supplies:" + str(player1.rem_funds) + "$")
print("-------------------------------")
# creating object of ExtendedGame class and initialing the player name and list to instance variables for player2
player2 = ExtendedGame("Player2", [], 10)
# calling the input_fun method  to read the units and store in list for player1
player2.input_fun()
print("\n-------------------------------")
# calling the print_army method to print the units of player1
player2.print_army()
print("\nMedics and Supplies:" + str(player2.rem_funds))
# calling battle_winner function to decide winner of each round
print("-------------------------------")
battle_winner(player1, player2)

# print the battle winner , the player left with units wins the battle
print("\n*******************************************")
print("Battle Over:")
if len(player1.army_list) == len(player2.army_list):
    print("No winner declared ! It's a Tie")
elif len(player1.army_list) < len(player2.army_list):
    print(" Player 2 wins the battle")
    print("Congratulations!")
elif len(player1.army_list) > len(player2.army_list):
    print(" Player 1 wins the battle")
    print("Congratulations!")
print("*******************************************")

