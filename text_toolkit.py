import collections
import numpy as np
import re

def _read_text(text_or_path):
    """
    Helper function to read text from a file or return the string directly.
    """
    if isinstance(text_or_path, str) and '\n' in text_or_path:
        return text_or_path
    else:
        with open(text_or_path, 'r', encoding='utf-8') as f:
            return f.read()

def word_frequency(text_or_path,*,filter_func = None):
    """
    Count how frequently each word appears in the text.
    Can accept a string or a file path to a text file.
    """
    text = _read_text(text_or_path)
    words = re.findall(r'\b\w+\b', text.lower())
    words  = collections.Counter(words)
    if filter_func:
        mask = [filter_func(i) for i in words]
        return {key: value for (key, value), include in zip(words.items(), mask) if include}
    return words

def unique_words(text_or_path):
    """
    Extract unique words from the text.
    """
    text = _read_text(text_or_path)
    words = re.findall(r'\b\w+\b', text.lower())
    return set(words)

def word_cooccurrence_matrix(text_or_path, window=2):
    """
    Create a word co-occurrence matrix with a given window size.
    """
    text = _read_text(text_or_path)
    words = re.findall(r'\b\w+\b', text.lower())
    unique = list(set(words))
    index = {word: i for i, word in enumerate(unique)}
    
    co_matrix = np.zeros((len(unique), len(unique)), dtype=int)
    co_occurrences = collections.defaultdict(int)

    for i in range(len(words)):
        for j in range(1, window + 1):
            if i + j < len(words):
                word_a = words[i]
                word_b = words[i + j]
                
                # Increment co-occurrence count
                co_matrix[index[word_a]][index[word_b]] += 1
                co_matrix[index[word_b]][index[word_a]] += 1  # Undirected
                
                # Store co-occurring pairs
                if word_a != word_b:
                    co_occurrences[(word_a, word_b)] += 1

    # Convert co_occurrences to a list of tuples
    co_occurring_pairs = list(co_occurrences.keys())
    
    return co_occurring_pairs

def text_generator(text_or_path):
    """
    A generator that yields one line of text at a time.
    """
    if isinstance(text_or_path, str) and '\n' not in text_or_path:
        with open(text_or_path, 'r', encoding='utf-8') as f:
            for line in f:
                yield line.strip()
    else:
        for line in text_or_path.splitlines():
            yield line.strip()

if __name__=="__main__":
    text_data = """Hello world! This is a test.
                            Hello again, world!
                            Testing word frequencies."""
    print(word_frequency(text_data))
    print(unique_words(text_data))
    print(word_cooccurrence_matrix(text_data))
    print(text_generator(text_data))