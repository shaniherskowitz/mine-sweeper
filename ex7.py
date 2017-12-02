"""
student name: shani herskowitz
student ID: 321658387
Course Exercise Group: 01
Exercise name: ex7.py
"""
import argparse
import random
import turtle

def RmysteryFunc(a, n):
    """
    prints the bianery value of a entered
    runs recursively until a = 0
    args: a,n numbers nned to be bigger then 1
    :return none
    """
    if a == 0:
        return
    print a % n
    return RmysteryFunc(a/n, n)


class Sierpinski(object):

    def __init__(self):
        """
        opens turtle window
        :return: none
        """

        self.window = turtle.Screen()
        self.sierpinski_turtle = turtle.Turtle()

    def draw_sierpinski(self, length, depth):
        """
        draws a sierpinski tree
        :param length: the length of the base of the all tree
        :param depth: the depth of the tree recursion
        :return:
        """
        if depth == 0:
            for i in range(0, 3):
                self.sierpinski_turtle.fd(length)
                self.sierpinski_turtle.left(120)
        else:
            self.draw_sierpinski(length / 2, depth - 1)
            self.sierpinski_turtle.fd(length / 2)
            self.draw_sierpinski(length / 2, depth - 1)
            self.sierpinski_turtle.back(length / 2)
            self.sierpinski_turtle.left(60)
            self.sierpinski_turtle.fd(length / 2)
            self.sierpinski_turtle.right(60)
            self.draw_sierpinski(length / 2, depth - 1)
            self.sierpinski_turtle.left(60)
            self.sierpinski_turtle.back(length / 2)
            self.sierpinski_turtle.right(60)
        pass

    def finish_draw(self):
        """
        closes turtle window
        :return: none
        """
        self.window.bye()

    def save_draw(self, length, depth):
        """
        save tringle drawing
        :param length: the length of the base of the all tree
        :param depth: the depth of the tree recursion
         :return:
        """
        self.sierpinski_turtle.hideturtle()
        nameSav = ("sierpinski_%d_%d" % (length, depth)) + ".svg"
        ts = turtle.Turtle().getscreen().getcanvas()
        ts.postscript(file=nameSav)


class GameStatus(object):
    """Enum of possible Game statuses."""
    __init__ = None
    NotStarted, InProgress, Win, Lose = range(4)


class BoardCell(object):
    """
    Represents a cell in the minesweeper board game and is current status in the game

    """
    def __init__(self):
        """
        Initializes a board cell with no neighboring mines and status is hidden

        Args:
            None

        Returns:
            None (alters self)
        """
        self.cellStatus = 'H'
        self.cellVal = 0
        pass

    def is_mine(self):
        """
        returns true if this cell contains a mine false otherwise

        Args:
            None

        Returns:
            true if this cell contains a mine false otherwise
        """
        if self.cellVal == '*':
            return True
        else:
            return False
        pass

    def is_hidden(self):
        """
        returns true if this cell is hidden false otherwise

        Args:
            None

        Returns:
            true if this cell is hidden false otherwise
        """
        if self.cellStatus == 'H':
            return True
        else:
            return False
        pass

    def get_cell_value(self):
        """
        returns the number of adjacent mines

        Args:
            None

        Returns:
            the number of adjacent mines in int or the charcter '*' if this cell is a mine
        """

        if self.cellVal == '*':
            return '*'
        else:
            return self.cellVal

        pass

    def uncover_cell(self):
        """
        uncovers this cell. when a cell is uncovered then its status is the value of the mines near it or * if the
        cell is a mine
        Args:
            None

        Returns:
            None (alters self)

        """
        self.cellStatus = self.cellVal

        pass

    def update_cell_value(self, cellValue):
        """
        updates the value of the how many neighboring mines this cell has

        Args:
            numOfNearMine - the new number of the how many neighboring mines this cell has

        Returns:
            None (alters self)
        """
        self.cellVal = cellValue
        pass

    def add_one_to_cell_value(self):
        """
        adds one to the number of near mine

        Args:
            None

        Returns:
            None (alters self)
        """
        self.cellVal += 1
        pass

    def set_has_mine(self):
        """
        changes this cell to a cell with a mine in it

        Args:
           None

        Returns:
            None (alters self)
        """
        self.cellVal = '*'
        pass


class Board(object):
    """Represents a board of minesweeper game and its current progress."""

    def __init__(self, rows, columns):
        """Initializes an empty hidden board.

        The board will be in the specified dimensions, without mines in it,
        and all of its cells are in hidden state.

        Args:
            rows: the number of rows in the board
            columns: the number of columns in the board

        Returns:
            None (alters self)
        """
        self.numRows = rows
        self.numColumns = columns
        # starts a board with row*col board cells
        self.board = [[BoardCell() for _ in range(columns)] for _ in range(rows)]


    def put_mines(self, mines, seed=None):
        """Randomly scatter the requested number of mines on the board.

        At the beggining, all cells on the board are hidden and with no mines
        at any of them. This method scatters the requested number of mines
        throughout the board randomly, only if the board is in the beginning
        state (as described here). A cell can host only one mine.
        This method not only scatters the mines on the board, but also updates
        the cells around it (so they will hold the right digit).

        Args:
            mines: the number of mines to scatter
            seed: the seed to give the random function. Default value None

        Returns:
            None (alters self)

        """
        listOfCellsIndex = [(numRow, numCol) for numRow in range(self.numRows) for numCol in range(self.numColumns)]
        # randomly choosing cells in the board to place mines in
        random.seed(seed)
        listOfMineCells = random.sample(listOfCellsIndex, mines)
        # sets mines into random board cells then updates cells around
        for x in listOfMineCells:
            self.board[x[0]][x[1]].set_has_mine()
            self.CheckAround(x[0], x[1])


    def CheckAround(self, i, j):
        """
        updates all cells around mine by adding one to the value
        of each(except for mine cells around)
        args: i repersents the row of the mine
              j repersents the colunm of the mine
        :return: none, changes self
        """
        # if mine is at the first spot in matrix only updates 3 cells arounf
        if i == 0 and j == 0:
            x = i
            y = j+1
            if y < self.numColumns:
                if not self.board[x][y].is_mine():
                    self.board[x][y].add_one_to_cell_value()
                if x+1 < self.numRows:
                    if not self.board[x+1][y].is_mine():
                        self.board[x+1][y].add_one_to_cell_value()
                    if not self.board[x+1][y-1].is_mine():
                        self.board[x+1][y-1].add_one_to_cell_value()
            return

        if j == 0:
            self.ifCol0(i, j)
            return

        x = i-1
        y = j-1
        while -1 < x < i+2 and x < self.numRows and -1 < y < j+2 and y < self.numColumns:
            if not self.board[x][y].is_mine():
                self.board[x][y].add_one_to_cell_value()
            y += 1

        x = i
        y = (j - 1)
        while -1 < x < i+2 and x < self.numRows and -1 < y < j+2 and y < self.numColumns:
            if not self.board[x][y].is_mine():
                self.board[x][y].add_one_to_cell_value()
            y += 1

        x = i + 1
        y = j - 1
        while -1 < x < i+2 and x < self.numRows and -1 < y < j+2 and y < self.numColumns:
            if not self.board[x][y].is_mine():
                self.board[x][y].add_one_to_cell_value()
            y += 1

    def ifCol0(self, i, j):
        """
        when the coulmn is 0 checkes around the cells
        in a diffrent order
        args: i repersents the row of the mine
              j repersents the colunm of the mine
        :return: none, changes self
        """

        x = i - 1
        y = j
        while -1 < x < i + 2 and x < self.numRows and -1 < y < j + 2 and y < self.numColumns:
            if not self.board[x][y].is_mine():
                self.board[x][y].add_one_to_cell_value()
            y += 1

        x = i
        y = j + 1
        while -1 < x < i + 2 and x < self.numRows and -1 < y < j + 2 and y < self.numColumns:
            if not self.board[x][y].is_mine():
                self.board[x][y].add_one_to_cell_value()
            break

        x = i + 1
        y = j
        while -1 < x < i + 2 and x < self.numRows and -1 < y < j + 2 and y < self.numColumns:
            if not self.board[x][y].is_mine():
                self.board[x][y].add_one_to_cell_value()
            y += 1

    def print_board(self):
        """prints the board according to the game format
            DO NOT CHANGE ANYTHING IN THIS FUNCTION!!!!!!!
        Args:
            None
        Returns:
            None
        """
        # creates the printing format
        printFormatString = "%-2s " * self.numColumns
        printFormatString += "%-2s"
        # prints the first line of the board which is the line containing the indexes of the columns
        argList = [" "]
        argList.extend([str(i) for i in range(self.numColumns)])
        print printFormatString % tuple(argList)
        # goes over the board rows and prints each one
        for i in range(self.numRows):
            argList = [str(i)]
            for j in range(self.numColumns):
                if self.board[i][j].is_hidden():
                    argList.append("H")
                else:
                    argList.append(str(self.board[i][j].get_cell_value()))
            print printFormatString % tuple(argList)

    def load_board(self, lines):
        """Loads a board from a sequence of lines.

        This method is used to load a saved board from a sequence of strings
        (that usually represent lines). Each line represents a row in the table
        in the following format:
            XY XY XY ... XY
        Where X is one of the characters: 0-8, * and Y is one of letters: H, S.
        0-8 = number of adjusting mines (0 is an empty, mine-free cell)
        * = represents a mine in this cell
        H = this cell is hidden

        The lines can have multiple whitespace of any kind before and after the
        lines of cells, but between each XY pair there is exactly one space.
        Empty or whitespace-only lines are possible between valid lines, or after/before them.
        It is safe to assume that the values are correct (the number represents the number of mines around
        a given cell) and the number of mines is also legal.

        Note that this method doesn't get the first two rows of the file (the
        dimensions) on purpose - they are handled in __init__.

        Args:
            lines: a sequence (list or tuple) of lines with the above restrictions

        Returns:
            None (alters self)
        """
        x = 0
        y = 0
        new = []
        count = 0
        for line in lines[2:]:
            new.extend(line.strip().split())
        while x < self.numRows and y < self.numColumns:
            for cell in new:
                # if cell is not a mine converts value to int
                if cell[0] != '*':
                    num = int(cell[0])
                    self.board[x][y].cellVal = num
                else:
                    count+= 1
                    self.board[x][y].cellVal = cell[0]
                self.board[x][y].cellStatus = cell[1]
                y += 1
                if y == self.numColumns:
                    y = 0
                    x += 1
        # after loading checks if the dimensions given are in right range
        if count > self.numRows*self.numColumns-1:
            print "Illegal board"
            quit()
        pass
    def get_value(self, row, column):
        """Returns the value of the cell at the given indices.

        The return value is a string of one character, out of 0-8 + '*'.

        Args:
            row: row index (integer)
            column: column index (integer)

        Returns:
            If the cell is empty and has no mines around it, return '0'.
            If it has X mines around it (and none in it), return 'X' (digit
            character between 1-8).
            If it has a mine in it return '*'.

        """
        return self.board[row][column].cellVal

        pass

    def is_hidden(self, row, column):
        """Returns if the given cell is in hidden or uncovered state.

        Args:
            row: row index (integer)
            column: column index (integer)

        Returns:
            'H' if the cell is hidden, or 'S' if it's uncovered (can be seen).
        """

        return self.board[row][column].cellStatus
        pass

    def uncover(self, row, column):
        """Changes the status of a cell from hidden to seen.

        Args:
            row: row index (integer)
            column: column index (integer)

        Returns:
            None (alters self)
        """
        self.board[row][column].uncover_cell()

        pass

class Game(object):
    """Handles a game of minesweeper by supplying UI to Board object."""

    def __init__(self, board):
        """Initializes a Game object with the given Board object.

        The Board object can be a board in any given status or stage.

        Args:
            board: a Board object to continue (or start) playing.

        Returns:
            None (alters self)
        """
        self.game = board
        pass

    def get_status(self):
        """Returns the current status of the game.

        The current status of the game is as followed:
            NotStarted: if all cells are hidden.
            InProgress: if some cells are hidden and some are uncovered, and
            no cell with a mine is uncovered.
            Lose: a cell with mine is uncovered.
            Win: All non-mine cells are uncovered, and all mine cells are
            covered.

        Returns:
            one of GameStatus values (doesn't alters self)

        """
        count = 0
        countMines = 0
        countHidden = 0

        listOfCells = [(numRow, numCol) for numRow in range(self.game.numRows)
                       for numCol in range(self.game.numColumns)]
        for i in listOfCells:
            if self.game.is_hidden(i[0], i[1]) != 'H':
                # counts the num of non hidden cells
                count += 1
                if self.game.get_value(i[0], i[1]) == '*':
                    return GameStatus.Lose
            if self.game.is_hidden(i[0], i[1]) == 'H':
                # counts hidden cells
                countHidden += 1
                if self.game.get_value(i[0], i[1]) == '*':
                    # counts mines
                    countMines += 1
        # uses diffrent counts to return correct game status
        if count == 0:
            return GameStatus.NotStarted
        elif countHidden == countMines:
            return GameStatus.Win
        elif count != 0:
            return GameStatus.InProgress
        pass

    def make_move(self, row, column):
        """Makes a move by uncovering the given cell and unrippling it's area.

        The move flow is as following:
        1. Uncover the cell
        2. If the cell is a mine - return
        3. if the cell is not a mine, ripple (if value = 0) and uncover all
            adjacent cells, and recursively on this cells if needed (if they are empty cells)

        Args:
            row: row index (integer)
            column: column index (integer)

        Returns:
            the cell's value.
        """

        if self.game.get_value(row, column) == '*':
            return '*'
        self.game.uncover(row, column)

        if self.game.get_value(row, column) == 0:
            # makes lists of row and col from board and sub lists from
            # the user to ripple by recursion
            cellRow = []
            cellCol = []
            listOfRowsIndex = [numRow for numRow in range(self.game.numRows)]
            listOfColsIndex = [numCol for numCol in range(self.game.numColumns)]
            if row-1 in listOfRowsIndex:
                cellRow.append(row-1)
            if row + 1 in listOfRowsIndex:
                cellRow.append(row + 1)
            if column -1 in listOfColsIndex:
                cellCol.append(column-1)
            if column + 1 in listOfColsIndex:
                cellCol.append(column + 1)
            if row in listOfRowsIndex:
                cellRow.append(row)
            if column in listOfColsIndex:
                cellCol.append(column)
            # goes over sub lists and calls func to ripple
            for i in cellRow:
                for j in cellCol:
                    if self.game.is_hidden(int(i), int(j)):
                        self.make_move(int(i), int(j))

        return self.game.get_value(row, column)
    def run(self):
        """Runs the game loop.

        At each turn, prints the following:
            current state of the board
            game status
            available actions
        And then wait for input and act accordingly.
        More details are in the project's description.

        Returns:
            None
        """
        # runs until user enters 1
        while True:
            self.game.print_board()
            # prints game status
            if self.get_status() == 0:
                print "Game status: NotStarted"
            elif self.get_status() == 1:
                print "Game status: InProgress"
            elif self.get_status() == 2:
                print "Game status: Win"
                print "Available actions: (1) Exit"
            elif self.get_status() == 3:
                print "Game status: Lose"
                print "Available actions: (1) Exit"
            if self.get_status() != 3 and self.get_status() != 2:
                print "Available actions: (1) Exit | (2) Move"
            print "Enter selection:"
            userInput = raw_input()
            # if user enters 1 exits game
            if userInput == '1':
                print "Goodbye :)"
                return
            elif userInput != 1 and self.get_status() == 3 or self.get_status() == 2:
                print "Illegal choice"
            elif userInput == '2':
                # gets row and col from user to make move in game
                rows, cols = raw_input("Enter row then column (space separated): \n").split()
                rows, cols = [int(rows), int(cols)]
                if rows > self.game.numRows-1 or cols > self.game.numColumns-1 \
                        or self.game.is_hidden(rows, cols) != 'H':
                    print "Illegal move values"
                else:
                    self.game.uncover(rows, cols)
                    self.make_move(rows, cols)
            else:
                print "Illegal choice"
        pass


def main():
    """Starts the game by parsing the arguments and initializing.
    Act according to the exercise explanation

    Regarding mine swiper:
    If an input file argument was given, the file is loaded (even if other
    legal command line argument were given).

    If input file wasn't given, create a board with the rows/columns/mines

    In case both an input file was given and other parameters, ignore the
    others and use only the input file.
    For example, in case we get "-i sample -r 2 -c 2" just use
    the input file and ignore the rest (even if there are missing parameters).

    Returns:
        None

    """
    #adds arguments used in the program
    parser = argparse.ArgumentParser(description="Process game arguments")
    parser.add_argument('-p', action="store", dest="pick", type=int)
    parser.add_argument('-a', action="store", dest="aNum", type=int)
    parser.add_argument('-n', action="store", dest="nNum", type=int)
    parser.add_argument('-l', action="store", dest="lengnth", type=float)
    parser.add_argument('-d', action="store", dest="depth", type=float)
    parser.add_argument('-r', action="store", dest="row", type=int)
    parser.add_argument('-c', action="store", dest="col", type=int)
    parser.add_argument('-m', action="store", dest="mine", type=int)
    parser.add_argument('-i', dest="INPUT", type=argparse.FileType("r"))
    parser.add_argument('-s', action="store", dest="seed", type=float)
    args = parser.parse_args()

    # based on commandline input compiles diffrent functions and runs
    if args.pick == 1:
        RmysteryFunc(args.aNum, args.nNum)
    elif args.pick == 2:
        s = Sierpinski()
        s.draw_sierpinski(args.lengnth, args.depth)
        s.save_draw(args.lengnth, args.depth)
        s.finish_draw()
    elif args.pick == 3:
        # opens board file and loads board
        if args.INPUT:
            lines = [line.strip() for line in args.INPUT if line.strip()]
            # checks board row and col to see if in range
            if int(lines[0]) > 20 and int(lines[1]) > 50 or int(lines[0]) < 1 and int(lines[1]) < 2:
                print "Illegal board"
                return
            fileBoard = Board(int(lines[0]), int(lines[1]))
            fileBoard.load_board(lines)
            gameFile = Game(fileBoard)
            gameFile.run()
        else:
            # checks board row and col to see if in range
            if args.mine > args.row * args.col-1 or args.row > 20 or\
                            args.col > 50 or args.row < 1 or args.col < 2 or args.mine < 0:
                print "Illegal board"
                return
            b = Board(args.row, args.col)
            g = Game(b)
            b.__init__(args.row, args.col)
            b.put_mines(args.mine, args.seed)
            g.run()

    pass
# runs main
if __name__ == '__main__':
    main()

