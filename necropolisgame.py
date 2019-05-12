infile = open("FinalGame.txt", 'rt', encoding = 'utf-8')
necro = infile.readlines()
infile.close()

print(necro[0])

class Intro:

    def __init__(self, queue, text_pos):
        self.queue = queue
        self.text_pos = text_pos

    def runtext(self):
        queue = self.queue
        text_pos = self.text_pos
        response = str(input("Your Options are: "+ queue))
        response = response.lower()
        while True:
            if queue not in response:
                print("Error, your options are:", queue)
                response = str(input())
                continue
            else:
                break

        print(text_pos)

        return

knockout = Intro("rest", necro[4])
knockout.runtext()

wakeup = Intro("open eyes", necro[8])
wakeup.runtext()

print(necro[10])

yourname = str(input("What is your name?"))

class PlayerInteract:
    def __init__(self, queue, text_pos):
        self.queue = queue
        self.text_pos = text_pos

    def runtext(self):
        queue = self.queue
        text_pos = self.text_pos
        text_pos = text_pos.replace("Player_name", yourname)
        queue = queue.lower()
        response = queue #str(input("Your Options are: "+ interact))
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

where = """ "No", "Yes, the necropolis?(enter yes)" """
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
            break
    elif "yes" in playerselect:#somehow this broke with more than one word entry even though the same thing works perfectly fine later
        somemem = PlayerInteract ("necropolis", necro[24])
        somemem.runtext()
    break

interact = """ "Telkani?", "Who are you?", "Kagash?", "Necropolis?", "I should go": """
playerchoice = str(input("Your Options Are: "+ interact))
playerchoice = playerchoice.lower()
while True:
    if "i should go" not in playerchoice:
        if "telkani" in playerchoice:
            telkanires = PlayerInteract ("Telkani",necro[34])
            telkanires.runtext()
            playerchoice = str(input("Your Options Are: "+ interact))
            playerchoice = playerchoice.lower()
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
    elif "i should go" in playerchoice:
        print(necro[40])
    break

print("End of Demo")
