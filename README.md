# Anagram Finder

## Objective

The purpose of this application is to find all strings from the list that contain the exact same characters as the string passed into it.  The order of the characters in the strings is not relevant.

## Approach to solving the problem:
- Sort the string elements of the array and also sort the string of the find method. After that just need to search the resultant string in the already sorted array.
- Sort the list passed as a constructor argument using quicksort and create the new array, reason for doing sorting in the constructor is that multiple calls of find method only need to sort passed string.
- In the find method, first sort the passed string, then check the indices in the sorted list
    Using the indices and return the original elements from the original list.

## Unit Testing using unittest:
- The unittest test framework is python's xUnit style framework.
-  It is a standard module that we already have. 
- It provides very useful setUp and tearDown functions.
- Use of setUp and tearDown functions to get your system ready for the tests, which called before the test can be run and once the test finishes.
- I have used the setUp method for creating the array and creating the Finder class instance.
- Also used the setUp method for holding the start time of the test.
- Used the tearDown method for printing down the time taken.

Running the program:
I have tested the program with the list of 10000 elements and each element having 10 characters. Time taken by the program was around 2 seconds.
Please run the unittest cases for checking the program.