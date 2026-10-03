# Activity 10: For Loop — Square Numbers

**Topic 04: Control Structures, Loop and Comprehension**  ·  Focus: generate a sequence with for and range()

Generate a Python list of 10 square numbers [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] using a for loop and range().

**You'll build:** A list of the first 10 square numbers built inside a for loop.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create an empty list to collect the squares.

   ```python
   squares = []
   ```

2. Loop i from 1 to 10 with range(1, 11) and append i squared each time.

   ```python
   for i in range(1, 11):
       squares.append(i ** 2)
   ```

3. Print the finished list.

   ```python
   print(squares)
   ```

4. Check your understanding of range(start, stop, step): what is list(range(2, 12, 2))?

   ```python
   print(list(range(2, 12, 2)))
   ```


## Check your result

The list prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] and range(2,12,2) gives [2, 4, 6, 8, 10].
