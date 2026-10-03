# Activity 6: Set — Count Unique Vocabulary

**Topic 02: Data Types**  ·  Focus: use a set to find distinct items in text

Given the sentence 'A budget is a quantitative plan for acquiring and using resources over a specified period.', find the number of unique vocabulary words.

**You'll build:** A set-based word counter that removes duplicate words.

**Tools:** Python 3 (Colab / IDE)

## Steps

1. Create the sentence variable.

   ```python
   sent = "A budget is a quantitative plan for acquiring and using resources over a specified period."
   ```

2. Normalise the text to lowercase and strip the final full stop, so 'A' and 'a' count as the same word.

   ```python
   clean = sent.lower().replace('.', '')
   ```

3. Split the sentence into a list of words.

   ```python
   words = clean.split()
   ```

4. Convert the list to a set to drop duplicates, then count it with len().

   ```python
   unique = set(words)
   print(unique)
   print('Unique words:', len(unique))
   ```


## Check your result

The duplicate 'a' appears only once in the set, and the unique word count prints 13.
