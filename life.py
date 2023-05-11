from abc import abstractmethod, ABC
from time import sleep


class AbstractLifeGameBoard(ABC):
    def __init__(self, width: int = 3, height: int = 3):
        pass

    def __str__(self):
        """Return a string representation of a board.

        Use small o for alive cells and period for empty cells.
        E.g. for board 3x3 with simplest oscillator:
        .o.
        .o.
        .o.
        """
        pass

    @abstractmethod
    def place_cell(self, row: int, col: int):
        """Make a cell alive."""
        pass

    @abstractmethod
    def toggle_cell(self, row: int, col: int) -> None:
        """Invert state of the cell."""
        pass

    @abstractmethod
    def next(self) -> None:
        pass

    @abstractmethod
    def is_alive(self, row: int, col: int) -> bool:
        pass


class Board(AbstractLifeGameBoard):
    def __init__(self, width: int = 3, height: int = 3):
        # Инициализация новой доски с заданными размерами
        self.width = width
        self.height = height
        self.board = [[False] * width for _ in range(height)]

    def __str__(self):
        # Получить строковое представление доски в виде таблицы (живые клетки - "o", мертвые - ".")
        res = ""
        for row in self.board:
            for cell in row:
                res += c if cell else "."
            res += "\n"
        return res

    def place_cell(self, row: int, col: int):
        # Добавить живую клетку на заданную позицию
        self.board[row][col] = True

    def toggle_cell(self, row: int, col: int) -> None:
        # Инвертировать состояние клетки (если клетка была мертвой, она станет живой, и наоборот)
        self.board[row][col] = not self.board[row][col]

    def next(self) -> None:
        # Продвинуть игру на один шаг - изменить состояние клеток на основе правил "Жизни"
        new_board = [[False] * self.width for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                count = self.count_neighbors(i, j)
                if self.board[i][j]:
                    if count in [2, 3]:
                        new_board[i][j] = True
                else:
                    if count == 3:
                        new_board[i][j] = True
        self.board = new_board

    def is_alive(self, row: int, col: int) -> bool:
        # Проверить, жива ли клетка на заданной позиции
        return self.board[row][col]

    def count_neighbors(self, row: int, col: int) -> int:
        # Подсчитать количество живых соседних клеток для заданной клетки
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (
                    i >= 0
                    and i < self.height
                    and j >= 0
                    and j < self.width
                    and not (i == row and j == col)
                ):
                    if self.board[i][j]:
                        count += 1
        return count


c = CELL_SYMBOL = "o"


if __name__ == "__main__":
    board = Board(10, 10)
    for i in range(3):
        board.place_cell(1, i)

    for i in range(10):
        print(board)
        board.next()
        sleep(0.5)
