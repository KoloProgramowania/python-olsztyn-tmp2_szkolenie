from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
from PyTechBrain import *
my_board = PyTechBrain()
my_board.board_init()


x_data, y_data = [], []

figure = plt.figure()
line, = plt.plot_date(x_data, y_data, '-')

def update(frame):
    x_data.append(datetime.now())
    y_data.append(my_board.get_potentiometer_raw())
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,

animation = FuncAnimation(figure, update, interval=500)

plt.show()