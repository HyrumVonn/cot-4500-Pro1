import numpy

#assingment 1, question 6 parameters
# solve f(x) = x^3 + 4x^2 - 10 
# w/ accuracy < 10^-4, using a = -4, b = 7
globalA = -4
globalB = 7
globalPrecision = pow(10, -4)

#simplified for computer, should be
# ( x + 4 ) * x^2 - 10
def f(x):
    return ( x + 4 ) * pow(x, 2) - 10

def ApproximationAlgorithm(a, b, precision):
    result = 0

    return "Approx Alg here"

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

    while(error > precision):
        iterations = iterations + 1
        result = (left + right) / 2

        lY = f(left)
        rY = f(right)
        midY = f(result)

        if(ShareSigns(lY, midY)):
            left = result
            error = numpy.abs(midY - rY)
        else :
            right = result
            error = numpy.abs(midY - lY)


    return result

def FixedPointIteration(a, b, precision):
    result = 0
    return "Fixed point It"

def NewtonRaphson(a, b, precision):
    result = 0
    return "Newton Raphson Method"

#Approximation
print(f"{ApproximationAlgorithm(globalA, globalB, globalPrecision)}\n")

#Bisection
print(f"{Bisection(globalA, globalB, globalPrecision)}\n")

#Fixed-Point Iteration
print(f"{FixedPointIteration(globalA, globalB, globalPrecision)}\n")

#Newton-Raphson
print(f"{NewtonRaphson(globalA, globalB, globalPrecision)}\n")
