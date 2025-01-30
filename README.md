# cot-4500-Pro1
COT4500 Spring 25 Programming Assignment 1

this program is written in python, and as such, does not need to be compiled
To run, make sure you have python installed on your computer; then, open a command line in the folder containing
the assignment_1.py file
type the following command into your command line:

python assignment_1.py

Your command line will now output the results, matching the slides
For the fixed point algorithm, there are two functions available to be used: one that converges, and one that diverges
In order to change which function it uses, open up the assignment_1.py file in an editor (i.e. Visual Studio, Notepad, etc.) and look for lines 82, and 83 (they should start with:
return 
and
#return
respectively)
Line 82 does NOT have a # in front of it, while line 83 does (83 is "commented out", meaning the program ignores it). To switch functions, add a # before line 82, and remove the # from in front of line 83. Save the file, and, when you next run it, you will see that the third block fails after 8 iterations, because it does not converge
NOTE: Commenting out (putting a # before) BOTH lines will result in errors when you try to run the program, as will leaving both lines uncommented. For the program to work, comment out one, and leave one uncommented
