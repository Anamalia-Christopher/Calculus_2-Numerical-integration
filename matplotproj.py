
import matplotlib.pyplot as plt
from math import *
##------------------------------------the imports as usual------------------------------------
##------------------------------------the class below is from the previous module i sent to you sometime ago------------------------------------
class Integration:
    def __init__(self, f, variable, lower, upper):
        self.f = str(f)
        self.variable = variable
        self.lower = lower
        self.upper = upper
        self.correct_input_form()


##------------------------------------the function below is to make sure that the function of the user is readable by python------------------------------------
## this does not always work. there are so many instances that the function hasn't captured such as '4log(x)'. this still gives errors. I will work on that later
    def correct_input_form(self):
        function_to_return = ''
        
        
        if "^" in self.f:

            self.f = self.f.replace("^", "**")

        for i in range(len(self.f)):

            try:
                if i > 0 and ((self.f[i] == self.variable and isinstance(int(self.f[i-1]), int)) or (self.f[i] == "(" and isinstance(int(self.f[i-1]), int))):
                    function_to_return += "*"
            except ValueError:
                pass
            finally:
                function_to_return += self.f[i]
        function_to_return = function_to_return.replace(self.variable, 'x')
        self.f = function_to_return


##------------------------------------this is the class that graphs------------------------------------

class Graph(Integration):
    def __init__(self, f, variable, lower, upper):
        super().__init__(f,variable,lower, upper)
        self.rectangle_number = int(input("Number of rectangles: "))
        

    def formular(self):
        try:
            x_points = [0.1*x for x in range(-12*int(fabs(self.lower)),12*int(fabs(self.upper)))] #gets the x coordinates for the graph 
            y_points = [eval(self.f) for x in x_points] #their corresponding y values 
        except ValueError: #throws an exception to when the function is undefined for negative values
            x_points = [0.1*x for x in range(1,12*int(fabs(self.upper)))]#x values for new one under the exception and their corresponding y values 
            y_points = [eval(self.f) for x in x_points]
            
        interval = (self.upper - self.lower)/self.rectangle_number #intervals for the rectangle


        x_rect = [self.lower + x*interval for x in range(self.rectangle_number+1)] #the x values for the rectangle
        y_rect = [eval(self.f) for x in x_rect]#the y values for the rectangle
        x_rect.pop()#takes the last rectangle which is evident of the left riemanns sum as Joe mensah taught us
        y_rect.pop()
            
        #for looking through the points for the rectangles and ploting them 
        for x,y in zip(x_rect, y_rect):
            rectangle = plt.Rectangle((x,0),interval,y, ec = 'r', fill = False)
            plt.gca().add_patch(rectangle)
        plt.plot(x_points, y_points)
        plt.axis((x_points[0],x_points[-1],y_points[0]-0.5,y_points[-1]+0.5))
        plt.show()
        

##------------------------------------These are the examples that work with my code above---------------
##Graph('tan(x)','x',10,20).formular()
##Graph('2x^2+8x+3','x',1,7).formular()
##Graph('(x+1)/(x^2+3x+5)','x',-3,6).formular()
##Graph('cos(x)', 'x', 2,5)
##Graph('sqrt(x)','x', 4,10).formular()
##Graph('log(x)','x', 4,10).formular()
Graph('4t^2 + 5*log(t) + 12t','t', 4,10).formular()
        

##you can run each of them and see how they work 


##------------------------------------Concluding comments------------------------------------
#code has been tested but i still recommend that we use the API of probably WolframAlpha to get the graphs 
#AND i think we should make sure we finish this project so that we can begin more complex projects that i stumbled on the internet


'__authors__'=='Hannah Boadiwaa Lormenyo and Christopher Anamalia'
