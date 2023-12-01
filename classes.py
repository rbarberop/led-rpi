from operator import add,sub

class Led:
    def __init__(self, start_color, step, end_color):
        self.start_color = start_color
        self.current_color = start_color
        self.end_color = end_color
        self.step = step

    def next(self):
        if self.current_color < self.end_color:
            self.current_color = tuple(map(add, self.current_color, self.step))

    def previous(self):
        if self.current_color > self.start_color:
            self.current_color = tuple(map(sub, self.current_color, self.step))

c0 = (0,0,0)
c1 = (10,10,10)
c2 = (255,255,255)

led1 = Led(c0,c1,c2)

led1.next()

print(led1.current_color)

led1.next()

print(led1.current_color)

led1.previous()

print(led1.current_color)

led1.previous()

print(led1.current_color)

led1.previous()

print(led1.current_color)

led1.previous()

print(led1.current_color)