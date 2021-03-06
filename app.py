import constants
import copy
from statistics import mean

players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)
num_players = int(len(players) / len(teams))

exp_players = []
inexp_players = []
panthers = []
bandits = []
warriors = []

# converting experience into boolean value, creating exp,inexp list of players, and converting height into integer, cleaned up "and" in guardians
def clean_data():
    for my_players in players:
        my_players['height'] = int(my_players['height'].split()[0])
        my_players['guardians'] = my_players['guardians'].replace(' and',',')
        if my_players['experience'] == 'YES':
            my_players['experience'] = True
            exp_players.append(my_players)
        else: 
            my_players['experience'] = False
            inexp_players.append(my_players)
    
        

# equally distributing exp,inexp players into the 3 teams
def sort_teams():
    for x in range(0, int((num_players /2))):
        panthers.append(exp_players[x])
    for x in range(0, int(num_players /2)):  
        panthers.append(inexp_players[x])
    for x in range(int(num_players / 2), int(num_players)):
        bandits.append(exp_players[x])
    for x in range(int(num_players / 2), int(num_players)):  
        bandits.append(inexp_players[x])
    for x in range(int(num_players), len(exp_players)):
        warriors.append(exp_players[x])
    for x in range(int(num_players), len(inexp_players)):  
        warriors.append(inexp_players[x])

# stats output to be called from menu_screen() function 
def show_stats(name, team):
    player_list = []
    guardians = []
    height_list = []
    exp = 0
    inexp = 0 
    for tm in team:
        player_list.append(tm['name'])
    for tm in team:
        guardians.append(tm['guardians'])
    for tm in team:
        if tm['experience'] == True:
            exp += 1
        else:
            inexp += 1
    for tm in team:
        height_list.append(tm['height'])
    average_height = mean(height_list)
    print("\n" + name + " Stats\n-------------\n")
    print("total players: {}".format(len(player_list)))
    print("total experienced: {}".format(exp))
    print("total inexperienced: {}".format(inexp))
    print("Average height: {}".format(round(average_height, 1)))
    print("\nPlayers:\n   " + ", ".join(player_list))
    print("Guardians:\n   " + ", ".join(guardians))

# main menu screen
def menu_screen():
    print("\n\nWILSON'S BASEBALL TEAM STATS TOOL\n\n---- MENU -----\n\n")
    while True:
        try:
            choice = int(input("  What do you want to do?\n 1. Display team stats\n 2. Quit\n\nEnter your choice > "))   
            if choice == 1:
                print("\n\n 1. Panthers\n 2. Bandits\n 3. Warriors\n\n")
                while True:
                    try:
                        select = int(input("Choose a team > "))
                        if select == 1:
                            show_stats("Panthers", panthers)
                            proceed_menu()
                        elif select == 2:
                            show_stats("Bandits", bandits)
                            proceed_menu()
                        elif select == 3:
                            show_stats("Warriors", warriors)
                            proceed_menu()
                        else:
                            raise ValueError
                            continue
                    except ValueError:
                        print("Invalid inpout, try again.")
                        continue
                    break
            elif choice == 2: 
                print("\n\nThanks, see you soon!")
                break
            else:
                raise ValueError
                continue
        except:
            print("\n\nInvalid input, try again\n\n")
            continue
        break
# proceed menu after stats are shown for each team. Probably could've looped it in the menu function but it was getting kinda messy        
def proceed_menu():
    while True:
        try:
            proceed = input("\n\nPress E to continue, or Q to quit> ")
            if proceed.lower()  == 'e':
                menu_screen()
                break
            elif proceed.lower() == 'q':
                print("Thanks, see you soon!")
                break
            else:
                raise ValueError
                continue
        except:
            print("invalid input, try again")
            continue


if __name__ == "__main__":
    clean_data()
    sort_teams()        
    menu_screen()
