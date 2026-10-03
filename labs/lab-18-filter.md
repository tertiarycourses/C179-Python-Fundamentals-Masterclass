# Activity 18: Filter

**Topic 05: Function**  ·  Focus: select items from a sequence with filter()

Use filter() to remove all the negative values in x = [0, 1, -4, 2, -6, 3].

**You'll build:** A filter() with a lambda that keeps only non-negative numbers.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the list.

   ```python
   x = [0, 1, -4, 2, -6, 3]
   ```

2. filter() keeps the items where the lambda returns True — keep x >= 0.

   ```python
   pos = list(filter(lambda v: v >= 0, x))
   print(pos)
   ```

3. Bonus: do the same with a list comprehension and compare.

   ```python
   print([v for v in x if v >= 0])
   ```


## Check your result

Both approaches print [0, 1, 2, 3] — the negatives are gone.
