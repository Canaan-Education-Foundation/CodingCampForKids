class Graph_Paper:

    def __init__(self, width = 5, height = 5):
        self.pen_color = 'Black'
        self.x_position = 0
        self.y_position = 0

    def change_pen_color(self, color):
        self.pen_color = color

    def move_left(self):
        self.x_position -= 1

    def move_right(self):
        self.x_position += 1

    def move_up(self):
        self.y_position -= 1

    def move_down(self):
        self.y_position += 1

    def fill(self):
        self.fill = True

    def clear(self):
        self.clear = True

