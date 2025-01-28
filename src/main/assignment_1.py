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

#3x^2 + 8x
#(3 * x + 8) x
def derivativeF(x):
    return (3 * x + 8) * x

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


    return result

def FixedPointIteration(a, b, precision):
    result = 0
    return "Fixed point It"

def NewtonRaphson(a, b, precision):
    result = (a + b) / 2
    iterations = 0

    while(True):
        iterations = iterations + 1
        if((derivativeF(result) > 0) or (derivativeF(result) < 0)):
            nextApprox = result - (f(result) / derivativeF(result))

            if(numpy.abs(nextApprox - result) < precision):
                return result
            else:
                result = nextApprox
        else:
            return f"Unsuccessful: f'(x) was 0 after {iterations} iterations\n"

#Approximation
print(f"{ApproximationAlgorithm(globalA, globalB, globalPrecision)}\n")

#Bisection
print(f"{Bisection(globalA, globalB, globalPrecision)}\n")

#Fixed-Point Iteration
print(f"{FixedPointIteration(globalA, globalB, globalPrecision)}\n")

#Newton-Raphson
print(f"{NewtonRaphson(globalA, globalB, globalPrecision)}\n")
