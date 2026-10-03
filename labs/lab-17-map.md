# Activity 17: Map

**Topic 05: Function**  ·  Focus: transform sequences with map() and lambda

Use map() to compute the answers for f = lambda x, y: 10*x + y with x = [0, 1, 2, 3] and y = [2, 4, 6, 8].

**You'll build:** A map() over two lists producing [2, 14, 26, 38].

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the lambda and the two lists.

   ```python
   f = lambda x, y: 10 * x + y
   x = [0, 1, 2, 3]
   y = [2, 4, 6, 8]
   ```

2. map() applies f pairwise across both lists; wrap in list() to see the results.

   ```python
   result = list(map(f, x, y))
   print(result)
   ```

3. Check one by hand: the second pair is 10*1 + 4 = 14.

## Check your result

The result prints [2, 14, 26, 38].
