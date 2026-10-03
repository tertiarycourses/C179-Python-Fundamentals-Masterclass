# Activity 14: Multiple Return Values — Discount & Tax

**Topic 05: Function**  ·  Focus: return more than one value from a function

Prompt the user for the order amount, then create a function that returns BOTH the discount amount and the tax for a grocery purchase: discount is 25% if order > 200 else 0; disc_amt = discount*order/100; tax = 7% of the discounted amount.

**You'll build:** A function returning (discount amount, tax) unpacked into two variables.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Prompt for the order amount and convert it to a float.

   ```python
   order = float(input('Order amount? '))
   ```

2. Define the function computing both values, returned as a pair.

   ```python
   def bill(order):
       discount = 25 if order > 200 else 0
       disc_amt = discount * order / 100
       tax = 0.07 * (order - disc_amt)
       return disc_amt, tax
   ```

3. Call the function and unpack the two return values.

   ```python
   disc_amt, tax = bill(order)
   print(f'Discount: ${disc_amt:.2f}')
   print(f'Tax: ${tax:.2f}')
   ```

4. Test with an order of 300 (gets the discount) and 100 (no discount).

## Check your result

Order 300 → Discount $75.00 and Tax $15.75; order 100 → Discount $0.00 and Tax $7.00.
