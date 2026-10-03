# Activity 15: Variable Arguments — Minimum Finder

**Topic 05: Function**  ·  Focus: accept any number of arguments with *args

Given a variable number of elements, create a function to determine the minimum value. E.g. for 5, 4, 7 the function returns 4. Do it with a loop — no min()!

**You'll build:** A my_min(*args) function that scans any number of values for the smallest.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Define the function with *args — the arguments arrive as a tuple.

   ```python
   def my_min(*args):
       smallest = args[0]
       for x in args:
           if x < smallest:
               smallest = x
       return smallest
   ```

2. Call it with different numbers of arguments.

   ```python
   print(my_min(5, 4, 7))
   print(my_min(9, 2, 8, 1, 6))
   ```

3. Confirm against Python's built-in min().

   ```python
   print(min(5, 4, 7))
   ```


## Check your result

my_min(5, 4, 7) prints 4 and my_min(9, 2, 8, 1, 6) prints 1 — matching min().
