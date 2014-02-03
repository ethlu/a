import pygame
import sys
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SQUARE_SIZE = 100

BACKGROUND_COLOR = (100, 149, 237)
LINE_COLOR = (0, 0, 139)
LINE_WIDTH = 2

class Board:
    def __init__(self, num_columns, num_rows, square_size, line_color, line_width):
        self.num_columns = num_columns
        self.num_rows = num_rows
        self.square_size = square_size
        self.line_color = line_color
        self.line_width = line_width

    def draw(self, surface):
        line_start = self.square_size / 2

        # draw the vertical lines
        for vertical in range(1, self.num_columns):
            vertical_pos = line_start + self.square_size * vertical
            pygame.draw.line(surface, self.line_color,
                             (vertical_pos, line_start),
                             (vertical_pos, line_start + self.square_size * self.num_rows),
                             self.line_width)

        # draw the horizontal lines
        for horizontal in range(1, self.num_columns):
            horizontal_pos = line_start + self.square_size * horizontal
            pygame.draw.line(surface, self.line_color,
                             (line_start, horizontal_pos),
                             (line_start + self.square_size * self.num_columns, horizontal_pos),
                             self.line_width)


class TicTacToeBoard(Board):
    def __init__(self, square_size, line_color, line_width):
        Board.__init__(self, 3, 3, square_size, line_color, line_width)


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    board = TicTacToeBoard(SQUARE_SIZE, LINE_COLOR, LINE_WIDTH)

    

    

    while True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit(0)
        
        # draw the background
        screen.fill(BACKGROUND_COLOR)

        # draw the board
        board.draw(screen)

        # display the screen
    
        pygame.display.flip()
