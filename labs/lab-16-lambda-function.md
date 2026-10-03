# Activity 16: Lambda Function

**Topic 05: Function**  ·  Focus: trace and write anonymous functions

Given f = lambda x, y: 10*x + y and def g(f, x, y=0): return f(x, y) — what is g(f, 4)? Predict first, then verify.

**You'll build:** A verified trace of a lambda passed into another function with a default argument.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the lambda and the function.

   ```python
   f = lambda x, y: 10 * x + y
   
   def g(f, x, y=0):
       return f(x, y)
   ```

2. Predict: g(f, 4) calls f(4, 0) → 10*4 + 0 = 40. Verify it.

   ```python
   print(g(f, 4))
   ```

3. Write your own lambda — cube a number — and test it.

   ```python
   cube = lambda x: x ** 3
   print(cube(4))
   ```


## Check your result

g(f, 4) prints 40 and cube(4) prints 64.
