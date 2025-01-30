#test to find desired precision to use on Newton-Raphson
import numpy
import math

def NewtonRaphson(precision):
    #give a non-zero initial approximation
    pPrevious = numpy.pi / 4
    iterations = 0
    
    def f(x):
        return numpy.cos(x) - x
    
    def df(x):
        return (- numpy.sin(x) - 1)
    
    while(True):
        if(math.isclose(df(pPrevious), 0) == False):
            pNext = pPrevious - (f(pPrevious) / df(pPrevious))

            if(numpy.abs(pNext - pPrevious) < precision):
                print(f"precision: {precision};\tIterations: {iterations};\tResult: {pPrevious}")
                return
            else:
                iterations = iterations + 1
                pPrevious = pNext
        else:
            print(f"Unsuccessful: f'(x) was 0 after {iterations} iterations\n")
            return 
        
for i in range(10, 20):
    for j in range(1, 6):
         NewtonRaphson(pow(10, -i) / j)


print("\n\n\n")
NewtonRaphson(2 * pow(10, -16))

#after running, precision of 2e-16 gave us 4 iterations, matching the slides
