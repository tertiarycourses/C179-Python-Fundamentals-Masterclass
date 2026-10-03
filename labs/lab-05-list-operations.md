# Activity 5: List Operations

**Topic 02: Data Types**  ·  Focus: manipulate lists with copy, remove, insert and reverse

Given years = ['2017','2018','2020','2021']: copy it to years2, remove '2021' from years2, insert '2019' at position 2, then reverse the order of years2.

**You'll build:** A list transformed step by step with the core list methods.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the original list.

   ```python
   years = ['2017', '2018', '2020', '2021']
   ```

2. Copy the list with copy() — NOT with years2 = years, which would only copy the reference so both names point at the same list.

   ```python
   years2 = years.copy()
   ```

3. Remove '2021' from years2.

   ```python
   years2.remove('2021')
   ```

4. Insert '2019' at index 2 of years2.

   ```python
   years2.insert(2, '2019')
   ```

5. Reverse the order of years2 and print both lists to confirm the original is untouched.

   ```python
   years2.reverse()
   print(years)
   print(years2)
   ```


## Check your result

years is unchanged ['2017','2018','2020','2021'] and years2 prints ['2020','2019','2018','2017'].
