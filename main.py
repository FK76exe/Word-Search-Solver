from Grid import Grid
import os

def checkGrid(file):
    f = open(file,"r")
    lines = f.readlines()
    for x in range(1,len(lines)):
        if (len(lines[x-1].replace('\n','')) != len(lines[x].replace('\n',''))):
            return False
    return True

print(
'''Welcome to Word Search Solver! To add a new grid to search words for, create a text file and place it in the Grids folder.
Note that all rows in the grid must have same length to be accepted.
To add a list of words, create a text file and place it in the WordList folder.  
For formatting, see the examples already listed there.
For commands, see README file''')

n = ''
gridMade = False
while n != "quit":
    n = input(">")
    if n.lower() == "quit":
        print("Exiting Program")
        quit()
    elif n.lower() == "new":
        path = os.getcwd() + "\\Grids"
        print("Pick an option:")
        try:
            for x in range(len(os.listdir(path))):
                print("{}: {}".format(x,os.listdir(path)[x]))
            choice = int(input())
            file = "Grids/" + os.listdir(path)[choice]
            if checkGrid(file):
                grid = Grid(file)
                gridMade = True
            else:
                print ("Invalid Grid. Must be rectangular (all rows must be equal length) and grid must have at least one row")
        except:
            print("Invalid option. Must be an integer and has to be a given key")
    if gridMade:
        if n.lower() == "print":
            grid.printGrid()
        elif n.split(" ")[0].lower() == "find" and len(n.split(" ")) == 2:
            grid.printSelected(grid.findWord(n.split(" ")[1]))
        elif n.lower() == "findall":
            try:
                path = os.getcwd() + "\\WordLists"
                print("Pick an option")
                for x in range(len(os.listdir(path))):
                    print("{}: {}".format(x,os.listdir(path)[x]))
                choice = int(input())
                file = "WordLists/" + os.listdir(path)[choice]
                grid.findListedWords(file)
            except:
                print("File Not Found")
    else:
        print("Make a grid first. Use new command")
    