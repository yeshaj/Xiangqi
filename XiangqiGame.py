class Pieces:
# Each piece is assigned a number for the board area, when putting in the specific piece in the initial position
    Empty = 0
    King = 1
    Advisor = 2
    Elephant = 3
    Horse = 4
    Chariot = 5
    Cannon = 6
    Pawn = 7

# this is a string to inform that each letter and piece should equal each other
    @staticmethod
    def fromString(s):
        if s == 'G':
            return Pieces.King
        elif s == 'A':
            return Pieces.Advisor
        elif s == 'E':
            return Pieces.Elephant
        elif s == 'H':
            return Pieces.Horse
        elif s == 'R':
            return Pieces.Chariot
        elif s == 'C':
            return Pieces.Cannon
        elif s == 'S':
            return Pieces.Pawn
    @staticmethod
    def toString(s):
        if s == Pieces.King:
            return 'G'
        elif s == Pieces.Advisor:
            return 'A'
        elif s == Pieces.Elephant:
            return 'E'
        elif s == Pieces.Horse:
            return 'H'
        elif s == Pieces.Chariot:
            return 'R'
        elif s == Pieces.Cannon:
            return 'C'
        elif s == Pieces.Pawn:
            return 'S'
        else:
            return " "

# in order to make the board and pieces work, one color has to be negative and the other will be positive
class Color:
    Red = 1
    Black = -1

    @staticmethod
    def toString(c):
        if c == 1:
            return 'r'
        else:
            return 'b'

# If the move cannot work, there will be a wrong moves message that will take place
class WrongMove(Exception):
    def __init__(self, m):
        self.msg = m
    def __str__(self):
        return self.msg

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
    # every function is later used in the Board class when giving the different positions
        return str(chr(self.x + ord('A') - 1)) + str(self.y)
    def isEqual(self, pos):
        return self.x == pos.x and self.y == pos.y
    def sameRow(self, pos):
        return self.y == pos.y
    def sameColumn(self, pos):
        return self.x == pos.x
    def sameDiagonal(self, pos):
        return abs(self.y - pos.y) == abs(self.x - pos.x)
    # depending on which pieces can be in the castle
    def inCastle(self, color):
        if self.x <= 6 and self.x >= 4:
            if (color == Color.Red and self.y <= 3) or (color == Color.Black and self.y >= 8):
                return True
        return False
    def onSide(self, color):
        if (color == Color.Red and self.y <= 5) or (color == Color.Black and self.y >= 6):
            return True
        return False
    def distance(self, pos):
        return max(abs(self.x - pos.x), abs(self.y - pos.y))
    def getElephantBlock(self, dst):
        y = (self.y + dst.y) / 2
        x = (self.x + dst.x) / 2
        return Position(x, y)
    def horseMove(self, dst):
        if self.distance(dst) == 2:
            if abs(self.x - dst.x) == 1 or abs(self.y - dst.y) == 1:
                return True
        return False
    def getHorseBlock(self, dst):
        if abs(self.y - dst.y) == 1:
            if self.x > dst.x:
                return Position(self.x - 1, self.y)
            else:
                return Position(self.x + 1, self.y)
        elif abs(self.x - dst.x) == 1:
            if self.y > dst.y:
                return Position(self.x, self.y - 1)
            else:
                return Position(self.x, self.y + 1)


class Board:
    def __init__(self, zero=False):
        self.board = [
            # as mentioned earlier, the different colors allows the board to be set up with the specific colors on each side
            # without the negative, both side would be one color (in this case red)
                    [5, 4, 3, 2, 1, 2, 3, 4, 5],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 6, 0, 0, 0, 0, 0, 6, 0],
                    [7, 0, 7, 0, 7, 0, 7, 0, 7],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [-7, 0, -7, 0, -7, 0, -7, 0, -7],
                    [0, -6, 0, 0, 0, 0, 0, -6, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [-5, -4, -3, -2, -1, -2, -3, -4, -5]]

        if zero:
            return
        self.pieces = {}
        for i in range(10):
            for j in range(9):
                p = self.board[i][j]
                if p != Pieces.Empty:
                    self.pieces[(i, j)] = p
                if p == Pieces.King:
                    self.redking = Position(j + 1, i + 1)
                elif p == -Pieces.King:
                    self.blackking = Position(j + 1, i + 1)


    def __str__(self):
        '''self.board = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, 0]]'''
}

# the board must be 9 x 10 otherwise return False
def equals(self, other):
    for i in range(10):
        for j in range(9):
            if other.board[i][j] != self.board[i][j]:
                return False
        return True


def getPieces(self, pos):
    return self.board[pos.y - 1][pos.x - 1]


def piecesBetween(self, src, dst):
    counter = 0
    if src.x == dst.x:
        for i in range(min(src.y, dst.y) + 1, max(src.y, dst.y)):
            if self.getPieces(Position(src.x, i)) != Pieces.Empty:
                counter += 1
    if src.y == dst.y:
        for i in range(min(src.x, dst.x) + 1, max(src.x, dst.x)):
            if self.getPieces(Position(i, src.y)) != Pieces.Empty:
                counter += 1
    return counter


def tryMovePieces(self, color, src, dst):
    piece = self.getPieces(src)

# these first 3 are for incorrect movements and the different messages for each type of error
    if piece * color < 0:
        raise WrongMove("This is the wrong color")

    if piece == 0:
        raise WrongMove("There is no piece")

    if self.getPieces(dst) * color > 0:
        raise WrongMove("You are trying to capture your own piece")
# Every piece has a specific way they cannot move, whether it's outside the castle or going backwards
# This will create an error message for each type of problem so that the user does not make the problem again
    piecemove = abs(piece)
    if piecemove == Pieces.King:
        if not (src.sameRow(dst) or src.sameColumn(dst)) or src.distance(dst) > 1:
            raise WrongMove("The movement of the king is incorrect")
    if not dst.inCastle(color):
        raise WrongMove("King has moved out of the castle")
    if piecemove == Pieces.Advisor:
        if not src.sameDiagonal(dst) or src.distance(dst) > 1:
            raise WrongMove("The movement of the advisor is incorrect")
    if not dst.inCastle(color):
        raise WrongMove("Advisor has moved out of castle")
    if piecemove == Pieces.Elephant:
        if not src.sameDiagonal(dst) or src.distance(dst) != 2:
            raise WrongMove("The movement of the elephant is incorrect")
    if not dst.onSide(color):
        raise WrongMove("Elephant has moved out of castle")
    if self.getPieces(src.getElephantBlock(dst)) != 0:
        raise WrongMove("Elephant is blocked")
    if piecemove == Pieces.Horse:
        if not src.horseMove(dst):
            raise WrongMove("The movement of the horse is incorrect")
    if self.getPieces(src.getHorseBlock(dst)) != 0:
        raise WrongMove("Horse is blocked")
    if piecemove == Pieces.Chariot:
        if not (src.sameRow(dst) or src.sameColumn(dst)):
            raise WrongMove("The movement of the chariot is incorrect")
    if self.piecesBetween(src, dst) > 0:
        raise WrongMove("Chariot skipping over pieces")
    if piecemove == Pieces.Cannon:
        if not (src.sameRow(dst) or src.sameColumn(dst)):
            raise WrongMove("Chariot movement direction is incorrect")
    if self.getPieces(dst) != Pieces.Empty:
        if self.piecesBetween(src, dst) != 1:
            raise WrongMove("Cannon can't kill without skipping over a piece")
    else:
        if self.piecesBetween(src, dst) > 0:
            raise WrongMove("Cannon cannot move skipping over pieces")
    if piecemove == Pieces.Pawn:
        if not (src.sameRow(dst) or src.sameColumn(dst)) or src.distance(dst) > 1:
            raise WrongMove("Pawn movement direction is incorrect")
    if (color == Color.Red and dst.y < src.y) or (color == Color.Black and dst.y > src.y):
        raise WrongMove("Pawn cannot move backwards")
    if src.y == dst.y and src.onSide(color):
        raise WrongMove("Pawn cannot move sideways yet")

    return True


def movePieces(self, src, dst):
    p = self.getPieces(src)
    if self.board[dst.y - 1][dst.x - 1] == Piece.King:
        self.redking = None
    elif self.board[dst.y - 1][dst.x - 1] == -Piece.King:
        self.blackking = None
    self.board[dst.y - 1][dst.x - 1] = p
    self.board[src.y - 1][src.x - 1] = Piece.Empty
    del self.pieces[(src.y - 1, src.x - 1)]
    pos = (dst.y - 1, dst.x - 1)
    self.pieces[pos] = p
    if p == Pieces.King:
        self.redking = dst
    elif p == -Pieces.King:
        self.blackking = dst

# print the piece to where they should go with the write letter from the string
def printMove(self, move):
    print(Pieces.toString(abs(self.getPieces(move.src))) + str(move.src) + "-" + str(move.dst))

# get the correct position from the coordinates 1-9 and 1-10
def getPositions(self, pos, piece):
    def addPos(i, j):
        if i >= 1 and i <= 9 and j >= 1 and j <= 10:
            res.append(Position(i, j))

#each piece and the ways they can move
    s = piece
    res = []
    if (s == Pieces.Chariot) or (s == Pieces.Cannon):
        for i in range(10):
            addPos(pos.x, i + 1)
        for i in range(9):
            addPos(i + 1, pos.y)
    elif s == Pieces.Horse:
        addPos(pos.x + 1, pos.y + 2)
        addPos(pos.x + 1, pos.y - 2)
        addPos(pos.x - 1, pos.y + 2)
        addPos(pos.x - 1, pos.y - 2)
        addPos(pos.x + 2, pos.y + 1)
        addPos(pos.x + 2, pos.y - 1)
        addPos(pos.x - 2, pos.y + 1)
        addPos(pos.x - 2, pos.y - 1)
    elif s == Pieces.Elephant:
        addPos(pos.x + 2, pos.y + 2)
        addPos(pos.x + 2, pos.y - 2)
        addPos(pos.x - 2, pos.y + 2)
        addPos(pos.x - 2, pos.y - 2)
    elif s == Pieces.Advisor:
        addPos(pos.x + 1, pos.y + 1)
        addPos(pos.x + 1, pos.y - 1)
        addPos(pos.x - 1, pos.y + 1)
        addPos(pos.x - 1, pos.y - 1)
    elif s == Pieces.King:
        addPos(pos.x + 1, pos.y)
        addPos(pos.x, pos.y + 1)
        addPos(pos.x - 1, pos.y)
        addPos(pos.x, pos.y - 1)
    elif s == Pieces.Pawn:
        addPos(pos.x + 1, pos.y)
        addPos(pos.x, pos.y + 1)
        addPos(pos.x - 1, pos.y)
        addPos(pos.x, pos.y - 1)
        return res


def getAllMoves(self, color):
    res = []
    for k in self.pieces.keys():
        piece = self.pieces[k]
        src = Position(k[1] + 1, k[0] + 1)
        apiece = abs(piece)
    for pos in self.getPositions(src, apiece):
        try:
            dst = pos
            col = Color.Red if piece > 0 else Color.Black
            if col == color:
                self.tryMovePiece(col, src, dst)
                res.append(Move(col, src, dst))
        except:
            pass
    return res

# create a new board with all the pieces back in the initial position
def _getNewBoard(self, src, dst):
    newb = Board(True)
    for i in range(10):
        for j in range(9):
            newb.board[i][j] = self.board[i][j]
    newb.pieces = {}
    for k in self.pieces.keys():
        newb.pieces[k] = self.pieces[k]
    newb.redking = self.redking
    newb.blackking = self.blackking
    newb.movePieces(src, dst)
    return newb

# when the general is in danger of being captured by the enemy player on its next move
def isCheck(self, color):
    kingpos = None
    otherkingpos = None
    if color == Color.Red:
        kingpos = self.redking
        otherkingpos = self.blackking
    else:
        kingpos = self.blackking
        otherkingpos = self.redking
    for m in self.getAllMoves(color):
        if self.getPiece(m.src) * color > 0 and m.dst.isEqual(otherkingpos):
            return True
    if kingpos.sameColumn(otherkingpos) and self.piecesBetween(kingpos, otherkingpos) == 0:
        return True
    return False

# if the general's player can make no move to prevent the general's capture
def isCheckmate(self, color):
    for m in self.getAllMoves(-color):
        newb = self._getNewBoard(m.src, m.dst)
        if not newb.isCheck(color):
# print("Protect with ", m)
            return False
    return True


class Move:
    def __init__(self, color, src, dst):
        self.color = color
        self.src = src
        self.dst = dst

    def __str__(self):
        return str(self.src) + str(self.dst)


class XiangqiGame:
    def __init__(self):
        self.moves = []
        self.positions = []
    def addMove(self, m):
        self.moves.append(m)
    def addPosition(self, p):
        self.positions.append(copy.deepcopy(p))
    def checkRepetition(self):
        lastp = self.positions[-1]
        counter = 0
        for p in self.positions[:len(self.positions) - 2]:
            if lastp.equals(p):
                counter += 1
        if counter == 4:
            return True
        return False


def getMove(self, color):
    s = input("Move " + ("Red" if color == 1 else "Black") + " >")

