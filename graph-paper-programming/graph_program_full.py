import tkinter as tk
import math

class Graph_Paper:

    def __init__(self, width = 5, height = 5, cell_size = 50, fill_color = "black", start_x = 1, start_y = 1):
        self._fill_color = fill_color
        self._cell_size = cell_size
        self._grid_width = width
        self._grid_height = height
        self._has_error = False

        if start_x > 0:
            self._x_position = start_x - 1
        else:
            self._x_position = 0

        if start_y > 0:
            self._y_position = start_y - 1
        else:
            self._y_position = 0

        self._window = self._make_window()
        self._grid = self._make_grid()

    def _make_window(self):
        window = tk.Tk()
        window.title("Graph Paper Programming")
        window.resizable(width=False, height=False)
        return window

    def _make_grid(self):
        graph_grid = [None for x in range(self._grid_width)]

        for i in range(self._grid_width):
            column_grid = [None for y in range(self._grid_height)]
            for j in range(self._grid_height):
                column_grid_cell = tk.Frame(
                    master = self._window,
                    relief = tk.RAISED,
                    width = self._cell_size,
                    height = self._cell_size,
                    borderwidth = 1
                )
                column_grid_cell.grid(row = i, column = j, sticky="snew")
                column_grid[j] = column_grid_cell
                if i == self._x_position and j == self._y_position:
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
        for i in range(self._grid_width):
            for j in range(self._grid_height):
                self._grid[i][j].configure(background = color)
        self._window.update()

    def change_fill_color(self, color):
        self._fill_color = color

    def move_left(self):
        if not self._has_error:
            self._x_position -= 1

    def move_right(self):
        if not self._has_error:
            self._x_position += 1

    def move_up(self):
        if not self._has_error:
            self._y_position -= 1

    def move_down(self):
        if not self._has_error:
            self._y_position += 1

    def fill(self):
        if not self._has_error:
            try:
                self._grid[self._x_position][self._y_position].configure(background = self._fill_color)
                self._window.update()
            except Exception:
                self._has_error = True
                print(Exception)

    def get_row(self):
        return self._y_position + 1

    def get_column(self):
        return self._x_position + 1

    def clear_all(self):
        self._fill_all(self._window.cget('bg'))

    def show(self):
        self._window.mainloop()

def main():
    # Function for starting the program and defining
    # important variables.
    grid = Graph_Paper(width = 10, height = 10, start_x = 2, start_y = 2)
    grid.move_right()
    grid.fill()
    grid.move_down()
    grid.fill()
    grid.move_right()
    grid.fill()
    print(grid.get_row())
    print(grid.get_column())
    grid.show()


main()