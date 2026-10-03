# Activity 12: List Comprehension

**Topic 04: Control Structures, Loop and Comprehension**  ·  Focus: build a filtered list in one line

Create a list comprehension of 10 square numbers that are not divisible by 3 and 5: [1, 4, 16, 49, 64, 121, 169, 196, 256, 289]

**You'll build:** A one-line comprehension with a transform, an iteration and a filter.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Recall the pattern: [ transform  iteration  filter ].
2. The transform is x**2; iterate x over a range; filter out x divisible by 3 or 5. Squares of multiples of 3 or 5 are exactly the squares divisible by 3 or 5.

   ```python
   a = [x**2 for x in range(1, 18) if x % 3 != 0 and x % 5 != 0]
   print(a)
   print(len(a))
   ```

3. Adjust the range until the list holds exactly 10 items — range(1, 18) gives 10 qualifying squares.

## Check your result

The list prints [1, 4, 16, 49, 64, 121, 169, 196, 256, 289] with length 10.
