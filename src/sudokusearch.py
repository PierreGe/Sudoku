



class SudokuGrid():
    def __init__(self, grid):

        def combination(letter, digit):
            return [l+d for l in letter for d in digit]
        self._digits = '123456789'
        self._letters = 'ABCDEFGHI'
        self._squares = (('ABC', 'DEF', 'GHI'),('123', '456', '789'))
        self._conflictPositionDict = dict((s, set(sum(dict((s, [e for e in [combination(self._letters, d) for d in self._digits] + [combination(l, self._digits) for l in self._letters] + [combination(rs, cs) for rs in self._squares[0] for cs in self._squares[1]] if s in e]) for s in [l+d for l in self._letters for d in self._digits])[s],[]))-set([s])) for s in [l+d for l in self._letters for d in self._digits])
        self._grid = {}
        self.parse(grid)

    def parse(self,grid):
        """ Parse une string de 81 caractere contenant un sudoku"""
        self._grid = {}
        for irow,row in enumerate(self._letters):
            for icol,col in enumerate(self._digits):
                if grid[irow*9 + icol] != '0' and grid[irow*9 + icol] != '.':
                    self._grid[row+col] = grid[irow*9 + icol]

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

    def possibleValue(self,position):
        """
        :param position: une position sur la grille genre C5
        :return: les valeurs placables en C5
        """
        value = list(self._digits)
        for conflictPos in self._conflictPositionDict[position]:
            if conflictPos in self._grid:
                value.remove(self._grid[conflictPos])
        return value

    def __str__(self):
        string = ""
        for irow,row in enumerate(self._letters):
            for icol,col in enumerate(self._digits):
                if row+col in self._grid:
                    string += self._grid[row+col] + " "
                else:
                    string += ". "
                if icol!= 0 and (icol+1)%3 ==0:
                    string += "|"
            string += "\n"
            if irow!= 0 and (irow+1)%3 ==0:
                string += "-"*21 + "\n"
        return string



if __name__ == '__main__':
    s = SudokuGrid('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    print s
    print s.possibleValue("A1")