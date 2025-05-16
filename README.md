Omnidroid Construction using Memoized Dynamic Programming

First let me give a brief description of the problem
● The main task is to calculate the total sprocket cost that requires to assemble an omnidroid
● The problem needs to be solved using dynamic programming, recursion and memoization which is required to efficiently find the cost of assembling parts.
Here is the brief overview of the Algorithm
The solution is designed in such a way that
● Dynamic programming is used to solve by breaking into smaller problems, where the cost of assembling for each part happens recursively.
● Memoization, a dictionary(memo) is used to store the computed costs for parts making sure that each part is being used only once.
● Recursion is used to calculate the cost of each part by summing the sprocket cost of the part and the part and the cost of its dependencies.

All the necessary files that are required to run the program are here.
● Input folder(It has all inputs)
● main.py( the main functionality)
● Readme.pdf ( All the explanation is in this pdf)
