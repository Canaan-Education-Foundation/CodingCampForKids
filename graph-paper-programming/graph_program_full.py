import tkinter as tk
import math

class Graph_Paper:

    def __init__(self, rows = 5, columns = 5, cell_size = 50, fill_color = "black", start_row = 1, start_column = 1):
        self._fill_color = fill_color
        self._cell_size = cell_size
        self._grid_rows = rows
        self._grid_columns = columns
        self._has_error = False

        if start_row > 0:
            self._row_position = start_row - 1
        else:
            self._row_position = 0

        if start_column > 0:
            self._col_position = start_column - 1
        else:
            self._col_position = 0

        self._window = self._make_window()
        self._grid = self._make_grid()

    def _make_window(self):
        window = tk.Tk()
        window.title("Graph Paper Programming")
        window.resizable(width=False, height=False)
        return window

    def _make_grid(self):
        graph_grid = [None for x in range(self._grid_rows)]

        for i in range(self._grid_rows):
            column_grid = [None for y in range(self._grid_columns)]
            for j in range(self._grid_columns):
                column_grid_cell = tk.Frame(
                    master = self._window,
                    relief = tk.RAISED,
                    width = self._cell_size,
                    height = self._cell_size,
                    borderwidth = 1
                )
                column_grid_cell.grid(row = i, column = j, sticky="snew")
                column_grid[j] = column_grid_cell
                if i == self._row_position and j == self._col_position:
                    self._mark_start_position(column_grid_cell)
            graph_grid[i] = column_grid
        return graph_grid

    def _mark_start_position(self, grid_cell):
        canvas = tk.Canvas(grid_cell, width = self._cell_size, height = self._cell_size)
        self._draw_star(canvas)
        canvas.pack()

    def _draw_star(self, drawing_canvas):
        #
        size = self._cell_size / 2
        center_x = size
        center_y = size

        r = size # The distance from the center point to each angle, called the radius

        # Place the five points of the five-pointed star in turn
        points=[
            #
            center_x - int(r * math.sin(2 * math.pi/5)),
            center_y - int(r * math.cos(2 * math.pi/5)),

            #
            center_x + int(r * math.sin(2 * math.pi/5)),
            center_y - int(r * math.cos(2 * math.pi/5)),

            #
            center_x - int(r * math.sin(math.pi/5)),
            center_y + int(r * math.cos(math.pi/5)),

            # vertex
            center_x,
            center_y-r,

            #
            center_x + int(r * math.sin(math.pi/5)),
            center_y + int(r * math.cos(math.pi/5)),
        ]
        # Create a polygon based on ten vertices
        drawing_canvas.create_polygon(points, outline = self._fill_color, fill = "gray")

    def _fill_all(self, color):
        for i in range(self._grid_rows):
            for j in range(self._grid_columns):
                self._grid[i][j].configure(background = color)
        self._window.update()

    def change_fill_color(self, color):
        self._fill_color = color

    def move_left(self, spaces = 1):
        if not self._has_error and spaces > 0:
            self._col_position -= spaces

    def move_right(self, spaces = 1):
        if not self._has_error and spaces > 0:
            self._col_position += spaces

    def move_up(self, spaces = 1):
        if not self._has_error and spaces > 0:
            self._row_position -= spaces

    def move_down(self, spaces = 1):
        if not self._has_error and spaces > 0:
            self._row_position += spaces

    def fill(self):
        if not self._has_error:
            try:
                self._grid[self._row_position][self._col_position].configure(background = self._fill_color)
                self._window.update()
            except Exception:
                self._has_error = True
                print(Exception)

    def get_row(self):
        return self._row_position + 1

    def get_column(self):
        return self._col_position + 1

    def clear_all(self):
        self._fill_all(self._window.cget('bg'))

    def show(self):
        self._window.mainloop()

def main():
    # Function for starting the program and defining
    # important variables.
    # Enter program code here
    grid = Graph_Paper()
    grid.move_down(2)
    grid.fill()
    grid.show()


main()