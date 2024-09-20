The Text Analytics Toolkit is a Python module designed for analyzing and processing textual data. It provides a set of tools to count word frequencies, extract unique words, create word co-occurrence matrices, and handle large text files efficiently. This toolkit is useful for natural language processing (NLP) tasks, enabling quick insights from textual data.

Features
1. Word Frequency Counter: Count how frequently each word appears in the text.
2. Unique Word Extractor: Extract all unique words from the text.
3. Word Co-occurrence Matrix: Create a matrix showing how frequently words appear next to each other.
4. Text Generator: Efficiently read large text files line by line.
5. Custom Filtering: Filter word frequencies using a custom function.
 
# Example usage and explanation:

## word_frequency(text_or_path, *, filter_func=None)

Description: Counts how frequently each word appears in the provided text.
- Parameters:
    - text_or_path: A string containing the text or a file path to a text file.
    - filter_func: (Optional) A function to filter the words based on custom criteria.
- Returns: A dictionary where keys are words and values are their corresponding counts
```bash
text_data = """Hello world! This is a test.
                        Hello again, world!
                        Testing word frequencies."""
print(word_frequency(text_data))
Counter({'hello': 2, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'test': 1, 'again': 1, 'testing': 1, 'word': 1, 'frequencies': 1})
```

## unique_words(text_or_path)
Description: Extracts unique words from the provided text.
- Parameters:
    - text_or_path: A string containing the text or a file path to a text file.
- Returns: A set of unique words.
```bash
text_data = """Hello world! This is a test.
                        Hello again, world!
                        Testing word frequencies."""
print(unique_words(text_data))
{'is', 'world', 'a', 'hello', 'word', 'test', 'this', 'frequencies', 'again', 'testing'}
```

## word_cooccurrence_matrix(text_or_path, window=2)
Description: Creates a word co-occurrence matrix with a specified window size.
- Parameters:
    - text_or_path: A string containing the text or a file path to a text file.
    - window: (Optional) The number of words to consider for co-occurrence (default is 2).
- Returns: A list of tuples representing co-occurring word pairs.
```bash
text_data = """Hello world! This is a test.
                        Hello again, world!
                        Testing word frequencies."""
print(word_cooccurrence_matrix(text_data))
[('hello', 'world'), ('hello', 'this'), ('world', 'this'), ('world', 'is'), ('this', 'is'), ('this', 'a'), ('is', 'a'), ('is', 'test'), ('a', 'test'), ('a', 'hello'), ('test', 'hello'), ('test', 'again'), ('hello', 'again'), ('again', 'world'), ('again', 'testing'), ('world', 'testing'), ('world', 'word'), ('testing', 'word'), ('testing', 'frequencies'), ('word', 'frequencies')]
```

## text_generator(text_or_path)

Description: A generator function that yields one line of text at a time.
- Parameters:
    - text_or_path: A string containing the text or a file path to a text file.
- Returns: A generator that yields lines of text.
```bash
text_data = """Hello world! This is a test.
                        Hello again, world!
                        Testing word frequencies."""
print(text_generator(text_data))
<generator object text_generator at 0x10245a4d0>
```