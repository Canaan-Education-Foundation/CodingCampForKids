def move_to(grid, row, column):
    current_row = grid.get_row()
    current_column = grid.get_column()

    if current_row < row:
        number_of_cells = row - current_row
        grid.move_down(number_of_cells)
    elif current_row > row:
        number_of_cells = current_row - row
        grid.move_up(number_of_cells)

    if current_column < column:
        number_of_cells = column - current_column
        grid.move_right(number_of_cells)
    elif current_column > column:
        number_of_cells = current_column - column
        grid.move_left(number_of_cells)

def fill_at_cell(grid, row, column, color=None):
    move_to(grid, row, column)
    grid.fill()

def move_to_row(grid, row, column=1):
    move_to(grid, row, column)

def move_to_column(grid, column, row=1):
    move_to(grid, row, column)

def fill_row(grid, row):
    move_to(grid, row, 1)
    for i in range(grid.number_of_rows):
        grid.fill()
        grid.move_right()

def fill_column(grid, column):
    move_to(grid, 1, column)
    for i in range(grid.number_of_columns):
        grid.fill()
        grid.move_down()

def fill_row_alternate(grid, row):
    move_to(grid, row, 1)
    fill_cell = True
    for i in range(grid.number_of_rows):
        if fill_cell:
            grid.fill()
        grid.move_right()
        fill_cell = not fill_cell

def make_checkerboard(grid):
    for i in range(grid.number_of_rows):
        move_to_row(grid, i)
    row_number = grid.get_row()
    for j in range(grid.number_of_columns):
        column_number = grid.get_column()
        if row_number % 2 != 0 and column_number % 2 == 0:
            grid.fill()
        elif row_number % 2 == 0 and column_number % 2 != 0:
            grid.fill()
        grid.move_right()
