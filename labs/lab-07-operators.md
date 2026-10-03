# Activity 7: Operators

**Topic 03: Operators**  ·  Focus: evaluate comparison and logical operators

Given a = 1 and b = 2, predict and then verify: what is (a == 1) and not (b > 3)? Then explore the arithmetic and membership operators.

**You'll build:** Verified predictions of Boolean expressions and arithmetic results.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the variables and write your prediction as a comment first.

   ```python
   a = 1
   b = 2
   # my prediction: ?
   ```

2. Evaluate the expression — (a == 1) is True, (b > 3) is False, and not False is True; True and True gives True.

   ```python
   print((a == 1) and not (b > 3))
   ```

3. Try the arithmetic operators, including exponent, modulus and floor division.

   ```python
   print(2 ** 10)   # exponent
   print(7 % 3)     # modulus
   print(7 // 3)    # floor division
   ```

4. Try the compound operators — x += 1 is shorthand for x = x + 1.

   ```python
   x = 5
   x += 1
   x *= 2
   print(x)
   ```

5. Try the membership operators on a list.

   ```python
   banks = ['DBS', 'UOB', 'OCBC']
   print('DBS' in banks)
   print('HSBC' not in banks)
   ```


## Check your result

The Boolean expression prints True; 2**10 → 1024, 7%3 → 1, 7//3 → 2, x → 12, and both membership checks print True.
