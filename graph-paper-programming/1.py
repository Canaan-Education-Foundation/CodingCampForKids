from graph_paper import Graph_Paper


grid = Graph_Paper(rows = 10, columns = 10)
# Add your code after this line
for i in range(9):
    grid.move_right()
    grid.fill()

# Don't add any code after this line.
grid.show()