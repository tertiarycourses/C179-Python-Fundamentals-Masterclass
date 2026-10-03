# Activity 8: Conditional — Income Classifier

**Topic 04: Control Structures, Loop and Comprehension**  ·  Focus: apply if / elif / else to a business rule

Prompt the user for their income and classify it: more than 8000 → 'High income'; 4000 to 8000 → 'Medium high income'; otherwise → 'Average income'.

**You'll build:** An interactive income classifier using input() and if/elif/else.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Prompt for the income and convert the text input to an integer.

   ```python
   income = input('What is your income? ')
   income = int(income)
   ```

2. Write the if / elif / else ladder — test the highest band first.

   ```python
   if income > 8000:
       print('High income')
   elif income >= 4000:
       print('Medium high income')
   else:
       print('Average income')
   ```

3. Run the cell three times with incomes 9000, 5000 and 3000 to exercise every branch.
4. Bonus: rewrite the middle band explicitly as 4000 <= income <= 8000 — Python allows chained comparisons.

   ```python
   if 4000 <= income <= 8000:
       print('Medium high income')
   ```

5. Make the input robust: wrap the prompt in try/except inside a while True loop so a non-numeric entry like 'abc' re-prompts instead of crashing.

   ```python
   while True:
       try:
           income = int(input('What is your income? '))
           break
       except ValueError:
           print('Invalid input. Enter a number.')
   ```


## Check your result

9000 → High income, 5000 → Medium high income, 3000 → Average income; typing 'abc' re-prompts instead of crashing.
