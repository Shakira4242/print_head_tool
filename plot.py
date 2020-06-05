import argparse
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

def playback_visualizer(start_pos, stop_pos):
    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)


    # Lines to plot in 3D
    x = np.linspace(start_pos[0], stop_pos[0],100)
    y = np.linspace(start_pos[1], stop_pos[1],100)
    z = np.linspace(start_pos[2], stop_pos[2],100)
    data = np.array([[x,y,z]])

    # NOTE: Can't pass empty arrays into 3d version of plot()
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]


    ax.set_xlim(-10.10,10.10)
    ax.set_ylim(-10.10,10.10)
    ax.set_zlim(-10.10,10.10)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update_lines, 50, fargs=(data, lines),
                                       interval=100, blit=True, repeat=True)
    #
    plt.show()

def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines





def head_visualizer(start_pos):
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    step = 0.1

    x_min = 0    # the minimial value of the paramater a
    x_max = 10   # the maximal value of the paramater a
    x_init = 0   # the value of the parameter a to be used initially, when the graph is created

    y_min = 0    # the minimial value of the paramater a
    y_max = 10   # the maximal value of the paramater a
    y_init = 0   # the value of the parameter a to be used initially, when the graph is created
    
    z_min = 0    # the minimial value of the paramater a
    z_max = 10   # the maximal value of the paramater a
    z_init = 0   # the value of the parameter a to be used initially, when the graph is created

    axcolor = 'yellow'

    x_box = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor = axcolor)
    y_box = plt.axes([0.25,  0.15, 0.65, 0.03], facecolor = 'yellow')
    z_box = plt.axes([0.25,  0.20, 0.65, 0.03], facecolor = 'yellow')
    
    # create slider
    x_slider = Slider(x_box, 'x_position', 0.1, 10.0, valinit=x_min, valstep=step)
    y_slider = Slider(y_box, 'y_position', 0.1, 10.0, valinit=y_min)
    z_slider  = Slider(z_box, 'z_position', 0.1, 10.0, valinit=z_min)

    # plot the start_pos on the plt
    
    plot = ax.scatter3D(start_pos[0], start_pos[1], start_pos[2], cmap='Greens');



    # Next we define a function that will be executed each time the value
    # indicated by the slider changes. The variable of this function will
    # be assigned the value of the slider.
    def update(val):
        ax.clear()
        x = np.array(x_slider.val)
        y = np.array(y_slider.val)
        z = np.array(z_slider.val)
        ax.scatter3D(x, y, z, cmap='Greens')
      

    x_slider.on_changed(update)
    x_slider.reset()
    y_slider.on_changed(update)
    y_slider.reset()
    z_slider.on_changed(update)
    z_slider.reset()

        # the final step is to specify that the slider needs to
    # execute the above function when its value changes

    plt.show() 

    # print("akash  & amrita are cool")
      
