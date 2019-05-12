infile = open("FinalGame.txt", 'rt', encoding = 'utf-8')
necro = infile.readlines()
infile.close()

print(necro[0])

class Intro: #intro is a slightly different class because theres no branching options that need to come off it, but not substantially different to PlayerInteract

    def __init__(self, queue, text_pos):
        self.queue = queue
        self.text_pos = text_pos

    def runtext(self):
        queue = self.queue
        text_pos = self.text_pos
        response = str(input("Your Options are: "+ queue))
        response = response.lower()
        while True: #while loops were the only way I could figure out how to repeatedly prompt for inputs, explanation of them was found on stackexchange
            if queue not in response:
                print("Error, your options are:", queue)
                response = str(input())
                continue
            else:
                break #things get wild without this little word right here

        print(text_pos)

        return

knockout = Intro("rest", necro[4])
knockout.runtext()

wakeup = Intro("open eyes", necro[8])
wakeup.runtext()

print(necro[10])#straight transitional block text between choice styles, end of intro

yourname = str(input("What is your name?"))

class PlayerInteract:
    def __init__(self, queue, text_pos):
        self.queue = queue
        self.text_pos = text_pos

    def runtext(self):
        queue = self.queue
        text_pos = self.text_pos
        text_pos = text_pos.replace("Player_name", yourname)# Now that theres an assignend playername, all instances of the placeholder name from the text need to be removed every time, which is why its in the class
        queue = queue.lower()
        response = queue #change from Intro class is here, found that keeping this here prevented me from screwing myself stylistically if I had a captial letter in somewhere
        response = response.lower()
        while True:
            if queue not in response:
                print("Error, did you mean:", queue, "?")
                response = str(input())
                continue
            else:
                break

        print(text_pos)

        return

newchar = PlayerInteract(yourname,necro[14])
newchar.runtext()

where = """ "No", "Yes, the necropolis?(enter yes)" """ #explanation of why yes is in () later
playerselect = str(input("Your Options Are: "+ where))
playerselect = playerselect.lower()

while True:
    if "no" in playerselect:
        nores = PlayerInteract("no", necro[21])
        nores.runtext()

    elif playerselect not in where:
        if playerselect not in where:
                print("Error, your options are:", where)
                playerselect = str(input())
                playerselect = playerselect.lower()
                continue
        else:
            break # again my only solition to figuring out how to repeatedly ask for input
    elif "yes" in playerselect:#somehow this broke with more than one word entry even though the same thing works perfectly fine later
        somemem = PlayerInteract ("necropolis", necro[24])
        somemem.runtext()
    break

interact = """ "Telkani?", "Who are you?", "Kagash?", "Necropolis?", "I should go": """
playerchoice = str(input("Your Options Are: "+ interact))
playerchoice = playerchoice.lower()
#belatedly realized I used the above twice and 100% could have made a funtion out of it.

while True:
    if "i should go" not in playerchoice: #i should go the only break option, meaning it needs to be on a different, higher level than all the other choices so they can all answer to it
        if "telkani" in playerchoice:
            telkanires = PlayerInteract ("Telkani",necro[34])
            telkanires.runtext()
            playerchoice = str(input("Your Options Are: "+ interact))
            playerchoice = playerchoice.lower() #these two lines are repeated on every single one to maintain the ability to switch between prompts
            continue
        elif "who are you" in playerchoice:
            who_res =PlayerInteract ("Who are you?", necro[37])
            who_res.runtext()
            playerchoice = str(input("Your Options Are: "+ interact))
            playerchoice = playerchoice.lower()
            continue
        elif "kagash" in playerchoice:
            kagashres = PlayerInteract ("Kagash?", necro[31])
            kagashres.runtext()
            playerchoice = str(input("Your Options Are: "+ interact))
            playerchoice = playerchoice.lower()
            continue
        elif "necropolis" in playerchoice:
            polisres= PlayerInteract("Necropolis?", necro[28])
            polisres.runtext()
            playerchoice = str(input("Your Options Are: "+ interact))
            playerchoice = playerchoice.lower()
            continue
        elif "i should go" in playerchoice:
            print(necro[40])
            break
        elif playerchoice not in interact:
            if playerchoice not in interact:
                print("Error, your options are:", interact)
                playerchoice = str(input())
                playerchoice = playerchoice.lower()
                continue
            else:
                break
    elif "i should go" in playerchoice: #allowing the same variable to change everywhere means this still works here even if it wouldnt one lower down. Which it didnt
        print(necro[40])
    break 

print("End of Demo")
