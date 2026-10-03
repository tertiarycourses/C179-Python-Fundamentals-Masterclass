# Activity 2: Format Numbers

**Topic 02: Data Types**  ·  Focus: format numeric output with f-strings

Given a = 4.444, b = 5.555 and c = 6.6666, use the string-literal (f-string) method to format the output as:  5.55 + 6.67 + 4.4 = 17

**You'll build:** An f-string that rounds each number to the required decimal places.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the three variables and their total.

   ```python
   a = 4.444
   b = 5.555
   c = 6.6666
   d = a + b + c
   ```

2. Print the sum with an f-string, choosing the decimal places for each value: b to 2 dp, c to 2 dp, a to 1 dp and the total to 0 dp.

   ```python
   print(f"{b:.2f} + {c:.2f} + {a:.1f} = {d:.0f}")
   ```

3. Run the cell and compare with the expected output.
4. Experiment: change the format specs (e.g. {a:10.3f}) and observe the width/decimals.

   ```python
   print(f"{a:10.3f}")
   ```


## Check your result

The output is exactly:  5.55 + 6.67 + 4.4 = 17
