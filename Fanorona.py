class Strategy:
    __slots__ = "board"

    def __init__(self, board):
        self.board = board

    # returns a tuple, 1st index -> position; 2nd index = direction
    def get_movable_pieces(self, color):
        slots_arr = []
        for i in range(self.board.x):
            for j in range(self.board.y):
                if self.board.my_board[i][j].get_color() == color:
                    for move in self.board.my_board[i][j].get_possible_moves():
                        if self.board.my_board[move.x][move.y].get_color() == "n":
                            move_direction = self.get_direction(i, j, move.x, move.y, True)
                            slots_arr.append((Move(i,j), move_direction))
        return slots_arr

    def get_best_move(self, color):
        all_moves = self.get_movable_pieces(color)
        max = 0
        for each in all_moves:
            move = each[0]
            move_to = each[1](move.x, move.y)[0]
            get_approach_pieces = each[1](move.x, move.y)[1](move_to.x, move_to.y, color)
            get_withdraw_pieces = each[1](move_to.x, move_to.y)[1](move.x, move.y, color)
            if len(get_approach_pieces)>max:
                max = len(get_approach_pieces)
                max_move = move
                max_move_to = move_to
                self.board.my_board[max_move_to.x][max_move_to.y].set_color(color)
                self.board.my_board[max_move.x][max_move.y].set_color("n")
                opp_color = self.get_opp_color(color)
                self.board.remove(get_approach_pieces, opp_color)
            if len(get_withdraw_pieces)>max:
                max = len(get_withdraw_pieces)
                max_move = move
                max_move_to = move_to
                self.board.my_board[max_move_to.x][max_move_to.y].set_color(color)
                self.board.my_board[max_move.x][max_move.y].set_color("n")
                opp_color = self.get_opp_color(color)
                self.board.remove(get_withdraw_pieces, opp_color)
        self.board.print_board()

    def get_opp_top(self, x_pos, y_pos, color):
        arr = []
        opp_color = self.get_opp_color(color)
        # opp_color = self.get_opp_color(self.board.my_board[x_pos][y_pos].get_color())
        for i in range(x_pos-1, -1, -1):
            if self.board.my_board[i][y_pos].get_color() == opp_color:
                arr.append(Move(i,y_pos))
            else:
                return arr
        return arr

    def get_opp_bottom(self, x_pos, y_pos, color):
        arr = []
        opp_color = self.get_opp_color(color)
        # opp_color = self.get_opp_color(self.board.my_board[x_pos][y_pos].get_color())
        for i in range(x_pos +1, self.board.x):
            if self.board.my_board[i][y_pos].get_color() == opp_color:
                arr.append(Move(i, y_pos))
            else:
                return arr
        return arr

    def get_opp_left(self, x_pos, y_pos, color):
        arr = []
        opp_color = self.get_opp_color(color)
        # opp_color = self.get_opp_color(self.board.my_board[x_pos][y_pos].get_color())
        for j in range(y_pos-1, -1, -1):
            if self.board.my_board[x_pos][j].get_color() == opp_color:
                arr.append(Move(x_pos, j))
            else:
                return arr
        return arr

    def get_opp_right(self,x_pos, y_pos, color):
        arr = []
        opp_color = self.get_opp_color(color)
        # opp_color = self.get_opp_color(self.board.my_board[x_pos][y_pos].get_color())
        for j in range(y_pos + 1 , self.board.y):
            if self.board.my_board[x_pos][j].get_color() == opp_color:
                arr.append(Move(x_pos, j))
            else:
                return arr
        return arr

    def get_opp_rt_diag(self, x_pos, y_pos, color):
        i=x_pos
        j=y_pos
        opp_color = self.get_opp_color(color)
        # opp_color = self.get_opp_color(self.board.my_board[x_pos][y_pos].get_color())
        arr = []
        while i-1 >-1 and j+1<self.board.y:
            i -= 1
            j += 1
            if self.board.my_board[i][j].get_color() == opp_color:
                arr.append(Move(i,j))
            else:
                return arr
        return arr

    def get_opp_lt_diag(self, x_pos, y_pos, color):
        i = x_pos
        j = y_pos
        opp_color = self.get_opp_color(color)
        # opp_color = self.get_opp_color(self.board.my_board[x_pos][y_pos].get_color())
        arr = []
        while i-1 > -1 and j-1 >-1:
            i -= 1
            j -= 1
            if self.board.my_board[i][j].get_color() == opp_color:
                arr.append(Move(i, j))
            else:
                return arr
        return arr

    def get_opp_rb_diag(self, x_pos, y_pos, color):
        i = x_pos
        j = y_pos
        opp_color = self.get_opp_color(color)
        # opp_color = self.get_opp_color(self.board.my_board[x_pos][y_pos].get_color())
        arr = []
        while i+1 < self.board.x and j+1 < self.board.y:
            i += 1
            j += 1
            if self.board.my_board[i][j].get_color() == opp_color:
                arr.append(Move(i, j))
            else:
                return arr
        return arr

    def get_opp_lb_diag(self, x_pos, y_pos, color):
        i = x_pos
        j = y_pos
        opp_color = self.get_opp_color(color)
        # opp_color = self.get_opp_color(self.board.my_board[x_pos][y_pos].get_color())
        arr = []
        while i+1 < self.board.x and j-1 > -1:
            i += 1
            j -= 1
            if self.board.my_board[i][j].get_color() == opp_color:
                arr.append(Move(i, j))
            else:
                return arr
        return arr

    def get_opp_color(self, my_color):
        if my_color == "w":
            return "b"
        else:
            return "w"

    def top(self, x, y ):
        return Move(x-1,y), self.get_opp_top

    def bottom(self, x, y):
        return Move(x+1, y), self.get_opp_bottom

    def left(self,x,y):
        return Move(x, y-1), self.get_opp_left

    def right(self, x, y):
        return Move(x, y+1), self.get_opp_right

    def rt_diag(self, x, y):
        return Move(x-1, y+1), self.get_opp_rt_diag

    def lt_diag(self, x, y):
        return Move(x-1, y-1), self.get_opp_lt_diag

    def rb_diag(self, x, y):
        return Move(x+1, y+1), self.get_opp_rb_diag

    def lb_diag(self, x, y):
        return Move(x+1, y-1), self.get_opp_lb_diag

    def get_direction(self, curr_x, curr_y, next_x, next_y, withdrawOrApproach):
        if curr_x - next_x == 1 and curr_y == next_y:
            return self.top
        if curr_x - next_x == -1 and curr_y == next_y:
            return self.bottom
        if curr_x == next_x and curr_y - next_y == 1:
            return self.left
        if curr_x == next_x and curr_y - next_y == -1:
            return self.right
        if curr_x - next_x == 1 and curr_y - next_y == -1:
            return self.rt_diag
        if curr_x - next_x == 1 and curr_y - next_y == 1:
            return self.lt_diag
        if curr_x - next_x == -1 and curr_y - next_y == -1:
            return self.rb_diag
        if curr_x - next_x == -1 and curr_y - next_y == 1:
            return self.lb_diag

class Board:
    __slots__ = "my_board", "x", "y", "no_of_b", "no_of_w"

    def __init__(self,  x=5, y=9):
        self.x = x
        self.y = y
        self.my_board = []
        self.set_no_of_pieces()
        self.init_board()
        self.create_board()
        self.place_pieces()

    def set_no_of_pieces(self):
        if self.x == 5 and self.y == 9:
            self.no_of_w = self.no_of_b = 22
        if self.x == 5 and self.y == 5:
            self.no_of_w = self.no_of_b = 12
        if self.x == 3 and self.y == 3:
            self.no_of_w = self.no_of_b = 4

    def init_board(self):
        for i in range(self.x):
            dummy_list = []
            for j in range(self.y):
                dummy_list.append(Slot())
            self.my_board.append(dummy_list)

    def create_board(self):
        if self.x == 3 and self.y == 3:
            self.create_mini_board(0,0)
        else:
            if self.x == 5:
                self.create_mini_board(0,0)
                self.create_mini_board(0,2)
                self.create_mini_board(2,0)
                self.create_mini_board(2,2)
            if self.y == 9:
                self.create_mini_board(0,4)
                self.create_mini_board(0,6)
                self.create_mini_board(2,4)
                self.create_mini_board(2,6)

    def remove(self, positions, color):
        for move in positions:
            self.my_board[move.x][move.y].remove_piece()
            if self.my_board[move.x][move.y]:
                if color == "w":
                    self.no_of_w -= 1
                else:
                    self.no_of_b -= 1

    def create_mini_board(self, xi, yi):
        self.my_board[xi][yi].set_possible_moves([Move(xi,yi+1), Move(xi+1, yi+1), Move(xi+1,yi)])
        self.my_board[xi][yi+1].set_possible_moves([Move(xi,yi+2), Move(xi+1,yi+1), Move(xi,yi)])
        self.my_board[xi][yi+2].set_possible_moves([Move(xi,yi+1), Move(xi+1,yi+1), Move(xi+1,yi+2)])
        self.my_board[xi+1][yi].set_possible_moves([Move(xi,yi), Move(xi+1,yi+1), Move(xi+2,yi)])
        self.my_board[xi+1][yi+1].set_possible_moves([Move(xi,yi),Move(xi,yi+1), Move(xi,yi+2),Move(xi+1,yi),Move(xi+1,yi+2), Move(xi+2,yi), Move(xi+2,yi+1),Move(xi+2, yi+2)])
        self.my_board[xi+1][yi+2].set_possible_moves([Move(xi,yi+2), Move(xi+1,yi+1), Move(xi+2,yi+2)])
        self.my_board[xi+2][yi].set_possible_moves([Move(xi+1,yi), Move(xi+1,yi+1), Move(xi+2,yi+1)])
        self.my_board[xi+2][yi+1].set_possible_moves([Move(xi+2, yi), Move(xi+1, yi+1), Move(xi+2,yi+2)])
        self.my_board[xi+2][yi+2].set_possible_moves([Move(xi+2, yi+1), Move(xi+1,yi+1), Move(xi+1,yi+2)])

    def place_pieces(self):
        rowsBy2 = self.x//2
        colsBy2 = self.y//2
        color = "w"
        for i in range(self.x):
            if i > rowsBy2:
                color = "b"
            if i == rowsBy2 :
                color = "no color"
            for j in range(self.y):
                if color == "no color":
                    if j == colsBy2:
                        self.my_board[i][j].set_color("n")
                    else:
                        if j % 2 == 0:
                            if j<colsBy2:
                                self.my_board[i][j].set_color("w")
                            else:
                                self.my_board[i][j].set_color("b")
                        else:
                            if j > colsBy2:
                                self.my_board[i][j].set_color("w")
                            else:
                                self.my_board[i][j].set_color("b")
                else:
                    self.my_board[i][j].set_color(color)

    def print_board(self):
        for row in range(self.x):
            for col in range(self.y):
                print(self.my_board[row][col].get_color(), end ="   ")
                # print(row,col, "---> ",self.my_board[row][col])
            print()
        print("whites: ", self.no_of_w)
        print("blacks: ", self.no_of_b, "\n")

class Slot:
    __slots__ = "possible_moves","color"

    def __init__(self):
        self.possible_moves = []

    def remove_piece(self):
        self.color = "n"

    def set_possible_moves(self, moves_array):
        self.possible_moves = moves_array

    def get_possible_moves(self):
        return self.possible_moves

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        if self.possible_moves == None:
            s = "No Moves"
        else:
            s = ""
            for move in self.possible_moves:
                s += str(move) + " & "
            s += "--->  " + self.color
        return s

class Move:
    __slots__ = "x", "y"

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + "," + str(self.y) +" "

def minmax_nodepth(game):
    while(game.board.no_of_w != 0 or game.board.no_of_b != 0):
        game.get_best_move("w")
        game.get_best_move("b")

def get_opp_color(color):
    if color == "w":
        return "b"
    else:
        return "w"

def minmax_with_depth(game):
    depth = 5
    color = "w"
    for i in range(depth):
        game.get_best_move(color)
        color = get_opp_color(color)

def start_game():
    b = Board()
    g = Strategy(b)
    # minmax_nodepth(g)
    minmax_with_depth(g)

def main():
    x = 5
    y = 9
    if (x==3 and y==3) or (x==5 and y==5) or (x==5 and y==9):
        b = Board(x,y)
        b.print_board()
        start_game()
    else:
        print("Give correct dimensions")
        print("choose a 3*3 5*5 or a 5*9 board to play the game!")

if __name__ == '__main__':
    main()