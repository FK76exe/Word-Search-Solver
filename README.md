# Word-Search-Solver

<h4> Note: to use, run the main.py file </h4>

# Commands:

<b> New: </b> Creates a new grid (or overwrites pre-existing grid) to search words for. After input, you will be shown all files in the Grids folder with
an mapped to an integer. You would then have to choose which file to pick by entering the integer assigned to it. The program will raise an error if a non-integer was entered or
an integer that was not assigned a file.<br>

Note: The file containing the grid must have a rectangular grid (all rows must be equal length), or an error would arise. <br>

<b> Print: </b> Prints the unsolved grid. If the grid has not been created yet, an error would arise.

<b> Find [word]: </b> Searches for the given word in the grid. If word is found, the program would return a grid with only the letters forming the found word present. Otherwise,
It will state that the word cannot be found in the grid.

<b> Findall: </b> Searches the grid for words found in a text file. Like new, the program prompts user to select an integer assigned to a file in the WordLists folder.
If a non-integer or an invalid integer was selected, an error will be raised. Otherwise, the program will output the grid with all findable words, and lists any words that have
not been found.

<b> Quit: </b> Exits program <br>


Note: commands are not case-sensitive. However, the word grid is.
