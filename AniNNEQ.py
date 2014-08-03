import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_line( num, data_local, line_b, line_r):
    # In every starting time, data will be initialize again with different values
    global data
        
    line_b.set_data( data[...,num:num+2])
    line_r.set_data( data[...,:num+1])

    #if num == 24:
    #    data = np.random.rand(2, 25)
    print num
     
    return line_b, line_r, 

fig1 = plt.figure()

data = np.random.rand(2, 25)
lr, = plt.plot( [], [], 'rx-')
lb, = plt.plot( [], [], 'bo-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('Animation')
line_ani = animation.FuncAnimation( fig1, update_line, 25, fargs = (data, lr, lb), interval=200, blit=True)

plt.show() 