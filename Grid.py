

class Grid:

    def createGrid(self,file):
        M = []
        f = open(file,"r")
        for line in f.readlines():
            if line[-1] == '\n':
                line = line[:-1]
            M.append(line)
        f.close()
        return M
            
    def __init__(self,file):
        self.file = file
        self.grid = self.createGrid(file)
        self.paths = [[-1,0],[1,0],[0,1],[0,-1],[-1,1],[-1,-1],[1,1],[1,-1]]

    def printGrid(self):
        for row in self.grid:
            print(*row)

    def findListedWords(self,file):
        listOfCoords = []
        with open(file) as f:
            for line in f.readlines():
                listOfCoords += self.findWord(line.strip('\n'))
        f.close()
        self.printSelected(listOfCoords)

    def findWord(self,word):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == word[0]:
                    for d in self.paths:
                        i,j = d
                        if (row + i) < len(self.grid) and (row + i) >= 0 and (col + j) >= 0 and (col + j) < len(self.grid[0]):
                            if self.grid[row+i][col+j] == word[1]:
                                result = self.recursiveCheck(row+i,col+j,word,1,d)
                                if False not in result:
                                    # self.printSelected([[row,col]] + result)
                                    return self.printSelected([[row,col]] + result)
        return False

    def recursiveCheck(self,row,col,word,I,path):
        if row == len(self.grid) or row < 0 or col == len(self.grid[0]) or col < 0:
            return [False]
        if self.grid[row][col] != word[I]:
            return [False]
        elif I == len(word) -1 and self.grid[row][col] == word[I]:
            return [[row,col]]
        else:
            i,j = path
            return [[row,col]] + self.recursiveCheck(row+i,col+j,word,I+1,path)

    def printSelected(self,matrix):
        matrixToPrint = []
        for row in range(len(self.grid)):
            line = [self.grid[row][col] if [row,col] in matrix else "*" for col in range(len(self.grid[0]))]
            matrixToPrint.append(line)
        for line in matrixToPrint:
            print(*line)