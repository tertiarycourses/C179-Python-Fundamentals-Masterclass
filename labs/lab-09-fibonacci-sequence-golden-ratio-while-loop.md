# Activity 9: Fibonacci Sequence & Golden Ratio (While Loop)

**Topic 04: Control Structures, Loop and Comprehension**  ·  Focus: compute an iterative sequence with a while loop and multiple assignment

A Fibonacci number is the sum of the previous two: 1, 1, 2, 3, 5, 8, 13, 21, 34 … Use a while loop to compute the sequence up to 144 and compute the golden ratio.

**You'll build:** A while loop producing the Fibonacci sequence and the golden ratio ≈ 1.618.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Start with the first two Fibonacci numbers.

   ```python
   a, b = 1, 1
   ```

2. Loop while a has not passed 144, printing a and stepping the pair forward with MULTIPLE ASSIGNMENT — both sides are evaluated before assignment.

   ```python
   while a <= 144:
       print(a, end=' ')
       a, b = b, a + b
   ```

3. Compute the golden ratio from the last pair — the ratio of consecutive Fibonacci numbers converges to 1.618…

   ```python
   print()
   print('Golden ratio ~', b / a)
   ```

4. Why multiple assignment? Try the same update as two separate lines (a = b then b = a + b) and see the wrong sequence — a has already changed when b is computed.

   ```python
   a, b = 1, 1
   while a <= 20:
       print(a, end=' ')
       a = b
       b = a + b   # WRONG: uses the NEW a
   ```


## Check your result

The sequence prints 1 1 2 3 5 8 13 21 34 55 89 144 and the golden ratio is approximately 1.618.
