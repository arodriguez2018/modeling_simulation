#from pylive import live_plotter
from pylive import live_plotter
import numpy as np

size = 60
x_vec = np.linspace(0,240,size+1)[0:-1]
y_vec = np.random.randn(len(x_vec))
line1 = []


while True:
#while x_vec.all() < 124:
    rand_val = np.random.randn(1)
    y_vec[-1] = 10 #input function here
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)

