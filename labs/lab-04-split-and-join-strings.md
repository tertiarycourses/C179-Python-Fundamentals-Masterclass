# Activity 4: Split and Join Strings

**Topic 02: Data Types**  ·  Focus: split a string into parts and join them back

Given email = 'finance@company.com', separate the user name and domain name, then join them back together with a '/'.

**You'll build:** Code that splits an email address and re-joins the parts with a different separator.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the email variable.

   ```python
   email = 'finance@company.com'
   ```

2. Split the email at the '@' character into a username and a domain.

   ```python
   user, domain = email.split('@')
   print(user)
   print(domain)
   ```

3. Join the two parts back with a '/' separator.

   ```python
   joined = '/'.join([user, domain])
   print(joined)
   ```


## Check your result

The output shows 'finance', then 'company.com', then 'finance/company.com'.
