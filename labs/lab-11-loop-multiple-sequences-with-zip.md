# Activity 11: Loop Multiple Sequences with zip()

**Topic 04: Control Structures, Loop and Comprehension**  ·  Focus: iterate several lists in parallel

Given year, revenue and expense lists, fill in the blank so the loop prints each year's revenue and expense together: data = ____________; for y, r, e in data: …

**You'll build:** A zip() of three lists looped in parallel to print a mini financial report.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the three lists.

   ```python
   year = ['2017', '2018', '2019']
   revenue = [150000, 200000, 500000]
   expense = [90000, 100000, 250000]
   ```

2. Fill the blank with zip(year, revenue, expense) — zip pairs the items positionally.

   ```python
   data = zip(year, revenue, expense)
   ```

3. Loop and print with an f-string.

   ```python
   for y, r, e in data:
       print(f"{y}'s revenue is ${r} and expense is ${e}")
   ```

4. Bonus: compute the profit inside the loop.

   ```python
   for y, r, e in zip(year, revenue, expense):
       print(f'{y} profit: ${r - e}')
   ```


## Check your result

Three lines print, one per year, each showing the matching revenue and expense (e.g. 2017's revenue is $150000 and expense is $90000).
