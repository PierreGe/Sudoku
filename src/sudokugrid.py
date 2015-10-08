
import copy
import random
import itertools

class SudokuGrid():
    def __init__(self, grid):
        self._digits = '123456789'
        self._letters = 'ABCDEFGHI'
        self._squares = (('ABC', 'DEF', 'GHI'), ('123', '456', '789'))
        self._conflictPositionDict = dict((s, set(sum(dict((s, [e for e in
                                                                [SudokuGrid.combination(self._letters, d) for d in
                                                                 self._digits] + [
                                                                    SudokuGrid.combination(l, self._digits) for l in
                                                                    self._letters] + [SudokuGrid.combination(rs, cs) for
                                                                                      rs in self._squares[0] for cs in
                                                                                      self._squares[1]] if s in e]) for
                                                           s in [l + d for l in self._letters for d in self._digits])[
                                                          s], [])) - set([s])) for s in
                                          [l + d for l in self._letters for d in self._digits])
        self._initialGrid = {}
        self._grid = {}
        self.parse(grid)

    @staticmethod
    def combination(letter, digit):
        return [l + d for l in letter for d in digit]

    def getGrid(self):
        return self._grid

    def getFirstEmpty(self):
        for pos in SudokuGrid.combination(self._letters, self._digits):
            if pos not in self._grid:
                return pos

    def getAllEmpty(self):
        l = []
        for pos in SudokuGrid.combination(self._letters, self._digits):
            if pos not in self._grid:
                l.append(pos)
        return l if len(l)>0 else None

    def randomFill(self):
        self._grid = copy.deepcopy(self._initialGrid)
        for l in self._squares[0]:
            for d in self._squares[1]:
                dig = list(self._digits)
                random.shuffle(dig)
                for s in SudokuGrid.combination(l,d):
                    if s in self._grid:
                        dig.remove(self._grid[s])
                for s in SudokuGrid.combination(l,d):
                     if s not in self._grid:
                         self._grid[s] = dig.pop()

    def getConflictCaseNumberFilled(self,posTarget):
        res = 0
        for pos in self._conflictPositionDict[posTarget]:
            if pos in self._grid:
                res+=1
        return res


    def switchConflict(self,square):
        indexlist = SudokuGrid.combination(self._squares[0][(square-1)%3],self._squares[1][(square-1)/3])
        conflitList = []
        for i in indexlist:
            if i not in self._initialGrid:
                if self.isConflict(i,self._grid[i]):
                    conflitList.append(i)
        if len(conflitList) > 1:
            best1 = conflitList[0]
            best2 = conflitList[1]
            initialNbr = self.getConflictNumber()
            ini = initialNbr
            for el1,el2 in list(itertools.permutations(conflitList,2)):
                if el1 != el2:
                    self._grid[el1], self._grid[el2] = self._grid[el2], self._grid[el1]
                    newNbr = self.getConflictNumber()
                    if newNbr < initialNbr:
                        initialNbr = newNbr
                        best1 = el1
                        best2 = el2
                    else:
                        self._grid[el1], self._grid[el2] = self._grid[el2], self._grid[el1]

            #print(ini, initialNbr)


            #j = 20
            #while j != 0:
            #    random.shuffle(conflitList)
             #   el1 = conflitList[0]
              #  el2 = conflitList[1]
                #self._grid[el1], self._grid[el2] = self._grid[el2], self._grid[el1]
               # if self.getConflictNumber() < initialNbr:
                ##    break
                #self._grid[el1], self._grid[el2] = self._grid[el2], self._grid[el1]
                #j-=1



        return indexlist

    def getBestEmpty(self):
        min = 9
        minpos = None
        l = []
        for pos in SudokuGrid.combination(self._letters, self._digits):
            if pos not in self._grid:
                val = self.possibleValue(pos)
                if len(val) < min :
                    min = len(val)
                    minpos = pos
                    l = [minpos]
                elif len(val) == min:
                    l.append(pos)
                if min == 1:
                    return l
        if minpos == None: # TODO ne devrait pas faire ca
            minpos = self.getFirstEmpty()
        return l

    def setOnGrid(self, position, chiffre):
        self._grid[position] = chiffre

    def parse(self, grid):
        """ Parse une string de 81 caractere contenant un sudoku"""
        self._grid = {}
        for irow, row in enumerate(self._letters):
            for icol, col in enumerate(self._digits):
                if grid[irow * 9 + icol] != '0' and grid[irow * 9 + icol] != '.':
                    self._grid[row + col] = grid[irow * 9 + icol]
        self._initialGrid = copy.deepcopy(self._grid)

    def isConflict(self, position, chiffre):
        """
        On regarde si ca fait un conflit de mettre 8 en C7 par exemple
        :param position: la position
        :param chiffre: le chiffre
        :return: True or False
            Note: On aurrait pu utiliser possibleValue.
        """
        for conflictPos in self._conflictPositionDict[position]:
            if conflictPos in self._grid and self._grid[conflictPos] == chiffre:
                return True
        return False

    def possibleValue(self, position):
        """
        :param position: une position sur la grille genre C5
        :return: les valeurs placables en C5
        """
        value = list(self._digits)
        for conflictPos in self._conflictPositionDict[position]:
            if conflictPos in self._grid:
                if self._grid[conflictPos] in value:
                    value.remove(self._grid[conflictPos])
        return value

    def isFinished(self):
        if len(self._grid) < 81:
            return False
        else:
            for irow, row in enumerate(self._letters):
                for icol, col in enumerate(self._digits):
                    for conflictPos in self._conflictPositionDict[row + col]:
                        if conflictPos not in self._grid:
                            return False
                        if self._grid[conflictPos] == self._grid[row + col]:
                            return False
        return True

    def getConflictNumber(self):
        n = 0
        for irow, row in enumerate(self._letters):
            for icol, col in enumerate(self._digits):
                n += self.isConflict(row+col, self._grid[row+col])
        return n

    def __str__(self):
        string = ""
        for irow, row in enumerate(self._letters):
            for icol, col in enumerate(self._digits):
                if row + col in self._grid:
                    string += self._grid[row + col] + " "
                else:
                    string += ". "
                if icol != 0 and (icol + 1) % 3 == 0:
                    string += "|"
            string += "\n"
            if irow != 0 and (irow + 1) % 3 == 0:
                string += "-" * 21 + "\n"
        return string


if __name__ == '__main__':
    s = SudokuGrid('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    s.randomFill()
    print s.switchConflict(6)
    print s
    print s.getConflictNumber()
    print s.possibleValue("A1")
    print s.isFinished()
    s = SudokuGrid('483921657967345821251876493548132976729564138136798245372689514814253769695417382')
    print s.isFinished()
