import tkinter as tk
import math

class Graph_Paper:
    pre_stat = "Graph_Paper:   "

    def __init__(self, rows = 5, columns = 5, cell_size = 50, fill_color = "black", start_row = 1, start_column = 1, debug=False):
        self._fill_color = fill_color
        self._cell_size = cell_size
        self.number_of_rows = rows
        self.number_of_columns = columns
        self._has_error = False
        self._debug_mode = debug

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
        if (self._debug_mode):
            print(self.pre_stat + "[Created Window]")
        return window

    def _make_grid(self):
        graph_grid = [None for x in range(self.number_of_rows)]

        for i in range(self.number_of_rows):
            column_grid = [None for y in range(self.number_of_columns)]
            for j in range(self.number_of_columns):
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
        if (self._debug_mode):
            print("{0}[Created grid with {1} rows and {2} columns]".format(self.pre_stat, self.number_of_rows, self.number_of_columns))
        return graph_grid

    def _mark_start_position(self, grid_cell):
        canvas = tk.Canvas(grid_cell, width = self._cell_size, height = self._cell_size)
        self._draw_star(canvas)
        canvas.pack()
        if (self._debug_mode):
            print("{0}[Marked start position at row {1}, column {2}]".format(self.pre_stat, self.number_of_rows, self.number_of_columns))

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
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                self._grid[i][j].configure(background = color)
        self._window.update()

    def change_fill_color(self, color):
        self._fill_color = color
        if (self._debug_mode):
            print("{0}[Changed fill color to {1}]".format(self.pre_stat, color))

    def move_left(self, spaces = 1):
        if not self._has_error and spaces > 0:
            self._col_position -= spaces
            if (self._debug_mode):
                print("{0}[Moved {1} cell(s) to the left ... \tNow on row {2}, column {3}]".format(self.pre_stat, spaces, self.get_row(), self.get_column()) )

    def move_right(self, spaces = 1):
        if not self._has_error and spaces > 0:
            self._col_position += spaces
            if (self._debug_mode):
                print("{0}[Moved {1} cell(s) to the right ... \tNow on row {2}, column {3}]".format(self.pre_stat, spaces, self.get_row(), self.get_column()) )

    def move_up(self, spaces = 1):
        if not self._has_error and spaces > 0:
            self._row_position -= spaces
            if (self._debug_mode):
                print("{0}[Moved {1} cell(s) up ... \tNow on row {2}, column {3}]".format(self.pre_stat, spaces, self.get_row(), self.get_column()) )


    def move_down(self, spaces = 1):
        if not self._has_error and spaces > 0:
            self._row_position += spaces
            if (self._debug_mode):
                print("{0}[Moved {1} cell(s) down ... \tNow on row {2}, column {3}]".format(self.pre_stat, spaces, self.get_row(), self.get_column()) )

    def fill(self):
        if not self._has_error:
            try:
                self._grid[self._row_position][self._col_position].configure(background = self._fill_color)
                self._window.update()
                if (self._debug_mode):
                    print("{0}[Filled cell at row {1}, column {2} with color]".format(self.pre_stat, self.get_row(), self.get_column()) )

            except Exception as e:
                self._has_error = True
                for i in range(self.number_of_rows):
                    for j in range(self.number_of_columns):
                        self._grid[i][j].configure(background = "Red")
                if (self._debug_mode):
                    print(self.pre_stat + "{0}[ERROR!!! Cell at row {1}, column {2} does not exist! Cannot fill it with color. Program Halted]".format(self.pre_stat, self.get_row(), self.get_column())  )
                print(e.__traceback__)

    def get_row(self):
        return self._row_position + 1

    def get_column(self):
        return self._col_position + 1

    def clear_all(self):
        self._fill_all(self._window.cget('bg'))

    def show(self):
        if (self._debug_mode):
            print(self.pre_stat + "[Displayed Grid]" )
        self._window.mainloop()
