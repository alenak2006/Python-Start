from enum import Enum
import pygame as pg

CELL_SIZE = 50
FPS = 60


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Player and avators and name
    """

    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type


class GameRoundManager:
    """
    Manages all game processes
    """

    def __init__(self, player1: Player, player2: Player) -> None:
        self._players = [player1, player2]
        self.current_player = 0
        self.field = GameField()

    def handle_click(self, event, i, j):
        print("click handled", event, i, j)


class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]


class GameFieldView:
    def __init__(self, field):
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True

    def get_coords(self, x, y):
        return 0, 0


class GameWindow:
    """
    Contain widget of the field and the game round
    """

    def __init__(self) -> None:
        pg.init()
        self._height = 600
        self._width = 800
        self._title = "Tic Tac Toe"
        self._screen = pg.display.set_mode((self._width, self._height))
        pg.display.set_caption(self._title)

        player1 = Player("Pete", Cell.CROSS)
        player2 = Player("Don", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def main_loop(self):
        finished = False
        clock = pg.time.Clock()
        while not finished:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    finished = True
                elif event.type == pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()
                    x, y = mouse_pos
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(event, i, j)
            pg.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print("Game over!")


main()

if __name__ == "__main__":
    pass
