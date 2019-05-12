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

# Player_Name = input("Enter One Name: ")
# class PC:
#     def __init__(self, Player_Name):
#         self.Player_Name = Player_Name
#
#     def respond(self):
#         print(self.Player_Name + ":" + necro[23])#hardcoded for testing
#
#
# def main():
#     char = PC(Player_Name)
#     char.respond()
#
# if __name__ == "__main__":
#     main()

#BUTTON TESTING, SAVE FOR LATER?
# import graphics #from the Zelle book, found it on the internet
# from graphics import *
#
# def main():
#     win = graphics.GraphWin("Hello", 1000,600)
#     message = Text(Point(600, 70), necro[0])#hard coded for testing purposes
#     message.draw(win)
#     win.getMouse()
# main()
# #word wrap is an issue here, this may be too ambitious to get this as a pop up

#
# def main():
#     win = GraphWin("Rest")
#     message = Text(Point(100,100), "Rest")
#     message.draw(win)
#     win.getMouse()
#     # for i in range(10):
#     #     p = win.getMouse()
#     #     print("tested", p.getX(), p.getY())
#
# main()
#
#
