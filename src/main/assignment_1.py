import numpy
import math

#3x^2 + 8x
#(3 * x + 8) x
def derivativeF(x):
    return (3 * x + 8) * x

def ApproximationAlgorithm():
    precision = pow(10, -6)
    result = 1.5
    iterations = 0
    error = precision + 1
    print(f"{iterations} : {result}")

    while(error > precision):
        iterations = iterations + 1
        y = result

        result = ( result / 2) + ( 1 / result )

        error = numpy.abs(result - y)
        print(f"{iterations} : {result}")

    return f"\nConvergence after {iterations} iterations"

#returns True if a number is negative
def isNeg(x):
    return x < 0

#returns True if the two inputs are both positive or are both negative
#otherwise, returns False
def ShareSigns(x, y):
    return isNeg(x) == isNeg(y)

def Bisection(a, b, precision):
    result = 0
    iterations = 0
    error = precision + 1
    left = a
    right = b

    #simplified for computer, should be
    # ( x + 4 ) * x^2 - 10
    def f(x):
        return ( x + 4 ) * pow(x, 2) - 10

    while(error > precision):
        iterations = iterations + 1
        result = (left + right) / 2

        lY = f(left)
        rY = f(right)
        midY = f(result)

        if(ShareSigns(lY, midY)):
            #if left and middle share a sign, then it must be
            #between right and middle; set middle as new left, then
            #repeat
            left = result
            error = numpy.abs(midY - rY)
        else :
            #if left and middle do not share a sign, then it must
            #be between left and middle; set middle as new right,
            #then repeat
            right = result
            error = numpy.abs(midY - lY)
        
        print(f"{iterations} : {result}")


    return f"\nConvergence after {iterations} iterations"

def FixedPointIteration():
    p0 = 1.5
    maxIterations = 50
    result = "Failure"
    iterations = 1
    precision = .000001

    def g(x):
        return numpy.sqrt(10 - pow(x, 3)) / 2, numpy.sqrt(4)

    # def g(x):
    #    return x - x * x * x - 4 * x * x + 10, 1.5

    while(iterations <= maxIterations):
        p, pChecker = g(p0)

        if(math.isnan(p) or (type(p) != type(pChecker))):
            print(f"\nResult diverges\n")
            break

        print(f"{iterations} : {p}")

        if(numpy.abs(p - p0) < precision):
            result = "SUCCESS"
            break
        
        iterations = iterations + 1
        p0 = p

    return f"{result} after {iterations} iterations"



def NewtonRaphson():
    #give a non-zero initial approximation
    pPrevious = numpy.pi / 4
    iterations = 0
    precision = 0.00000000000000025

    def f(x):
        return numpy.cos(x) - x
    
    def df(x):
        return (- numpy.sin(x) - 1)
    
    while(True):
        print(f"{iterations}\t{pPrevious}")
        if(math.isclose(df(pPrevious), 0) == False):
            pNext = pPrevious - (f(pPrevious) / df(pPrevious))

            if(numpy.abs(pNext - pPrevious) < precision):
                return
            else:
                iterations = iterations + 1
                pPrevious = pNext
        else:
            print(f"Unsuccessful: f'(x) was 0 after {iterations} iterations\n")
            return 

#Approximation
print(f"{ApproximationAlgorithm()}\n\n\n")

#Bisection
print(f"{Bisection(-4, 7, pow(10, -4))}\n\n\n")

#Fixed-Point Iteration
print(f"{FixedPointIteration()}\n\n\n")

#Newton-Raphson
NewtonRaphson()
