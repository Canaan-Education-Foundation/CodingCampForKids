from graph_paper import Graph_Paper

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
