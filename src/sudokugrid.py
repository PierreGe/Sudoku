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
        return l

    def getBestEmpty(self):
        min = 9
        minpos = None
        for pos in SudokuGrid.combination(self._letters, self._digits):
            if pos not in self._grid:
                val = self.possibleValue(pos)
                if len(val) == 1:
                    return pos
                if len(val) < min and len(val) > 1:
                    min = len(val)
                    minpos = pos
        return minpos

    def setOnGrid(self, position, chiffre):
        self._grid[position] = chiffre

    def parse(self, grid):
        """ Parse une string de 81 caractere contenant un sudoku"""
        self._grid = {}
        for irow, row in enumerate(self._letters):
            for icol, col in enumerate(self._digits):
                if grid[irow * 9 + icol] != '0' and grid[irow * 9 + icol] != '.':
                    self._grid[row + col] = grid[irow * 9 + icol]

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
    print s
    print s.possibleValue("A1")
    print s.isFinished()
    s = SudokuGrid('483921657967345821251876493548132976729564138136798245372689514814253769695417382')
    print s.isFinished()
