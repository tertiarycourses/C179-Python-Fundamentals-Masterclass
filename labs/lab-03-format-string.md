# Activity 3: Format String

**Topic 02: Data Types**  ·  Focus: manipulate and format strings with methods and f-strings

Given bs = 'balance sheet' and income = 'income statement', print: "The finance statements typically require Balance sheet and INCOME STATEMENT." using the string-literal (f-string) method.

**You'll build:** An f-string combining capitalize() and upper() string methods.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the two variables.

   ```python
   bs = 'balance sheet'
   income = 'income statement'
   ```

2. Use capitalize() to turn 'balance sheet' into 'Balance sheet', and upper() to turn 'income statement' into 'INCOME STATEMENT', inside one f-string.

   ```python
   print(f"The finance statements typically require {bs.capitalize()} and {income.upper()}.")
   ```

3. Run the cell and check the output matches exactly, including the full stop.

## Check your result

The output is exactly: "The finance statements typically require Balance sheet and INCOME STATEMENT."
