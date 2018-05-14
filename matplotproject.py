import matplotlib.pyplot as plt
##import numpy as np

def formular(csquared, clinear,constant, upper_lim, lower_lim):
    x_val = [i for i in range(lower_lim,upper_lim + 1)]
    y_val = [csquared*x**2 + clinear*x + constant for x in x_val]

    
    rect_num = int(input("Enter the number of rectangles:  "))
    interval = (upper_lim - lower_lim)/rect_num
    
    x_new = [x+interval for x in x_val]
    y_new = [csquared*x**2 + clinear*x + constant for x in x_new]
    

    
    for i in y_new:
        x = lower_lim + (y_new.index(i)*interval)
        
        rectangle = plt.Rectangle((x,0),interval,i, ec = 'r', fill = False)
        plt.gca().add_patch(rectangle)
    
    plt.plot(x_val,y_val)
    plt.show()





formular(2,8,3,7,1)






